import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Animated,
  Dimensions,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { PhonemeItem } from '../types/game';
import { soundService } from '../services/soundService';
import { COLORS } from '../theme/colors';
import { useLanguage } from '../i18n/LanguageContext';

const { width } = Dimensions.get('window');

interface BubbleGameProps {
  items: PhonemeItem[];
  onComplete: (stars: number, coins: number, score: number, mistakes: string[]) => void;
  onExit: () => void;
}

interface BubbleOption {
  id: string;
  grapheme: string;
  isCorrect: boolean;
  colorIdx: number;
}

export const BubbleGame: React.FC<BubbleGameProps> = ({ items, onComplete, onExit }) => {
  const { language, t } = useLanguage();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [options, setOptions] = useState<BubbleOption[]>([]);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [mistakes, setMistakes] = useState<string[]>([]);
  const [selectedBubbleId, setSelectedBubbleId] = useState<string | null>(null);
  const [isSuccess, setIsSuccess] = useState<boolean | null>(null);

  // Animations
  const floatAnim1 = useRef(new Animated.Value(0)).current;
  const floatAnim2 = useRef(new Animated.Value(0)).current;
  const floatAnim3 = useRef(new Animated.Value(0)).current;
  const floatAnim4 = useRef(new Animated.Value(0)).current;
  const pulseAnim = useRef(new Animated.Value(1)).current;

  const currentItem = items[currentIndex];
  const isPhraseLevel = options.some((opt) => {
    const baseLetters = opt.grapheme.replace(/[\u064B-\u065F\u0670]/g, '');
    return opt.grapheme.includes(' ') || baseLetters.length > 7;
  });

  const getLocalizedPhonemeDesc = (desc?: string): string => {
    if (!desc) return '';
    if (language === 'fr') return desc;
    const d = desc.toLowerCase();
    if (d.includes('début')) return t.posInitial;
    if (d.includes('milieu')) return t.posMedial;
    if (d.includes('fin')) return t.posFinal;
    if (d.includes('isol')) return t.posIsolated;
    return desc;
  };

  useEffect(() => {
    // Floating animation loop
    const createFloating = (anim: Animated.Value, delay: number) => {
      Animated.loop(
        Animated.sequence([
          Animated.timing(anim, { toValue: -8, duration: 1500, delay, useNativeDriver: true }),
          Animated.timing(anim, { toValue: 8, duration: 1500, useNativeDriver: true }),
          Animated.timing(anim, { toValue: 0, duration: 1500, useNativeDriver: true }),
        ])
      ).start();
    };

    createFloating(floatAnim1, 0);
    createFloating(floatAnim2, 400);
    createFloating(floatAnim3, 800);
    createFloating(floatAnim4, 1200);
  }, []);

  // Setup question options
  useEffect(() => {
    if (!currentItem) return;

    const allChoices: BubbleOption[] = [
      { id: 'correct', grapheme: currentItem.grapheme, isCorrect: true, colorIdx: 0 },
      ...currentItem.distractors.map((dist, idx) => ({
        id: `dist_${idx}`,
        grapheme: dist,
        isCorrect: false,
        colorIdx: (idx + 1) % COLORS.bubbleColors.length,
      })),
    ];

    // Fisher-Yates unbiased uniform shuffle
    const shuffled = [...allChoices];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }

    setOptions(shuffled);
    setSelectedBubbleId(null);
    setIsSuccess(null);

    // Speak target sound
    const timer = setTimeout(() => {
      playCurrentSound();
    }, 400);

    return () => clearTimeout(timer);
  }, [currentIndex]);

  const playCurrentSound = () => {
    if (!currentItem) return;
    soundService.playSound(currentItem.id, currentItem.audioText || currentItem.grapheme);

    // Pulse the sound speaker
    Animated.sequence([
      Animated.timing(pulseAnim, { toValue: 1.25, duration: 180, useNativeDriver: true }),
      Animated.timing(pulseAnim, { toValue: 1, duration: 180, useNativeDriver: true }),
    ]).start();
  };

  const handleBubblePress = (option: BubbleOption) => {
    if (selectedBubbleId !== null) return; // Prevent double tap

    setSelectedBubbleId(option.id);
    soundService.triggerPop();

    if (option.isCorrect) {
      setIsSuccess(true);
      soundService.triggerSuccess();
      setScore((s) => s + 1);
      setStreak((st) => st + 1);

      setTimeout(() => {
        if (currentIndex + 1 < items.length) {
          setCurrentIndex((i) => i + 1);
        } else {
          // Finished level
          const finalScore = score + 1;
          const stars = finalScore === items.length ? 3 : finalScore >= items.length * 0.7 ? 2 : 1;
          const coins = stars * 10 + 5;
          onComplete(stars, coins, finalScore, mistakes);
        }
      }, 1000);
    } else {
      setIsSuccess(false);
      soundService.triggerError();
      setStreak(0);
      setMistakes((m) => [...m, currentItem.grapheme]);

      // Pronounce the wrong letter to teach the difference
      setTimeout(() => {
        soundService.playSound(undefined, option.grapheme);
      }, 300);

      setTimeout(() => {
        setSelectedBubbleId(null);
        setIsSuccess(null);
      }, 1200);
    }
  };

  const getAnimForIndex = (index: number) => {
    switch (index % 4) {
      case 0: return floatAnim1;
      case 1: return floatAnim2;
      case 2: return floatAnim3;
      default: return floatAnim4;
    }
  };

  if (!currentItem) return null;

  const progressPercent = ((currentIndex + 1) / items.length) * 100;

  return (
    <LinearGradient colors={['#E0F2FE', '#BAE6FD', '#7DD3FC']} style={styles.container}>
      {/* Top Bar */}
      <View style={styles.topBar}>
        <TouchableOpacity style={styles.exitBtn} onPress={onExit}>
          <Ionicons name="close" size={26} color="#0F172A" />
        </TouchableOpacity>

        {/* Progress Bar */}
        <View style={styles.progressBarContainer}>
          <View style={[styles.progressBarFill, { width: `${progressPercent}%` }]} />
        </View>

        <View style={styles.counterBadge}>
          <Text style={styles.counterText}>
            {currentIndex + 1}/{items.length}
          </Text>
        </View>
      </View>

      {/* Center Sound Speaker (The Grapho Audio Prompt) */}
      <View style={styles.promptArea}>
        <Text style={styles.instructionText}>
          {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
          currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
          currentItem.phonemeDesc?.toLowerCase().includes('fin')
            ? `${t.bubbleInstructionShape} ${getLocalizedPhonemeDesc(currentItem.phonemeDesc)}`
            : t.bubbleInstructionLetter}
        </Text>
        <Text style={styles.instructionAr}>
          {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
          currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
          currentItem.phonemeDesc?.toLowerCase().includes('fin')
            ? 'اخْتَرِ الشَّكْلَ المُنَاسِبَ لِمَوْقِعِ الحَرْف'
            : 'اِسْتَمِعْ وَاخْتَرِ الحَرْفَ المُنَاسِب'}
        </Text>

        <TouchableOpacity style={styles.speakerButton} onPress={playCurrentSound} activeOpacity={0.8}>
          <Animated.View style={[styles.speakerInner, { transform: [{ scale: pulseAnim }] }]}>
            <LinearGradient colors={['#3B82F6', '#1D4ED8']} style={styles.speakerGradient}>
              <Ionicons name="volume-high" size={44} color="#FFFFFF" />
            </LinearGradient>
          </Animated.View>
        </TouchableOpacity>

        {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
        currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
        currentItem.phonemeDesc?.toLowerCase().includes('fin') ? (
          <View style={styles.hintPill}>
            <Ionicons name="locate" size={14} color="#1E40AF" />
            <Text style={styles.hintPillText}>{getLocalizedPhonemeDesc(currentItem.phonemeDesc)}</Text>
          </View>
        ) : (
          <Text style={styles.phonemeHint}>{t.bubbleReplayHint}</Text>
        )}
      </View>

      {/* Floating Bubbles Grid */}
      <View style={[styles.bubblesGrid, isPhraseLevel && styles.bubblesColumn]}>
        {options.map((opt, index) => {
          const color = COLORS.bubbleColors[opt.colorIdx];
          const isSelected = selectedBubbleId === opt.id;
          const anim = getAnimForIndex(index);

          let bubbleBg = color.bg;
          let bubbleBorder = color.border;

          if (isSelected) {
            bubbleBg = isSuccess ? '#D1FAE5' : '#FEE2E2';
            bubbleBorder = isSuccess ? '#10B981' : '#EF4444';
          }

          return (
            <Animated.View
              key={opt.id}
              style={[
                styles.bubbleWrapper,
                isPhraseLevel && styles.bubbleWrapperPhrase,
                { transform: [{ translateY: anim }] },
              ]}
            >
              <TouchableOpacity
                style={[
                  styles.bubble,
                  isPhraseLevel && styles.bubblePhrase,
                  { backgroundColor: bubbleBg, borderColor: bubbleBorder },
                ]}
                onPress={() => handleBubblePress(opt)}
                activeOpacity={0.7}
              >
              <View style={styles.bubbleContentWrapper}>
                <Text
                  style={[
                    styles.bubbleText,
                    { color: color.text },
                    opt.grapheme.length > 16
                      ? styles.bubbleTextExtraSmall
                      : opt.grapheme.length > 8
                      ? styles.bubbleTextSmall
                      : opt.grapheme.length > 4
                      ? styles.bubbleTextMedium
                      : null,
                  ]}
                  numberOfLines={2}
                  adjustsFontSizeToFit
                >
                  {opt.grapheme}
                </Text>
              </View>

                {isSelected && (
                  <View style={styles.feedbackIcon}>
                    <Ionicons
                      name={isSuccess ? 'checkmark-circle' : 'close-circle'}
                      size={30}
                      color={isSuccess ? '#10B981' : '#EF4444'}
                    />
                  </View>
                )}
              </TouchableOpacity>
            </Animated.View>
          );
        })}
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
    paddingBottom: 30,
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
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  progressBarContainer: {
    flex: 1,
    height: 14,
    backgroundColor: 'rgba(255, 255, 255, 0.6)',
    borderRadius: 7,
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#10B981',
    borderRadius: 7,
  },
  counterBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.85)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 14,
  },
  counterText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
  },
  promptArea: {
    alignItems: 'center',
    marginTop: 6,
  },
  instructionText: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E3A8A',
    marginBottom: 2,
  },
  instructionAr: {
    fontSize: 17,
    fontWeight: '800',
    color: '#1E40AF',
    marginBottom: 10,
  },
  speakerButton: {
    marginVertical: 4,
  },
  speakerInner: {
    width: 88,
    height: 88,
    borderRadius: 44,
    ...Platform.select({
      ios: { shadowColor: '#1D4ED8', shadowOffset: { width: 0, height: 8 }, shadowOpacity: 0.35, shadowRadius: 10 },
      android: { elevation: 8 },
      web: { boxShadow: '0 10px 15px -3px rgba(29, 78, 216, 0.4)' } as any,
    }),
  },
  speakerGradient: {
    width: '100%',
    height: '100%',
    borderRadius: 44,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 4,
    borderColor: '#FFFFFF',
  },
  phonemeHint: {
    marginTop: 8,
    fontSize: 14,
    fontWeight: '600',
    color: '#334155',
  },
  hintPill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#DBEAFE',
    borderWidth: 1.5,
    borderColor: '#93C5FD',
    paddingHorizontal: 14,
    paddingVertical: 4,
    borderRadius: 16,
    marginTop: 8,
  },
  hintPillText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#1E40AF',
  },
  bubblesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 12,
    paddingBottom: 10,
  },
  bubblesColumn: {
    flexDirection: 'column',
    alignItems: 'center',
    flexWrap: 'nowrap',
    width: '100%',
    gap: 10,
  },
  bubbleWrapper: {
    width: (width - 44) / 2,
    maxWidth: 180,
    aspectRatio: 1,
  },
  bubbleWrapperPhrase: {
    width: '100%',
    maxWidth: 420,
    aspectRatio: undefined,
  },
  bubble: {
    width: '100%',
    height: '100%',
    borderRadius: 36,
    borderWidth: 3.5,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 6,
    paddingVertical: 6,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 6 }, shadowOpacity: 0.12, shadowRadius: 8 },
      android: { elevation: 5 },
      web: { boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)' } as any,
    }),
  },
  bubblePhrase: {
    height: undefined,
    minHeight: 68,
    borderRadius: 22,
    paddingHorizontal: 16,
    paddingVertical: 10,
  },
  bubbleContentWrapper: {
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  bubbleText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 58,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextMedium: {
    fontSize: 40,
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextSmall: {
    fontSize: 30,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextExtraSmall: {
    fontSize: 24,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  feedbackIcon: {
    position: 'absolute',
    top: 6,
    right: 8,
  },
});

