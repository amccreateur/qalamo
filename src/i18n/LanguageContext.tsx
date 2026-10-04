import React, { createContext, useContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Language, TRANSLATIONS, Translations } from './translations';

const LANGUAGE_STORAGE_KEY = '@qalamo_language_v1';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => Promise<void>;
  toggleLanguage: () => Promise<void>;
  t: Translations;
}

const LanguageContext = createContext<LanguageContextType>({
  language: 'fr',
  setLanguage: async () => {},
  toggleLanguage: async () => {},
  t: TRANSLATIONS.fr,
});

export const LanguageProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>('fr');

  useEffect(() => {
    loadSavedLanguage();
  }, []);

  const loadSavedLanguage = async () => {
    try {
      const saved = await AsyncStorage.getItem(LANGUAGE_STORAGE_KEY);
      if (saved === 'en' || saved === 'fr') {
        setLanguageState(saved);
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
