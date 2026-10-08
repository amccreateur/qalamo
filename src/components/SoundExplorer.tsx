import React, { useState } from 'react';
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
import { soundService } from '../services/soundService';
import { useLanguage } from '../i18n/LanguageContext';

interface SoundExplorerProps {
  onBack: () => void;
}

const ARABIC_LETTERS = [
  { id: 'alif', char: 'أ', name: 'Alif', translit: 'a' },
  { id: 'ba', char: 'ب', name: 'Baa', translit: 'b' },
  { id: 'ta', char: 'ت', name: 'Taa', translit: 't' },
  { id: 'tha', char: 'ث', name: 'Thaa', translit: 'th' },
  { id: 'jeem', char: 'ج', name: 'Jeem', translit: 'j' },
  { id: 'hha', char: 'ح', name: 'Hhaa', translit: 'ḥ' },
  { id: 'kha', char: 'خ', name: 'Khaa', translit: 'kh' },
  { id: 'dal', char: 'د', name: 'Daal', translit: 'd' },
  { id: 'dhal', char: 'ذ', name: 'Dhaal', translit: 'dh' },
  { id: 'ra', char: 'ر', name: 'Raa', translit: 'r' },
  { id: 'zay', char: 'ز', name: 'Zay', translit: 'z' },
  { id: 'seen', char: 'س', name: 'Seen', translit: 's' },
  { id: 'sheen', char: 'ش', name: 'Sheen', translit: 'sh' },
  { id: 'sad', char: 'ص', name: 'Saad', translit: 'ṣ' },
  { id: 'dad', char: 'ض', name: 'Daad', translit: 'ḍ' },
  { id: 'ttaa', char: 'ط', name: 'Taa', translit: 'ṭ' },
  { id: 'zha', char: 'ظ', name: 'Zhaa', translit: 'ẓ' },
  { id: 'ayn', char: 'ع', name: '\'Ayn', translit: 'ʿ' },
  { id: 'ghayn', char: 'غ', name: 'Ghayn', translit: 'gh' },
  { id: 'fa', char: 'ف', name: 'Faa', translit: 'f' },
  { id: 'qaf', char: 'ق', name: 'Qaaf', translit: 'q' },
  { id: 'kaf', char: 'ك', name: 'Kaaf', translit: 'k' },
  { id: 'lam', char: 'ل', name: 'Laam', translit: 'l' },
  { id: 'meem', char: 'م', name: 'Meem', translit: 'm' },
  { id: 'noon', char: 'ن', name: 'Noon', translit: 'n' },
  { id: 'haa', char: 'هـ', name: 'Haa', translit: 'h' },
  { id: 'waw', char: 'و', name: 'Waaw', translit: 'w' },
  { id: 'yaa', char: 'ي', name: 'Yaa', translit: 'y' },
];

type VowelMode = 'raw' | 'fatha' | 'damma' | 'kasra' | 'sukun';

export const SoundExplorer: React.FC<SoundExplorerProps> = ({ onBack }) => {
  const { t } = useLanguage();
  const [selectedVowel, setSelectedVowel] = useState<VowelMode>('raw');
  const [activeLetter, setActiveLetter] = useState<string | null>(null);

  const getVocalizedChar = (rawChar: string, mode: VowelMode) => {
    if (mode === 'raw') return rawChar;
    if (mode === 'fatha') return `${rawChar}َ`;
    if (mode === 'damma') return `${rawChar}ُ`;
    if (mode === 'kasra') return `${rawChar}ِ`;
    if (mode === 'sukun') return `${rawChar}ْ`;
    return rawChar;
  };

  const handlePlayLetter = (item: typeof ARABIC_LETTERS[0]) => {
    const vocalized = getVocalizedChar(item.char, selectedVowel);
    setActiveLetter(item.char);
    soundService.triggerPop();

    if (selectedVowel === 'raw') {
      soundService.playSound(item.id, vocalized);
    } else {
      soundService.speakArabic(vocalized);
    }

    setTimeout(() => {
      setActiveLetter(null);
    }, 600);
  };

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backBtn} onPress={onBack} activeOpacity={0.8}>
          <Ionicons name="arrow-back" size={24} color="#0F172A" />
        </TouchableOpacity>
        <View style={styles.headerTitleContainer}>
          <Text style={styles.headerTitle}>{t.soundExplorerTitle}</Text>
          <Text style={styles.headerTitleAr}>{t.soundExplorerTitleAr}</Text>
        </View>
        <View style={{ width: 44 }} />
      </View>

      {/* Harakat Filter Tabs */}
      <View style={styles.vowelFilters}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.vowelScroll}>
          <TouchableOpacity
            style={[styles.vowelTab, selectedVowel === 'raw' && styles.vowelTabActive]}
            onPress={() => setSelectedVowel('raw')}
          >
            <Text style={[styles.vowelTabText, selectedVowel === 'raw' && styles.vowelTabTextActive]}>
              {t.tabRawLetters}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.vowelTab, selectedVowel === 'fatha' && styles.vowelTabActive]}
            onPress={() => setSelectedVowel('fatha')}
          >
            <Text style={[styles.vowelTabText, selectedVowel === 'fatha' && styles.vowelTabTextActive]}>
              {t.tabFatha}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.vowelTab, selectedVowel === 'damma' && styles.vowelTabActive]}
            onPress={() => setSelectedVowel('damma')}
          >
            <Text style={[styles.vowelTabText, selectedVowel === 'damma' && styles.vowelTabTextActive]}>
              {t.tabDamma}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.vowelTab, selectedVowel === 'kasra' && styles.vowelTabActive]}
            onPress={() => setSelectedVowel('kasra')}
          >
            <Text style={[styles.vowelTabText, selectedVowel === 'kasra' && styles.vowelTabTextActive]}>
              {t.tabKasra}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.vowelTab, selectedVowel === 'sukun' && styles.vowelTabActive]}
            onPress={() => setSelectedVowel('sukun')}
          >
            <Text style={[styles.vowelTabText, selectedVowel === 'sukun' && styles.vowelTabTextActive]}>
              {t.tabSukun}
            </Text>
          </TouchableOpacity>
        </ScrollView>
      </View>

      {/* Letters Grid */}
      <ScrollView contentContainerStyle={styles.gridContainer}>
        <View style={styles.grid}>
          {ARABIC_LETTERS.map((item) => {
            const vocalized = getVocalizedChar(item.char, selectedVowel);
            const isActive = activeLetter === item.char;

            return (
              <TouchableOpacity
                key={item.char}
                style={[
                  styles.letterCard,
                  isActive && styles.letterCardActive,
                ]}
                onPress={() => handlePlayLetter(item)}
                activeOpacity={0.7}
              >
                <Text style={styles.cardChar}>{vocalized}</Text>
                <Text style={styles.cardName}>{item.name}</Text>
                <View style={styles.speakerMini}>
                  <Ionicons name="volume-medium" size={14} color="#64748B" />
                </View>
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: Platform.OS === 'ios' ? 50 : 20,
    paddingBottom: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  backBtn: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: '#F1F5F9',
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerTitleContainer: {
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
  },
  headerTitleAr: {
    fontSize: 15,
    fontWeight: '700',
    color: '#3B82F6',
  },
  vowelFilters: {
    backgroundColor: '#FFFFFF',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  vowelScroll: {
    paddingHorizontal: 16,
    gap: 8,
  },
  vowelTab: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    backgroundColor: '#F1F5F9',
  },
  vowelTabActive: {
    backgroundColor: '#3B82F6',
  },
  vowelTabText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#475569',
  },
  vowelTabTextActive: {
    color: '#FFFFFF',
  },
  gridContainer: {
    padding: 16,
    paddingBottom: 40,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: 12,
  },
  letterCard: {
    width: '30%',
    aspectRatio: 1,
    backgroundColor: '#FFFFFF',
    borderRadius: 22,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#E2E8F0',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.06, shadowRadius: 4 },
      android: { elevation: 2 },
      web: { boxShadow: '0 2px 4px rgba(0,0,0,0.05)' } as any,
    }),
  },
  letterCardActive: {
    borderColor: '#3B82F6',
    backgroundColor: '#EFF6FF',
    transform: [{ scale: 1.05 }],
  },
  cardChar: {
    fontFamily: 'Amiri-Bold',
    fontSize: 50,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 2,
    includeFontPadding: true,
  },
  cardName: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
  },
  speakerMini: {
    position: 'absolute',
    top: 8,
    right: 8,
  },
});

