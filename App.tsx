import React, { useState, useEffect } from 'react';
import { StyleSheet, View, ActivityIndicator } from 'react-native';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar as ExpoStatusBar } from 'expo-status-bar';
import { useFonts } from 'expo-font';
import { Level, UserProgress } from './src/types/game';
import { WORLDS } from './src/data/curriculum';
import { WORLD_LESSONS } from './src/data/lessons';
import { storageService, INITIAL_PROGRESS } from './src/services/storageService';
import { HeaderStats } from './src/components/HeaderStats';
import { LevelMap } from './src/components/LevelMap';
import { BubbleGame } from './src/components/BubbleGame';
import { TargetGame } from './src/components/TargetGame';
import { WordBuilderGame } from './src/components/WordBuilderGame';
import { SoundExplorer } from './src/components/SoundExplorer';
import { AvatarCustomizer } from './src/components/AvatarCustomizer';
import { VictoryModal } from './src/components/VictoryModal';
import { LessonModal } from './src/components/LessonModal';

type AppView = 'map' | 'playing' | 'explorer' | 'avatar';

export default function App() {
  const [fontsLoaded] = useFonts({
    'Amiri-Regular': require('./assets/fonts/Amiri-Regular.ttf'),
    'Amiri-Bold': require('./assets/fonts/Amiri-Bold.ttf'),
  });

  const [view, setView] = useState<AppView>('map');
  const [progress, setProgress] = useState<UserProgress>(INITIAL_PROGRESS);
  const [activeLevel, setActiveLevel] = useState<Level | null>(null);
  const [activeLessonWorldId, setActiveLessonWorldId] = useState<number | null>(null);

  // Victory modal state
  const [victoryVisible, setVictoryVisible] = useState(false);
  const [earnedStars, setEarnedStars] = useState(0);
  const [earnedCoins, setEarnedCoins] = useState(0);
  const [gameScore, setGameScore] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(0);

  useEffect(() => {
    loadProgress();
  }, []);

  const loadProgress = async () => {
    const saved = await storageService.getProgress();
    setProgress(saved);
  };

  const calculateTotalStars = (): number => {
    return Object.values(progress.starsByLevel).reduce((acc, curr) => acc + curr, 0);
  };

  const handleStartLevel = (level: Level) => {
    setActiveLevel(level);
    setView('playing');
  };

  const handleGameComplete = async (stars: number, coins: number, score: number, mistakes: string[]) => {
    if (!activeLevel) return;

    setEarnedStars(stars);
    setEarnedCoins(coins);
    setGameScore(score);
    const questionsCount = activeLevel.gameType === 'wordBuilder' 
      ? (activeLevel.wordItems?.length || 4)
      : activeLevel.items.length;
    setTotalQuestions(questionsCount);

    const updated = await storageService.completeLevel(activeLevel.id, stars, coins, mistakes);
    setProgress(updated);
    setVictoryVisible(true);
  };

  const handleNextLevel = () => {
    setVictoryVisible(false);
    if (!activeLevel) return;

    // Find next level
    let allLevels: Level[] = [];
    WORLDS.forEach((w) => {
      allLevels = [...allLevels, ...w.levels];
    });

    const nextIdx = allLevels.findIndex((l) => l.id === activeLevel.id) + 1;
    if (nextIdx < allLevels.length) {
      setActiveLevel(allLevels[nextIdx]);
      setView('playing');
    } else {
      setView('map');
    }
  };

  const handleReplayLevel = () => {
    setVictoryVisible(false);
    setView('map');
    setTimeout(() => {
      if (activeLevel) setView('playing');
    }, 50);
  };

  const handleReturnHome = () => {
    setVictoryVisible(false);
    setView('map');
  };

  const renderCurrentGame = () => {
    if (!activeLevel) return null;

    if (activeLevel.gameType === 'bubble') {
      return (
        <BubbleGame
          key={`bubble_${activeLevel.id}`}
          items={activeLevel.items}
          onComplete={handleGameComplete}
          onExit={handleReturnHome}
        />
      );
    }

    if (activeLevel.gameType === 'target') {
      return (
        <TargetGame
          key={`target_${activeLevel.id}`}
          items={activeLevel.items}
          onComplete={handleGameComplete}
          onExit={handleReturnHome}
        />
      );
    }

    if (activeLevel.gameType === 'wordBuilder' && activeLevel.wordItems) {
      return (
        <WordBuilderGame
          key={`word_${activeLevel.id}`}
          items={activeLevel.wordItems}
          onComplete={handleGameComplete}
          onExit={handleReturnHome}
        />
      );
    }

    return null;
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.safeArea}>
        <ExpoStatusBar style="dark" />
        <View style={styles.container}>
          {/* Top Header Stats (shown when not playing full-screen game) */}
          {view !== 'playing' && (
            <HeaderStats
              coins={progress.coins}
              totalStars={calculateTotalStars()}
              avatarBase={progress.avatar.base}
              onAvatarPress={() => setView('avatar')}
              onHomePress={handleReturnHome}
              showHome={view !== 'map'}
            />
          )}

          {/* View Router */}
          {view === 'map' && (
            <LevelMap
              progress={progress}
              onSelectLevel={handleStartLevel}
              onOpenExplorer={() => setView('explorer')}
              onOpenAvatar={() => setView('avatar')}
              onOpenLesson={(worldId) => setActiveLessonWorldId(worldId)}
            />
          )}

          {view === 'playing' && renderCurrentGame()}

          {view === 'explorer' && (
            <SoundExplorer onBack={handleReturnHome} />
          )}

          {view === 'avatar' && (
            <AvatarCustomizer
              progress={progress}
              onUpdate={setProgress}
              onBack={handleReturnHome}
            />
          )}

          {/* Victory Modal */}
          <VictoryModal
            visible={victoryVisible}
            stars={earnedStars}
            earnedCoins={earnedCoins}
            score={gameScore}
            totalQuestions={totalQuestions}
            onReplay={handleReplayLevel}
            onNext={handleNextLevel}
            onHome={handleReturnHome}
          />

          {/* World Pedagogical Lesson Modal */}
          <LessonModal
            visible={activeLessonWorldId !== null}
            lesson={activeLessonWorldId ? WORLD_LESSONS[activeLessonWorldId] : null}
            onClose={() => setActiveLessonWorldId(null)}
            onStartExercises={() => setActiveLessonWorldId(null)}
          />
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
});
