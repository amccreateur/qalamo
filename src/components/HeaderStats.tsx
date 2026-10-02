import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Platform } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../theme/colors';
import { soundService } from '../services/soundService';

interface HeaderStatsProps {
  coins: number;
  totalStars: number;
  avatarBase?: string;
  onAvatarPress?: () => void;
  onHomePress?: () => void;
  showHome?: boolean;
}

export const HeaderStats: React.FC<HeaderStatsProps> = ({
  coins,
  totalStars,
  avatarBase = 'lion',
  onAvatarPress,
  onHomePress,
  showHome = false,
}) => {
  const [isMuted, setIsMuted] = useState(soundService.getMuted());

  const toggleMute = () => {
    const next = !isMuted;
    setIsMuted(next);
    soundService.setMuted(next);
  };

  const getAvatarEmoji = (base: string) => {
    switch (base) {
      case 'lion': return '🦁';
      case 'falcon': return '🦅';
      case 'boy1': return '👦';
      case 'girl1': return '👧';
      case 'cat': return '🐱';
      default: return '🦁';
    }
  };

  return (
    <View style={styles.container}>
      {showHome ? (
        <TouchableOpacity style={styles.iconButton} onPress={onHomePress} activeOpacity={0.8}>
          <Ionicons name="arrow-back" size={24} color="#1E293B" />
        </TouchableOpacity>
      ) : (
        <TouchableOpacity style={styles.avatarButton} onPress={onAvatarPress} activeOpacity={0.8}>
          <Text style={styles.avatarEmoji}>{getAvatarEmoji(avatarBase)}</Text>
        </TouchableOpacity>
      )}

      <View style={styles.statsRow}>
        {/* Stars */}
        <View style={[styles.badge, styles.starBadge]}>
          <Ionicons name="star" size={18} color="#F59E0B" />
          <Text style={styles.badgeText}>{totalStars}</Text>
        </View>

        {/* Coins */}
        <View style={[styles.badge, styles.coinBadge]}>
          <Ionicons name="diamond" size={18} color="#06B6D4" />
          <Text style={styles.badgeText}>{coins}</Text>
        </View>

        {/* Audio Mute / Unmute */}
        <TouchableOpacity style={styles.soundButton} onPress={toggleMute} activeOpacity={0.8}>
          <Ionicons
            name={isMuted ? 'volume-mute' : 'volume-high'}
            size={22}
            color={isMuted ? '#EF4444' : '#3B82F6'}
          />
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 10,
    backgroundColor: 'rgba(255, 255, 255, 0.92)',
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(226, 232, 240, 0.8)',
    zIndex: 10,
  },
  avatarButton: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: '#EEF2FF',
    borderWidth: 2,
    borderColor: '#818CF8',
    justifyContent: 'center',
    alignItems: 'center',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1, shadowRadius: 3 },
      android: { elevation: 3 },
      web: { boxShadow: '0 2px 4px rgba(0,0,0,0.1)' } as any,
    }),
  },
  avatarEmoji: {
    fontSize: 24,
  },
  iconButton: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: '#F1F5F9',
    justifyContent: 'center',
    alignItems: 'center',
  },
  statsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  badge: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
    gap: 6,
  },
  starBadge: {
    backgroundColor: '#FEF3C7',
    borderWidth: 1.5,
    borderColor: '#FDE68A',
  },
  coinBadge: {
    backgroundColor: '#CFFAFE',
    borderWidth: 1.5,
    borderColor: '#A5F3FC',
  },
  badgeText: {
    fontSize: 15,
    fontWeight: '800',
    color: '#1E293B',
  },
  soundButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
});

