import React, { createContext, useContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as Localization from 'expo-localization';
import { Language, TRANSLATIONS, Translations } from './translations';

const LANGUAGE_STORAGE_KEY = '@qalamo_language_v1';

export const getSystemDefaultLanguage = (): Language => {
  try {
    const locales = Localization.getLocales();
    if (locales && locales.length > 0) {
      const code = locales[0].languageCode?.toLowerCase();
      if (code) {
        if (code.startsWith('fr')) return 'fr';
        // For English or any other language, default directly to English
        return 'en';
      }
    }
  } catch (e) {
    console.warn('Localization getLocales error:', e);
  }

  try {
    const intlLang = Intl.DateTimeFormat().resolvedOptions().locale?.toLowerCase();
    if (intlLang?.startsWith('fr')) return 'fr';
    return 'en';
  } catch {}

  return 'en';
};

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => Promise<void>;
  toggleLanguage: () => Promise<void>;
  t: Translations;
}

const initialDefaultLang = getSystemDefaultLanguage();

const LanguageContext = createContext<LanguageContextType>({
  language: initialDefaultLang,
  setLanguage: async () => {},
  toggleLanguage: async () => {},
  t: TRANSLATIONS[initialDefaultLang],
});

export const LanguageProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>(initialDefaultLang);

  useEffect(() => {
    loadSavedLanguage();
  }, []);

  const loadSavedLanguage = async () => {
    try {
      const saved = await AsyncStorage.getItem(LANGUAGE_STORAGE_KEY);
      if (saved === 'en' || saved === 'fr') {
        setLanguageState(saved);
      } else {
        // First run: detect from system language and save
        const sysLang = getSystemDefaultLanguage();
        setLanguageState(sysLang);
        await AsyncStorage.setItem(LANGUAGE_STORAGE_KEY, sysLang);
      }
    } catch (e) {
      console.warn('Failed to load language setting:', e);
    }
  };

  const setLanguage = async (newLang: Language) => {
    try {
      setLanguageState(newLang);
      await AsyncStorage.setItem(LANGUAGE_STORAGE_KEY, newLang);
    } catch (e) {
      console.warn('Failed to save language setting:', e);
    }
  };

  const toggleLanguage = async () => {
    const nextLang: Language = language === 'fr' ? 'en' : 'fr';
    await setLanguage(nextLang);
  };

  return (
    <LanguageContext.Provider
      value={{
        language,
        setLanguage,
        toggleLanguage,
        t: TRANSLATIONS[language],
      }}
    >
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
