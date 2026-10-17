import AsyncStorage from '@react-native-async-storage/async-storage';
import { UserProgress } from '../types/game';

const STORAGE_KEY = '@graphogame_arabic_progress_v1';

export const INITIAL_PROGRESS: UserProgress = {
  unlockedLevelId: 999,
  starsByLevel: {},
  validatedLevels: {},
  coins: 100,
  xp: 0,
  avatar: {
    base: 'lion',
    color: '#3B82F6',
    accessory: 'cap',
  },
  ownedAccessories: ['cap'],
  mistakeHistory: {},
};

export const storageService = {
  async getProgress(): Promise<UserProgress> {
    try {
      const data = await AsyncStorage.getItem(STORAGE_KEY);
      if (data) {
        const parsed = JSON.parse(data);
        const validatedLevels = parsed.validatedLevels || {};
        // Backward compatibility: migrate if stars exist but validatedLevels is not initialized
        if (Object.keys(validatedLevels).length === 0 && parsed.starsByLevel) {
          Object.keys(parsed.starsByLevel).forEach((lvlId) => {
            if (parsed.starsByLevel[Number(lvlId)] > 0) {
              validatedLevels[Number(lvlId)] = true;
            }
          });
        }
        return {
          ...INITIAL_PROGRESS,
          ...parsed,
          validatedLevels,
        };
      }
    } catch (e) {
      console.warn('Failed to load user progress:', e);
    }
    return INITIAL_PROGRESS;
  },

  async saveProgress(progress: UserProgress): Promise<void> {
    try {
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    } catch (e) {
      console.warn('Failed to save user progress:', e);
    }
  },

  async validateLevel(levelId: number, earnedStars: number, earnedCoins: number, mistakes: string[]): Promise<UserProgress> {
    const current = await this.getProgress();
    const oldStars = current.starsByLevel[levelId] || 0;
    const newStars = Math.max(oldStars, earnedStars);

    // Update mistakes history for adaptive learning
    const updatedMistakes = { ...current.mistakeHistory };
    mistakes.forEach((m) => {
      updatedMistakes[m] = (updatedMistakes[m] || 0) + 1;
    });

    const nextLevelId = Math.max(current.unlockedLevelId, levelId + 1);

    const updated: UserProgress = {
      ...current,
      unlockedLevelId: nextLevelId,
      starsByLevel: {
        ...current.starsByLevel,
        [levelId]: newStars,
      },
      validatedLevels: {
        ...(current.validatedLevels || {}),
        [levelId]: true,
      },
      coins: current.coins + earnedCoins,
      xp: current.xp + earnedStars * 50 + 20,
      mistakeHistory: updatedMistakes,
    };

    await this.saveProgress(updated);
    return updated;
  },

  async unvalidateLevel(levelId: number): Promise<UserProgress> {
    const current = await this.getProgress();
    const updatedValidated = { ...(current.validatedLevels || {}) };
    delete updatedValidated[levelId];
    const updatedStars = { ...current.starsByLevel };
    delete updatedStars[levelId];
    const updated: UserProgress = {
      ...current,
      validatedLevels: updatedValidated,
      starsByLevel: updatedStars,
    };
    await this.saveProgress(updated);
    return updated;
  },

  async completeLevel(levelId: number, earnedStars: number, earnedCoins: number, mistakes: string[]): Promise<UserProgress> {
    return this.validateLevel(levelId, earnedStars, earnedCoins, mistakes);
  },

  async resetProgress(): Promise<UserProgress> {
    await AsyncStorage.removeItem(STORAGE_KEY);
    return INITIAL_PROGRESS;
  },

  async getPlaybackSpeed(): Promise<number> {
    try {
      const data = await AsyncStorage.getItem('@qalamo_playback_speed');
      if (data) {
        const parsed = parseFloat(data);
        if (!isNaN(parsed) && parsed > 0) return parsed;
      }
    } catch (_) {}
    return 1.0;
  },

  async setPlaybackSpeed(speed: number): Promise<void> {
    try {
      await AsyncStorage.setItem('@qalamo_playback_speed', speed.toString());
    } catch (_) {}
  }
};

