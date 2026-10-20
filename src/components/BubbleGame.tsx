import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Animated,
  useWindowDimensions,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { PhonemeItem } from '../types/game';
import { soundService } from '../services/soundService';
import { COLORS } from '../theme/colors';
import { useLanguage } from '../i18n/LanguageContext';
import { PlaybackSpeedToggle } from './PlaybackSpeedToggle';

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
  const { width, height } = useWindowDimensions();
  const isTablet = Math.min(width, height) >= 600;

  const [currentIndex, setCurrentIndex] = useState(0);
  const [options, setOptions] = useState<BubbleOption[]>([]);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [mistakes, setMistakes] = useState<string[]>([]);
  const [selectedBubbleId, setSelectedBubbleId] = useState<string | null>(null);
  const [isSuccess, setIsSuccess] = useState<boolean | null>(null);
  const [playbackSpeed, setPlaybackSpeed] = useState<number>(soundService.getPlaybackSpeed());

  // Animations
  const floatAnim1 = useRef(new Animated.Value(0)).current;
  const floatAnim2 = useRef(new Animated.Value(0)).current;
  const floatAnim3 = useRef(new Animated.Value(0)).current;
  const floatAnim4 = useRef(new Animated.Value(0)).current;
  const pulseAnim = useRef(new Animated.Value(1)).current;

  const currentItem = items[currentIndex];
  const isPhraseLevel = items.some((item) => {
    const baseLetters = item.grapheme.replace(/[\u064B-\u065F\u0670]/g, '');
    return item.grapheme.includes(' ') || baseLetters.length > 7;
  }) || options.some((opt) => opt.grapheme.includes(' '));

  const isWordLevel = !isPhraseLevel && (
    items.some((item) => {
      const baseLetters = item.grapheme.replace(/[\u064B-\u065F\u0670]/g, '');
      return baseLetters.length >= 2;
    }) || options.some((opt) => {
      const baseLetters = opt.grapheme.replace(/[\u064B-\u065F\u0670]/g, '');
      return baseLetters.length >= 2;
    })
  );

  const isWordOrPhrase = isPhraseLevel || isWordLevel;

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

  const getInstruction = (): string => {
    const hasPosition = currentItem?.phonemeDesc?.toLowerCase().includes('début') ||
      currentItem?.phonemeDesc?.toLowerCase().includes('milieu') ||
      currentItem?.phonemeDesc?.toLowerCase().includes('fin');

    if (hasPosition) {
      return `${t.bubbleInstructionShape} ${getLocalizedPhonemeDesc(currentItem.phonemeDesc)}`;
    }
    if (isPhraseLevel) {
      return t.bubbleInstructionPhrase;
    }
    if (isWordLevel) {
      return t.bubbleInstructionWord;
    }
    return t.bubbleInstructionLetter;
  };

  const getInstructionAr = (): string => {
    const hasPosition = currentItem?.phonemeDesc?.toLowerCase().includes('début') ||
      currentItem?.phonemeDesc?.toLowerCase().includes('milieu') ||
      currentItem?.phonemeDesc?.toLowerCase().includes('fin');

    if (hasPosition) {
      return 'اخْتَرِ الشَّكْلَ المُنَاسِبَ لِمَوْقِعِ الحَرْف';
    }
    if (isPhraseLevel) {
      return 'اِسْتَمِعْ وَاخْتَرِ الجُمْلَةَ المُنَاسِبَة';
    }
    if (isWordLevel) {
      return 'اِسْتَمِعْ وَاخْتَرِ الكَلِمَةَ المُنَاسِبَة';
    }
    return 'اِسْتَمِعْ وَاخْتَرِ الحَرْفَ المُنَاسِب';
  };

  const playCurrentSound = (speed?: number) => {
    if (!currentItem) return;
    soundService.playSound(currentItem.id, currentItem.audioText || currentItem.grapheme, speed);

    // Pulse the sound speaker
    Animated.sequence([
      Animated.timing(pulseAnim, { toValue: 1.25, duration: 180, useNativeDriver: true }),
      Animated.timing(pulseAnim, { toValue: 1, duration: 180, useNativeDriver: true }),
    ]).start();
  };

  const handleSpeedChange = (newSpeed: number) => {
    setPlaybackSpeed(newSpeed);
    playCurrentSound(newSpeed);
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
    <LinearGradient
      colors={['#E0F2FE', '#BAE6FD', '#7DD3FC']}
      style={[
        styles.container,
        isTablet && styles.containerTablet,
        isPhraseLevel && isTablet && styles.containerPhraseTablet,
      ]}
    >
      {/* Top Bar */}
      <View style={[styles.topBar, isTablet && styles.topBarTablet]}>
        <TouchableOpacity style={[styles.exitBtn, isTablet && styles.exitBtnTablet]} onPress={onExit}>
          <Ionicons name="close" size={isTablet ? 30 : 26} color="#0F172A" />
        </TouchableOpacity>

        {/* Progress Bar */}
        <View style={[styles.progressBarContainer, isTablet && styles.progressBarContainerTablet]}>
          <View style={[styles.progressBarFill, { width: `${progressPercent}%` }]} />
        </View>

        <View style={[styles.counterBadge, isTablet && styles.counterBadgeTablet]}>
          <Text style={[styles.counterText, isTablet && styles.counterTextTablet]}>
            {currentIndex + 1}/{items.length}
          </Text>
        </View>
      </View>

      {/* Center Sound Speaker (The Grapho Audio Prompt) */}
      <View style={[
        styles.promptArea,
        isPhraseLevel && styles.promptAreaPhrase,
        isTablet && styles.promptAreaTablet,
      ]}>
        <Text style={[
          styles.instructionText,
          isPhraseLevel && styles.instructionTextPhrase,
          isTablet && styles.instructionTextTablet,
        ]}>
          {getInstruction()}
        </Text>
        <Text style={[
          styles.instructionAr,
          isPhraseLevel && styles.instructionArPhrase,
          isTablet && styles.instructionArTablet,
        ]}>
          {getInstructionAr()}
        </Text>

        <TouchableOpacity
          style={[
            styles.speakerButton,
            isPhraseLevel && styles.speakerButtonPhrase,
            isTablet && styles.speakerButtonTablet,
          ]}
          onPress={() => playCurrentSound()}
          activeOpacity={0.8}
        >
          <Animated.View style={[
            styles.speakerInner,
            isPhraseLevel && styles.speakerInnerPhrase,
            isTablet && styles.speakerInnerTablet,
            { transform: [{ scale: pulseAnim }] }
          ]}>
            <LinearGradient colors={['#3B82F6', '#1D4ED8']} style={styles.speakerGradient}>
              <Ionicons
                name="volume-high"
                size={isTablet ? 48 : (isPhraseLevel ? 32 : 44)}
                color="#FFFFFF"
              />
            </LinearGradient>
          </Animated.View>
        </TouchableOpacity>

        {isWordOrPhrase && (
          <PlaybackSpeedToggle
            currentSpeed={playbackSpeed}
            onSpeedChange={handleSpeedChange}
            variant="blue"
            style={[
              { marginTop: 6, marginBottom: 4 },
              isTablet && { marginTop: 10, marginBottom: 8 },
            ]}
          />
        )}

        {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
        currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
        currentItem.phonemeDesc?.toLowerCase().includes('fin') ? (
          <View style={[styles.hintPill, isTablet && styles.hintPillTablet]}>
            <Ionicons name="locate" size={isTablet ? 18 : 14} color="#1E40AF" />
            <Text style={[styles.hintPillText, isTablet && styles.hintPillTextTablet]}>
              {getLocalizedPhonemeDesc(currentItem.phonemeDesc)}
            </Text>
          </View>
        ) : (
          <Text style={[
            styles.phonemeHint,
            isPhraseLevel && styles.phonemeHintPhrase,
            isTablet && styles.phonemeHintTablet,
          ]}>
            {t.bubbleReplayHint}
          </Text>
        )}
      </View>

      {/* Floating Bubbles / Phrase Cards Grid */}
      <View style={[
        styles.bubblesGrid,
        isPhraseLevel && styles.bubblesColumn,
        isPhraseLevel && isTablet && styles.bubblesColumnTablet,
      ]}>
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
                isPhraseLevel
                  ? (isTablet ? styles.bubbleWrapperPhraseTablet : styles.bubbleWrapperPhrase)
                  : (isTablet ? styles.bubbleWrapperRegularTablet : styles.bubbleWrapperRegular),
                { transform: [{ translateY: anim }] },
              ]}
            >
              <TouchableOpacity
                style={[
                  isPhraseLevel
                    ? (isTablet ? styles.bubblePhraseTablet : styles.bubblePhrase)
                    : (isTablet ? styles.bubbleRegularTablet : styles.bubbleRegular),
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
                      isPhraseLevel
                        ? (isTablet
                            ? (opt.grapheme.length > 25 ? styles.bubbleTextPhraseLongTablet : styles.bubbleTextPhraseTablet)
                            : (opt.grapheme.length > 25 ? styles.bubbleTextPhraseLong : styles.bubbleTextPhrase))
                        : (opt.grapheme.length > 16
                          ? styles.bubbleTextExtraSmall
                          : opt.grapheme.length > 8
                          ? styles.bubbleTextSmall
                          : opt.grapheme.length > 4
                          ? styles.bubbleTextMedium
                          : (isTablet ? styles.bubbleTextTablet : null)),
                    ]}
                    numberOfLines={2}
                    adjustsFontSizeToFit
                  >
                    {opt.grapheme}
                  </Text>
                </View>

                {isSelected && (
                  <View style={[styles.feedbackIcon, isTablet && styles.feedbackIconTablet]}>
                    <Ionicons
                      name={isSuccess ? 'checkmark-circle' : 'close-circle'}
                      size={isTablet ? 38 : 30}
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
  containerTablet: {
    paddingHorizontal: 32,
    paddingTop: Platform.OS === 'ios' ? 60 : 30,
    paddingBottom: 40,
  },
  containerPhraseTablet: {
    justifyContent: 'space-evenly',
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 12,
  },
  topBarTablet: {
    paddingHorizontal: 8,
  },
  exitBtn: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  exitBtnTablet: {
    width: 52,
    height: 52,
    borderRadius: 26,
  },
  progressBarContainer: {
    flex: 1,
    height: 14,
    backgroundColor: 'rgba(255, 255, 255, 0.6)',
    borderRadius: 7,
    overflow: 'hidden',
  },
  progressBarContainerTablet: {
    height: 18,
    borderRadius: 9,
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
  counterBadgeTablet: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 18,
  },
  counterText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
  },
  counterTextTablet: {
    fontSize: 16,
  },
  promptArea: {
    alignItems: 'center',
    marginTop: 6,
  },
  promptAreaPhrase: {
    marginTop: 2,
  },
  promptAreaTablet: {
    marginTop: 0,
    marginBottom: 8,
  },
  instructionText: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E3A8A',
    marginBottom: 2,
  },
  instructionTextPhrase: {
    fontSize: 14,
    marginBottom: 1,
  },
  instructionTextTablet: {
    fontSize: 19,
    marginBottom: 4,
  },
  instructionAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 17,
    fontWeight: '800',
    color: '#1E40AF',
    marginBottom: 10,
  },
  instructionArPhrase: {
    fontSize: 15,
    marginBottom: 4,
  },
  instructionArTablet: {
    fontSize: 24,
    marginBottom: 8,
  },
  speakerButton: {
    marginVertical: 4,
  },
  speakerButtonPhrase: {
    marginVertical: 2,
  },
  speakerButtonTablet: {
    marginVertical: 6,
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
  speakerInnerPhrase: {
    width: 74,
    height: 74,
    borderRadius: 37,
  },
  speakerInnerTablet: {
    width: 96,
    height: 96,
    borderRadius: 48,
  },
  speakerGradient: {
    width: '100%',
    height: '100%',
    borderRadius: 48,
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
  phonemeHintPhrase: {
    marginTop: 2,
    fontSize: 11,
  },
  phonemeHintTablet: {
    fontSize: 14,
    marginTop: 6,
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
  hintPillTablet: {
    paddingHorizontal: 18,
    paddingVertical: 6,
    borderRadius: 20,
    marginTop: 10,
  },
  hintPillText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#1E40AF',
  },
  hintPillTextTablet: {
    fontSize: 16,
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
    gap: 8,
  },
  bubblesColumnTablet: {
    maxWidth: 720,
    gap: 16,
    alignSelf: 'center',
  },
  bubbleWrapperRegular: {
    width: '46%',
    maxWidth: 180,
    aspectRatio: 1,
  },
  bubbleWrapperRegularTablet: {
    width: '46%',
    maxWidth: 240,
    aspectRatio: 1,
  },
  bubbleWrapperPhrase: {
    width: '100%',
    maxWidth: 440,
    height: 64,
  },
  bubbleWrapperPhraseTablet: {
    width: '100%',
    maxWidth: 720,
    height: 84,
  },
  bubbleRegular: {
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
  bubbleRegularTablet: {
    borderRadius: 48,
    borderWidth: 4,
  },
  bubblePhrase: {
    width: '100%',
    height: '100%',
    borderRadius: 20,
    borderWidth: 3,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 6,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.12, shadowRadius: 6 },
      android: { elevation: 4 },
      web: { boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)' } as any,
    }),
  },
  bubblePhraseTablet: {
    width: '100%',
    height: '100%',
    borderRadius: 24,
    borderWidth: 3.5,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 24,
    paddingVertical: 8,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.15, shadowRadius: 8 },
      android: { elevation: 5 },
      web: { boxShadow: '0 6px 14px -2px rgba(0, 0, 0, 0.12)' } as any,
    }),
  },
  bubbleContentWrapper: {
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  bubbleText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 68,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextTablet: {
    fontSize: 82,
  },
  bubbleTextMedium: {
    fontSize: 48,
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextSmall: {
    fontSize: 36,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextExtraSmall: {
    fontSize: 28,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    includeFontPadding: false,
  },
  bubbleTextPhrase: {
    fontSize: 24,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    lineHeight: 34,
    includeFontPadding: false,
  },
  bubbleTextPhraseLong: {
    fontSize: 22,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    lineHeight: 32,
    includeFontPadding: false,
  },
  bubbleTextPhraseTablet: {
    fontSize: 32,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    lineHeight: 46,
    includeFontPadding: false,
  },
  bubbleTextPhraseLongTablet: {
    fontSize: 28,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    alignSelf: 'center',
    width: '100%',
    lineHeight: 42,
    includeFontPadding: false,
  },
  feedbackIcon: {
    position: 'absolute',
    top: 6,
    right: 8,
  },
  feedbackIconTablet: {
    top: 10,
    right: 14,
  },
});

