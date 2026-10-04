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

interface TargetGameProps {
  items: PhonemeItem[];
  onComplete: (stars: number, coins: number, score: number, mistakes: string[]) => void;
  onExit: () => void;
}

interface TargetOption {
  id: string;
  grapheme: string;
  isCorrect: boolean;
  colorIdx: number;
}

export const TargetGame: React.FC<TargetGameProps> = ({ items, onComplete, onExit }) => {
  const { language, t } = useLanguage();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [options, setOptions] = useState<TargetOption[]>([]);
  const [score, setScore] = useState(0);
  const [mistakes, setMistakes] = useState<string[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [isSuccess, setIsSuccess] = useState<boolean | null>(null);

  const bounceAnim = useRef(new Animated.Value(0.95)).current;
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
    if (!currentItem) return;

    const allChoices: TargetOption[] = [
      { id: 'correct', grapheme: currentItem.grapheme, isCorrect: true, colorIdx: 0 },
      ...currentItem.distractors.map((d, idx) => ({
        id: `dist_${idx}`,
        grapheme: d,
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
    setSelectedId(null);
    setIsSuccess(null);

    const timer = setTimeout(() => {
      playSound();
    }, 350);

    return () => clearTimeout(timer);
  }, [currentIndex]);

  const playSound = () => {
    if (!currentItem) return;
    soundService.playSound(currentItem.id, currentItem.audioText || currentItem.grapheme);

    Animated.sequence([
      Animated.timing(bounceAnim, { toValue: 1.15, duration: 150, useNativeDriver: true }),
      Animated.timing(bounceAnim, { toValue: 1, duration: 150, useNativeDriver: true }),
    ]).start();
  };

  const handleSelect = (option: TargetOption) => {
    if (selectedId !== null) return;
    setSelectedId(option.id);

    if (option.isCorrect) {
      setIsSuccess(true);
      soundService.triggerSuccess();
      setScore((s) => s + 1);

      setTimeout(() => {
        if (currentIndex + 1 < items.length) {
          setCurrentIndex((i) => i + 1);
        } else {
          const finalScore = score + 1;
          const stars = finalScore === items.length ? 3 : finalScore >= items.length * 0.7 ? 2 : 1;
          const coins = stars * 10 + 5;
          onComplete(stars, coins, finalScore, mistakes);
        }
      }, 900);
    } else {
      setIsSuccess(false);
      soundService.triggerError();
      setMistakes((m) => [...m, currentItem.grapheme]);

      setTimeout(() => {
        soundService.playSound(undefined, option.grapheme);
      }, 300);

      setTimeout(() => {
        setSelectedId(null);
        setIsSuccess(null);
      }, 1200);
    }
  };

  if (!currentItem) return null;

  const progressPercent = ((currentIndex + 1) / items.length) * 100;

  return (
    <LinearGradient colors={['#1E1B4B', '#312E81', '#4338CA']} style={styles.container}>
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

      {/* Target Center Stage */}
      <View style={styles.targetStage}>
        <Text style={styles.stageTitle}>
          {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
          currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
          currentItem.phonemeDesc?.toLowerCase().includes('fin')
            ? t.targetStageTitlePosition
            : t.targetStageTitleSound}
        </Text>
        <Text style={styles.stageSubtitle}>
          {currentItem.phonemeDesc?.toLowerCase().includes('début') ||
          currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
          currentItem.phonemeDesc?.toLowerCase().includes('fin')
            ? `${t.targetStageSubtitlePosition} ${getLocalizedPhonemeDesc(currentItem.phonemeDesc)}`
            : t.targetStageSubtitleSound}
        </Text>

        <TouchableOpacity style={styles.targetOrb} onPress={playSound} activeOpacity={0.8}>
          <Animated.View style={[styles.targetInner, { transform: [{ scale: bounceAnim }] }]}>
            <LinearGradient colors={['#F59E0B', '#EF4444']} style={styles.orbGradient}>
              <Ionicons name="volume-high" size={48} color="#FFFFFF" />
              <Text style={styles.tapListenText}>{t.targetReplay}</Text>
            </LinearGradient>
          </Animated.View>
        </TouchableOpacity>

        {(currentItem.phonemeDesc?.toLowerCase().includes('début') ||
          currentItem.phonemeDesc?.toLowerCase().includes('milieu') ||
          currentItem.phonemeDesc?.toLowerCase().includes('fin')) && (
          <View style={styles.targetHintBadge}>
            <Ionicons name="locate" size={16} color="#FEF08A" />
            <Text style={styles.targetHintText}>{getLocalizedPhonemeDesc(currentItem.phonemeDesc)}</Text>
          </View>
        )}
      </View>

      {/* Target Choices Cards */}
      <View style={[styles.cardsRow, isPhraseLevel && styles.cardsColumn]}>
        {options.map((opt) => {
          const isSelected = selectedId === opt.id;
          const colorTheme = COLORS.bubbleColors[opt.colorIdx] || COLORS.bubbleColors[0];
          let cardBg = colorTheme.bg;
          let borderColor = colorTheme.border;
          let textColor = colorTheme.text;

          if (isSelected) {
            cardBg = isSuccess ? '#D1FAE5' : '#FEE2E2';
            borderColor = isSuccess ? '#10B981' : '#EF4444';
            textColor = isSuccess ? '#065F46' : '#991B1B';
          }

          return (
            <TouchableOpacity
              key={opt.id}
              style={[
                styles.targetCard,
                { backgroundColor: cardBg, borderColor: borderColor },
                isPhraseLevel ? styles.targetCardPhrase : null,
              ]}
              onPress={() => handleSelect(opt)}
              activeOpacity={0.7}
            >
              <Text
                style={[
                  styles.cardArabicText,
                  { color: textColor },
                  opt.grapheme.length > 16
                    ? styles.cardArabicTextExtraSmall
                    : opt.grapheme.length > 8
                    ? styles.cardArabicTextSmall
                    : opt.grapheme.length > 4
                    ? styles.cardArabicTextMedium
                    : null,
                ]}
                numberOfLines={2}
                adjustsFontSizeToFit
              >
                {opt.grapheme}
              </Text>

              {isSelected && (
                <View style={styles.cardBadge}>
                  <Ionicons
                    name={isSuccess ? 'checkmark-circle' : 'close-circle'}
                    size={28}
                    color={isSuccess ? '#10B981' : '#EF4444'}
                  />
                </View>
              )}
            </TouchableOpacity>
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
    backgroundColor: '#F59E0B',
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
  targetStage: {
    alignItems: 'center',
    marginVertical: 6,
  },
  stageTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: '#FCD34D',
    marginBottom: 4,
  },
  stageSubtitle: {
    fontSize: 15,
    fontWeight: '600',
    color: '#E0E7FF',
    marginBottom: 14,
  },
  targetOrb: {
    marginVertical: 4,
  },
  targetInner: {
    width: 110,
    height: 110,
    borderRadius: 55,
    ...Platform.select({
      ios: { shadowColor: '#F59E0B', shadowOffset: { width: 0, height: 8 }, shadowOpacity: 0.5, shadowRadius: 15 },
      android: { elevation: 10 },
      web: { boxShadow: '0 0 25px rgba(245, 158, 11, 0.6)' } as any,
    }),
  },
  orbGradient: {
    width: '100%',
    height: '100%',
    borderRadius: 55,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 4,
    borderColor: '#FEF3C7',
  },
  tapListenText: {
    fontSize: 12,
    fontWeight: '800',
    color: '#FFFFFF',
    marginTop: 2,
  },
  phonemeDesc: {
    marginTop: 12,
    fontSize: 16,
    fontWeight: '700',
    color: '#C7D2FE',
  },
  targetHintBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(255, 255, 255, 0.15)',
    borderWidth: 1.5,
    borderColor: 'rgba(254, 240, 138, 0.4)',
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 20,
    marginTop: 10,
  },
  targetHintText: {
    fontSize: 15,
    fontWeight: '800',
    color: '#FEF08A',
  },
  cardsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 12,
    paddingBottom: 10,
  },
  cardsColumn: {
    flexDirection: 'column',
    alignItems: 'center',
    flexWrap: 'nowrap',
    width: '100%',
    gap: 10,
  },
  targetCard: {
    width: (width - 44) / 2,
    maxWidth: 180,
    aspectRatio: 1,
    borderRadius: 36,
    borderWidth: 3.5,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 6,
    paddingVertical: 6,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 6 }, shadowOpacity: 0.15, shadowRadius: 8 },
      android: { elevation: 6 },
      web: { boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.15)' } as any,
    }),
  },
  targetCardPhrase: {
    width: '100%',
    maxWidth: 420,
    aspectRatio: undefined,
    minHeight: 68,
    borderRadius: 22,
    paddingHorizontal: 16,
    paddingVertical: 10,
  },
  cardArabicText: {
    fontFamily: 'Amiri-Bold',
    fontSize: 58,
    fontWeight: '700',
    textAlign: 'center',
    textAlignVertical: 'center',
    includeFontPadding: false,
  },
  cardArabicTextMedium: {
    fontSize: 40,
    textAlignVertical: 'center',
    includeFontPadding: false,
  },
  cardArabicTextSmall: {
    fontSize: 30,
    fontWeight: '700',
    textAlignVertical: 'center',
    includeFontPadding: false,
  },
  cardArabicTextExtraSmall: {
    fontSize: 24,
    fontWeight: '700',
    textAlignVertical: 'center',
    includeFontPadding: false,
  },
  cardBadge: {
    position: 'absolute',
    top: 6,
    right: 8,
  },
});

