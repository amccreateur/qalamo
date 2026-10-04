import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { World, Level, UserProgress } from '../types/game';
import { WORLDS } from '../data/curriculum';
import { soundService } from '../services/soundService';
import { useLanguage } from '../i18n/LanguageContext';

interface LevelMapProps {
  progress: UserProgress;
  onSelectLevel: (level: Level) => void;
  onOpenExplorer: () => void;
  onOpenAvatar: () => void;
  onOpenLesson: (worldId: number) => void;
}

export const LevelMap: React.FC<LevelMapProps> = ({
  progress,
  onSelectLevel,
  onOpenExplorer,
  onOpenAvatar,
  onOpenLesson,
}) => {
  const { language, t } = useLanguage();

  const getGameIcon = (type: Level['gameType']) => {
    switch (type) {
      case 'bubble': return 'radio-button-on';
      case 'target': return 'disc';
      case 'wordBuilder': return 'extension-puzzle';
      default: return 'play';
    }
  };

  const getGameLabel = (type: Level['gameType']) => {
    switch (type) {
      case 'bubble': return t.bubbleGameLabel;
      case 'target': return t.targetGameLabel;
      case 'wordBuilder': return t.wordBuilderGameLabel;
      default: return t.miniGameLabel;
    }
  };

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.scrollContent}>
      {/* Quick Access Top Bar */}
      <View style={styles.quickAccessRow}>
        <TouchableOpacity style={styles.quickCard} onPress={onOpenExplorer} activeOpacity={0.8}>
          <LinearGradient colors={['#3B82F6', '#1D4ED8']} style={styles.quickGradient}>
            <Ionicons name="mic" size={24} color="#FFFFFF" />
            <View>
              <Text style={styles.quickTitle}>{t.quickExplorerTitle}</Text>
              <Text style={styles.quickSubtitle}>{t.quickExplorerSubtitle}</Text>
            </View>
          </LinearGradient>
        </TouchableOpacity>

        <TouchableOpacity style={styles.quickCard} onPress={onOpenAvatar} activeOpacity={0.8}>
          <LinearGradient colors={['#F59E0B', '#D97706']} style={styles.quickGradient}>
            <Ionicons name="shirt" size={24} color="#FFFFFF" />
            <View>
              <Text style={styles.quickTitle}>{t.quickAvatarTitle}</Text>
              <Text style={styles.quickSubtitle}>{t.quickAvatarSubtitle}</Text>
            </View>
          </LinearGradient>
        </TouchableOpacity>
      </View>

      {/* Worlds and Levels List */}
      {WORLDS.map((world: World, wIdx: number) => {
        const worldName = language === 'en' ? (world.nameEn || world.name) : world.name;
        const worldDesc = language === 'en' ? (world.descriptionEn || world.description) : world.description;

        return (
          <View key={world.id} style={styles.worldContainer}>
            {/* World Header Card */}
            <View style={styles.worldHeader}>
              <View style={[styles.worldIconCircle, { backgroundColor: world.color }]}>
                <Ionicons name="planet" size={24} color="#FFFFFF" />
              </View>
              <View style={styles.worldTitleBox}>
                <Text style={styles.worldName}>{worldName}</Text>
                <Text style={styles.worldNameAr}>{world.nameAr}</Text>
                <Text style={styles.worldDesc}>{worldDesc}</Text>

                {/* Lesson button for the world */}
                <TouchableOpacity
                  style={[styles.lessonPillBtn, { backgroundColor: `${world.color}15`, borderColor: world.color }]}
                  onPress={() => onOpenLesson(world.id)}
                  activeOpacity={0.7}
                >
                  <Ionicons name="book" size={14} color={world.color} />
                  <Text style={[styles.lessonPillText, { color: world.color }]}>
                    {t.discoverLessonBtn}
                  </Text>
                  <Ionicons name="chevron-forward" size={12} color={world.color} />
                </TouchableOpacity>
              </View>
            </View>

            {/* Levels along the road */}
            <View style={styles.levelsList}>
              {world.levels.map((level: Level, lIdx: number) => {
                const isUnlocked = true; // Débloqué pour tests
                const earnedStars = progress.starsByLevel[level.id] || 0;
                const levelTitle = language === 'en' ? (level.titleEn || level.title) : level.title;

                return (
                  <TouchableOpacity
                    key={level.id}
                    style={[
                      styles.levelCard,
                      !isUnlocked && styles.levelCardLocked,
                    ]}
                    onPress={() => {
                      if (isUnlocked) {
                        soundService.triggerPop();
                        onSelectLevel(level);
                      } else {
                        soundService.triggerError();
                      }
                    }}
                    activeOpacity={isUnlocked ? 0.7 : 1}
                  >
                    <LinearGradient
                      colors={isUnlocked ? level.bgColor : ['#E2E8F0', '#CBD5E1']}
                      style={styles.levelCardGradient}
                    >
                      {/* Left Number & Status */}
                      <View style={styles.levelNumberCircle}>
                        {isUnlocked ? (
                          <Text style={styles.levelNumber}>{level.id}</Text>
                        ) : (
                          <Ionicons name="lock-closed" size={18} color="#94A3B8" />
                        )}
                      </View>

                      {/* Middle Content */}
                      <View style={styles.levelInfo}>
                        <View style={styles.gameTypeTag}>
                          <Ionicons
                            name={getGameIcon(level.gameType) as any}
                            size={12}
                            color={isUnlocked ? '#FFFFFF' : '#64748B'}
                          />
                          <Text
                            style={[
                              styles.gameTypeText,
                              { color: isUnlocked ? 'rgba(255,255,255,0.9)' : '#64748B' },
                            ]}
                          >
                            {getGameLabel(level.gameType)}
                          </Text>
                        </View>
                        <Text style={[styles.levelTitle, { color: isUnlocked ? '#FFFFFF' : '#475569' }]}>
                          {levelTitle}
                        </Text>
                        <Text style={[styles.levelTitleAr, { color: isUnlocked ? '#FEF08A' : '#94A3B8' }]}>
                          {level.titleAr}
                        </Text>
                      </View>

                      {/* Right Stars */}
                      <View style={styles.starsColumn}>
                        <View style={styles.starsRow}>
                          {[1, 2, 3].map((starIdx) => (
                            <Ionicons
                              key={starIdx}
                              name={earnedStars >= starIdx ? 'star' : 'star-outline'}
                              size={18}
                              color={earnedStars >= starIdx ? '#FBBF24' : isUnlocked ? 'rgba(255,255,255,0.5)' : '#94A3B8'}
                            />
                          ))}
                        </View>
                        {isUnlocked && (
                          <View style={styles.playButtonPill}>
                            <Text style={styles.playButtonText}>{language === 'en' ? 'Play' : 'Jouer'}</Text>
                            <Ionicons name="chevron-forward" size={14} color="#1E293B" />
                          </View>
                        )}
                      </View>
                    </LinearGradient>
                  </TouchableOpacity>
                );
              })}
            </View>
          </View>
        );
      })}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F1F5F9',
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 50,
  },
  quickAccessRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 20,
  },
  quickCard: {
    flex: 1,
    borderRadius: 20,
    overflow: 'hidden',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.1, shadowRadius: 6 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.1)' } as any,
    }),
  },
  quickGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    padding: 14,
  },
  quickTitle: {
    fontSize: 15,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  quickSubtitle: {
    fontSize: 11,
    fontWeight: '600',
    color: 'rgba(255, 255, 255, 0.85)',
  },
  worldContainer: {
    marginBottom: 28,
  },
  worldHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 24,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.05, shadowRadius: 4 },
      android: { elevation: 2 },
      web: { boxShadow: '0 2px 4px rgba(0,0,0,0.05)' } as any,
    }),
  },
  worldIconCircle: {
    width: 48,
    height: 48,
    borderRadius: 24,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 14,
  },
  worldTitleBox: {
    flex: 1,
  },
  worldName: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
  },
  worldNameAr: {
    fontSize: 14,
    fontWeight: '700',
    color: '#3B82F6',
    marginTop: 2,
  },
  worldDesc: {
    fontSize: 12,
    fontWeight: '500',
    color: '#64748B',
    marginTop: 2,
  },
  lessonPillBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'flex-start',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 12,
    borderWidth: 1,
    marginTop: 8,
  },
  lessonPillText: {
    fontSize: 12,
    fontWeight: '800',
  },
  levelsList: {
    gap: 12,
  },
  levelCard: {
    borderRadius: 22,
    overflow: 'hidden',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.12, shadowRadius: 6 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.08)' } as any,
    }),
  },
  levelCardLocked: {
    opacity: 0.75,
  },
  levelCardGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    gap: 12,
  },
  levelNumberCircle: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: '#FFFFFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  levelNumber: {
    fontSize: 18,
    fontWeight: '900',
    color: '#1E293B',
  },
  levelInfo: {
    flex: 1,
  },
  gameTypeTag: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    marginBottom: 4,
  },
  gameTypeText: {
    fontSize: 11,
    fontWeight: '700',
  },
  levelTitle: {
    fontSize: 15,
    fontWeight: '800',
  },
  levelTitleAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 18,
    fontWeight: '700',
    marginTop: 2,
  },
  starsColumn: {
    alignItems: 'flex-end',
    gap: 6,
  },
  starsRow: {
    flexDirection: 'row',
    gap: 2,
  },
  playButtonPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    gap: 2,
  },
  playButtonText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#1E293B',
  },
});
