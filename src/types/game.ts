export type GameMode = 'bubble' | 'target' | 'wordBuilder' | 'explorer';

export interface PhonemeItem {
  id: string;
  grapheme: string; // ex: 'بَ' ou 'ب'
  audioText: string; // texte prononcé par TTS ou audio
  phonemeDesc: string; // ex: 'Ba avec Fatha'
  transliteration: string; // ex: 'ba'
  distractors: string[]; // ex: ['تَ', 'دَ', 'نَ']
  forms?: {
    isolated: string;
    initial: string;
    medial: string;
    final: string;
  };
}

export interface WordItem {
  id: string;
  word: string; // ex: 'كَتَبَ'
  meaning: string; // ex: 'Il a écrit'
  translationFr: string;
  letters: string[]; // ['كَ', 'تَ', 'بَ']
  distractorLetters: string[]; // ['سَ', 'رَ']
  emoji?: string; // ex: '✍️'
}

export interface Level {
  id: number;
  worldId: number;
  title: string;
  titleAr: string;
  description: string;
  gameType: GameMode;
  items: PhonemeItem[];
  wordItems?: WordItem[];
  requiredStars: number;
  bgColor: [string, string];
}

export interface World {
  id: number;
  name: string;
  nameAr: string;
  description: string;
  icon: string;
  color: string;
  levels: Level[];
}

export interface UserProgress {
  unlockedLevelId: number;
  starsByLevel: Record<number, number>; // levelId -> stars (0-3)
  coins: number;
  xp: number;
  avatar: {
    base: string; // 'boy1', 'girl1', 'lion', 'falcon'
    color: string;
    accessory: string; // 'cap', 'crown', 'glasses', 'none'
  };
  ownedAccessories: string[];
  mistakeHistory: Record<string, number>; // grapheme -> count of errors (for adaptive review)
}

