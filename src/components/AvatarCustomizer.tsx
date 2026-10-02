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
import { UserProgress } from '../types/game';
import { storageService } from '../services/storageService';
import { soundService } from '../services/soundService';

interface AvatarCustomizerProps {
  progress: UserProgress;
  onUpdate: (newProgress: UserProgress) => void;
  onBack: () => void;
}

const AVATARS = [
  { id: 'lion', name: 'Lionceau Courageux', emoji: '🦁' },
  { id: 'falcon', name: 'Faucon Rapide', emoji: '🦅' },
  { id: 'boy1', name: 'Petit Explorateur', emoji: '👦' },
  { id: 'girl1', name: 'Petite Aventurière', emoji: '👧' },
  { id: 'cat', name: 'Chat Curieux', emoji: '🐱' },
];

const ACCESSORIES = [
  { id: 'cap', name: 'Casquette Cool', emoji: '🧢', price: 0 },
  { id: 'crown', name: 'Couronne Royale', emoji: '👑', price: 30 },
  { id: 'glasses', name: 'Lunettes Savantes', emoji: '👓', price: 20 },
  { id: 'star_hat', name: 'Chapeau d\'Étoiles', emoji: '🎩', price: 40 },
  { id: 'medal', name: 'Médaille d\'Or', emoji: '🏅', price: 50 },
];

export const AvatarCustomizer: React.FC<AvatarCustomizerProps> = ({ progress, onUpdate, onBack }) => {
  const [selectedBase, setSelectedBase] = useState(progress.avatar.base);
  const [selectedAcc, setSelectedAcc] = useState(progress.avatar.accessory);

  const handleSelectAvatar = async (baseId: string) => {
    soundService.triggerPop();
    setSelectedBase(baseId);
    const updated: UserProgress = {
      ...progress,
      avatar: { ...progress.avatar, base: baseId },
    };
    await storageService.saveProgress(updated);
    onUpdate(updated);
  };

  const handleSelectAccessory = async (acc: typeof ACCESSORIES[0]) => {
    const isOwned = progress.ownedAccessories.includes(acc.id) || acc.price === 0;

    if (isOwned) {
      soundService.triggerPop();
      setSelectedAcc(acc.id);
      const updated: UserProgress = {
        ...progress,
        avatar: { ...progress.avatar, accessory: acc.id },
      };
      await storageService.saveProgress(updated);
      onUpdate(updated);
    } else {
      // Need to buy
      if (progress.coins >= acc.price) {
        soundService.triggerVictory();
        const updated: UserProgress = {
          ...progress,
          coins: progress.coins - acc.price,
          ownedAccessories: [...progress.ownedAccessories, acc.id],
          avatar: { ...progress.avatar, accessory: acc.id },
        };
        setSelectedAcc(acc.id);
        await storageService.saveProgress(updated);
        onUpdate(updated);
      } else {
        soundService.triggerError();
      }
    }
  };

  const currentAvatarEmoji = AVATARS.find((a) => a.id === selectedBase)?.emoji || '🦁';
  const currentAccEmoji = ACCESSORIES.find((a) => a.id === selectedAcc)?.emoji || '';

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backBtn} onPress={onBack} activeOpacity={0.8}>
          <Ionicons name="arrow-back" size={24} color="#0F172A" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Mon Avatar & Boutique</Text>
        <View style={styles.coinPill}>
          <Ionicons name="diamond" size={16} color="#06B6D4" />
          <Text style={styles.coinPillText}>{progress.coins}</Text>
        </View>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Avatar Preview Showcase */}
        <View style={styles.previewCard}>
          <View style={styles.avatarCircle}>
            <Text style={styles.largeEmoji}>{currentAvatarEmoji}</Text>
            {currentAccEmoji ? <Text style={styles.accessoryEmoji}>{currentAccEmoji}</Text> : null}
          </View>
          <Text style={styles.avatarTitle}>Personnage de lecture</Text>
        </View>

        {/* Section 1: Choose Base Character */}
        <Text style={styles.sectionTitle}>1. Choisis ton personnage :</Text>
        <View style={styles.grid}>
          {AVATARS.map((av) => {
            const isSelected = selectedBase === av.id;
            return (
              <TouchableOpacity
                key={av.id}
                style={[styles.itemCard, isSelected && styles.itemCardSelected]}
                onPress={() => handleSelectAvatar(av.id)}
                activeOpacity={0.7}
              >
                <Text style={styles.itemEmoji}>{av.emoji}</Text>
                <Text style={styles.itemName}>{av.name}</Text>
              </TouchableOpacity>
            );
          })}
        </View>

        {/* Section 2: Choose Accessories */}
        <Text style={[styles.sectionTitle, { marginTop: 24 }]}>2. Accessoires & Trophées :</Text>
        <View style={styles.grid}>
          {ACCESSORIES.map((acc) => {
            const isOwned = progress.ownedAccessories.includes(acc.id) || acc.price === 0;
            const isSelected = selectedAcc === acc.id;

            return (
              <TouchableOpacity
                key={acc.id}
                style={[styles.itemCard, isSelected && styles.itemCardSelected]}
                onPress={() => handleSelectAccessory(acc)}
                activeOpacity={0.7}
              >
                <Text style={styles.itemEmoji}>{acc.emoji}</Text>
                <Text style={styles.itemName}>{acc.name}</Text>

                {isOwned ? (
                  <View style={styles.ownedBadge}>
                    <Text style={styles.ownedText}>{isSelected ? 'Équipé' : 'Possédé'}</Text>
                  </View>
                ) : (
                  <View style={styles.priceBadge}>
                    <Ionicons name="diamond" size={12} color="#06B6D4" />
                    <Text style={styles.priceText}>{acc.price}</Text>
                  </View>
                )}
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
  headerTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
  },
  coinPill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#CFFAFE',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
  },
  coinPillText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0891B2',
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  previewCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 28,
    padding: 24,
    alignItems: 'center',
    marginBottom: 24,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.08, shadowRadius: 8 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.05)' } as any,
    }),
  },
  avatarCircle: {
    width: 110,
    height: 110,
    borderRadius: 55,
    backgroundColor: '#EEF2FF',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 4,
    borderColor: '#818CF8',
    marginBottom: 12,
  },
  largeEmoji: {
    fontSize: 60,
  },
  accessoryEmoji: {
    position: 'absolute',
    top: -10,
    right: -4,
    fontSize: 32,
  },
  avatarTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
    marginBottom: 12,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    justifyContent: 'space-between',
  },
  itemCard: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: 20,
    padding: 16,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#E2E8F0',
  },
  itemCardSelected: {
    borderColor: '#3B82F6',
    backgroundColor: '#EFF6FF',
  },
  itemEmoji: {
    fontSize: 40,
    marginBottom: 8,
  },
  itemName: {
    fontSize: 13,
    fontWeight: '700',
    color: '#334155',
    textAlign: 'center',
    marginBottom: 8,
  },
  ownedBadge: {
    backgroundColor: '#DCFCE7',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  ownedText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#15803D',
  },
  priceBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#ECFEFF',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  priceText: {
    fontSize: 12,
    fontWeight: '800',
    color: '#0891B2',
  },
});

