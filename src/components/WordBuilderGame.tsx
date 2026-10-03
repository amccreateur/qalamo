import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Dimensions,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WordItem } from '../types/game';
import { soundService } from '../services/soundService';

const { width } = Dimensions.get('window');

interface WordBuilderGameProps {
  items: WordItem[];
  onComplete: (stars: number, coins: number, score: number, mistakes: string[]) => void;
  onExit: () => void;
}

export const WordBuilderGame: React.FC<WordBuilderGameProps> = ({ items, onComplete, onExit }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [placedLetters, setPlacedLetters] = useState<string[]>([]);
  const [poolLetters, setPoolLetters] = useState<{ id: string; letter: string }[]>([]);
  const [score, setScore] = useState(0);
  const [mistakes, setMistakes] = useState<string[]>([]);
  const [isCompletedWord, setIsCompletedWord] = useState(false);

  const currentWord = items[currentIndex];

  useEffect(() => {
    if (!currentWord) return;

    setPlacedLetters([]);
    setIsCompletedWord(false);

    // Create pool of letters (correct letters + distractors)
    const all = [
      ...currentWord.letters.map((l, i) => ({ id: `cor_${i}_${l}`, letter: l })),
      ...currentWord.distractorLetters.map((d, i) => ({ id: `dis_${i}_${d}`, letter: d })),
    ];

    // Fisher-Yates unbiased uniform shuffle
    for (let i = all.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [all[i], all[j]] = [all[j], all[i]];
    }

    setPoolLetters(all);

    const timer = setTimeout(() => {
      playWordAudio();
    }, 400);

    return () => clearTimeout(timer);
  }, [currentIndex]);

  const playWordAudio = () => {
    if (!currentWord) return;
    soundService.playSound(currentWord.id, currentWord.word);
  };

  const handleSelectLetter = (poolItem: { id: string; letter: string }) => {
    if (isCompletedWord) return;

    const nextSlotIndex = placedLetters.length;
    const expectedLetter = currentWord.letters[nextSlotIndex];

    soundService.triggerPop();
    soundService.playSound(undefined, poolItem.letter);

    if (poolItem.letter === expectedLetter) {
      // Correct letter placement
      const nextPlaced = [...placedLetters, poolItem.letter];
      setPlacedLetters(nextPlaced);
      setPoolLetters((prev) => prev.filter((p) => p.id !== poolItem.id));

      if (nextPlaced.length === currentWord.letters.length) {
        // Complete word assembled!
        setIsCompletedWord(true);
        soundService.triggerSuccess();
        setScore((s) => s + 1);

        // Speak full word using studio audio
        setTimeout(() => {
          soundService.playSound(currentWord.id, currentWord.word);
        }, 500);

        setTimeout(() => {
          if (currentIndex + 1 < items.length) {
            setCurrentIndex((i) => i + 1);
          } else {
            const finalScore = score + 1;
            const stars = finalScore === items.length ? 3 : finalScore >= items.length * 0.7 ? 2 : 1;
            const coins = stars * 12 + 10;
            onComplete(stars, coins, finalScore, mistakes);
          }
        }, 1600);
      }
    } else {
      // Wrong letter
      soundService.triggerError();
      setMistakes((m) => [...m, currentWord.word]);
    }
  };

  const handleResetCurrent = () => {
    if (!currentWord || isCompletedWord) return;
    setPlacedLetters([]);
    const all = [
      ...currentWord.letters.map((l, i) => ({ id: `cor_${i}_${l}`, letter: l })),
      ...currentWord.distractorLetters.map((d, i) => ({ id: `dis_${i}_${d}`, letter: d })),
    ].sort(() => Math.random() - 0.5);
    setPoolLetters(all);
  };

  if (!currentWord) return null;

  const progressPercent = ((currentIndex + 1) / items.length) * 100;

  return (
    <LinearGradient colors={['#064E3B', '#047857', '#10B981']} style={styles.container}>
      {/* Top Bar */}
      <View style={styles.topBar}>
        <TouchableOpacity style={styles.exitBtn} onPress={onExit}>
          <Ionicons name="close" size={24} color="#FFFFFF" />
        </TouchableOpacity>

        <View style={styles.progressBarContainer}>
          <View style={[styles.progressBarFill, { width: `${progressPercent}%` }]} />
        </View>

        <View style={styles.counterBadge}>
          <Text style={styles.counterText}>
            {currentIndex + 1}/{items.length}
          </Text>
        </View>
      </View>

      {/* Word Illustration & Audio Prompt */}
      <View style={styles.wordStage}>
        {currentWord.emoji ? <Text style={styles.emoji}>{currentWord.emoji}</Text> : null}
        
        <TouchableOpacity style={styles.speakerPill} onPress={playWordAudio} activeOpacity={0.8}>
          <Ionicons name="volume-high" size={26} color="#065F46" />
          <Text style={styles.speakerPillText}>Écouter le mot</Text>
        </TouchableOpacity>

        {Boolean((currentWord.translationFr || currentWord.meaning || '').replace(/\s*\([^)]*\)/g, '').trim()) && (
          <Text style={styles.meaningText}>
            {(currentWord.translationFr || currentWord.meaning || '').replace(/\s*\([^)]*\)/g, '').trim()}
          </Text>
        )}
      </View>

      {/* Word Slots (assembled word) */}
      <View style={styles.slotsRow}>
        {currentWord.letters.map((_, idx) => {
          const letter = placedLetters[idx];
          const isCurrentSlot = placedLetters.length === idx;

          return (
            <View
              key={`slot_${idx}`}
              style={[
                styles.slot,
                letter ? styles.slotFilled : isCurrentSlot ? styles.slotActive : styles.slotEmpty,
              ]}
            >
              <Text style={styles.slotText}>{letter || '...'}</Text>
            </View>
          );
        })}
      </View>

      {/* If completed, show full connected word */}
      {isCompletedWord && (
        <View style={styles.fullWordBadge}>
          <Text style={styles.fullWordText}>{currentWord.word}</Text>
        </View>
      )}

      {/* Available Letters Pool */}
      <View style={styles.poolSection}>
        <View style={styles.poolHeader}>
          <Text style={styles.poolInstruction}>Touche les lettres dans le bon ordre :</Text>
          {placedLetters.length > 0 && !isCompletedWord && (
            <TouchableOpacity onPress={handleResetCurrent} style={styles.resetBtn}>
              <Ionicons name="refresh" size={16} color="#FFFFFF" />
              <Text style={styles.resetBtnText}>Effacer</Text>
            </TouchableOpacity>
          )}
        </View>

        <View style={styles.lettersPool}>
          {poolLetters.map((p) => (
            <TouchableOpacity
              key={p.id}
              style={styles.letterTile}
              onPress={() => handleSelectLetter(p)}
              activeOpacity={0.7}
            >
              <Text style={styles.letterTileText}>{p.letter}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === 'ios' ? 50 : 20,
    paddingHorizontal: 16,
    justifyContent: 'space-between',
    paddingBottom: 40,
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 12,
  },
  exitBtn: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  progressBarContainer: {
    flex: 1,
    height: 14,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    borderRadius: 7,
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#38BDF8',
    borderRadius: 7,
  },
  counterBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.25)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 14,
  },
  counterText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  wordStage: {
    alignItems: 'center',
    marginVertical: 10,
  },
  emoji: {
    fontSize: 64,
    marginBottom: 10,
  },
  speakerPill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 30,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.15, shadowRadius: 6 },
      android: { elevation: 4 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.1)' } as any,
    }),
  },
  speakerPillText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#065F46',
  },
  meaningText: {
    marginTop: 10,
    fontSize: 18,
    fontWeight: '700',
    color: '#D1FAE5',
  },
  slotsRow: {
    flexDirection: 'row-reverse', // Arabic RTL order
    justifyContent: 'center',
    gap: 12,
    marginVertical: 12,
    flexWrap: 'wrap',
  },
  slot: {
    minWidth: 72,
    maxWidth: 90,
    height: 84,
    paddingHorizontal: 8,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 3,
  },
  slotEmpty: {
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderColor: 'rgba(255, 255, 255, 0.3)',
  },
  slotActive: {
    backgroundColor: 'rgba(255, 255, 255, 0.35)',
    borderColor: '#FDE047',
  },
  slotFilled: {
    backgroundColor: '#FFFFFF',
    borderColor: '#34D399',
  },
  slotText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 44,
    fontWeight: '700',
    color: '#064E3B',
    includeFontPadding: true,
    textAlign: 'center',
  },
  fullWordBadge: {
    alignSelf: 'center',
    backgroundColor: '#FEF08A',
    paddingHorizontal: 28,
    paddingVertical: 10,
    borderRadius: 24,
    marginBottom: 8,
    borderWidth: 2,
    borderColor: '#FACC15',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.2, shadowRadius: 6 },
      android: { elevation: 4 },
      web: { boxShadow: '0 4px 10px rgba(0,0,0,0.15)' } as any,
    }),
  },
  fullWordText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 46,
    fontWeight: '700',
    color: '#713F12',
    textAlign: 'center',
    includeFontPadding: true,
  },
  poolSection: {
    backgroundColor: 'rgba(0, 0, 0, 0.25)',
    borderRadius: 28,
    padding: 16,
  },
  poolHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  poolInstruction: {
    fontSize: 14,
    fontWeight: '700',
    color: '#E0E7FF',
  },
  resetBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  resetBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  lettersPool: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 12,
  },
  letterTile: {
    minWidth: 70,
    height: 72,
    paddingHorizontal: 10,
    borderRadius: 20,
    backgroundColor: '#FFFFFF',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2.5,
    borderColor: '#D1D5DB',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.15, shadowRadius: 4 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.1)' } as any,
    }),
  },
  letterTileText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 44,
    fontWeight: '700',
    color: '#1F2937',
    includeFontPadding: false,
    textAlign: 'center',
  },
});

