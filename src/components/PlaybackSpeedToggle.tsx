import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Platform, ViewStyle, StyleProp } from 'react-native';
import * as Haptics from 'expo-haptics';
import { soundService } from '../services/soundService';

interface PlaybackSpeedToggleProps {
  currentSpeed: number;
  onSpeedChange: (speed: number) => void;
  style?: StyleProp<ViewStyle>;
  variant?: 'green' | 'amber' | 'blue' | 'glass';
}

export const PlaybackSpeedToggle: React.FC<PlaybackSpeedToggleProps> = ({
  currentSpeed,
  onSpeedChange,
  style,
  variant = 'glass',
}) => {
  const speeds = [
    { value: 1.0, label: '1.0x' },
    { value: 0.8, label: '0.8x 🐢' },
  ];

  const handleSelect = (speed: number) => {
    if (Platform.OS !== 'web') {
      try {
        Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
      } catch (_) {}
    }
    soundService.setPlaybackSpeed(speed);
    onSpeedChange(speed);
  };

  const getActiveColors = () => {
    switch (variant) {
      case 'green':
        return { bg: '#FFFFFF', text: '#065F46' };
      case 'amber':
        return { bg: '#FEF3C7', text: '#92400E' };
      case 'blue':
        return { bg: '#FFFFFF', text: '#1D4ED8' };
      case 'glass':
      default:
        return { bg: '#FFFFFF', text: '#1E293B' };
    }
  };

  const activeColor = getActiveColors();

  return (
    <View style={[styles.container, style]}>
      {speeds.map((s) => {
        const isActive = Math.abs(currentSpeed - s.value) < 0.05;

        return (
          <TouchableOpacity
            key={`speed_${s.value}`}
            style={[
              styles.speedButton,
              isActive && [styles.speedButtonActive, { backgroundColor: activeColor.bg }],
            ]}
            onPress={() => handleSelect(s.value)}
            activeOpacity={0.7}
          >
            <Text
              style={[
                styles.speedText,
                isActive ? [styles.speedTextActive, { color: activeColor.text }] : styles.speedTextInactive,
              ]}
              allowFontScaling={false}
            >
              {s.label}
            </Text>
          </TouchableOpacity>
        );
      })}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.25)',
    borderRadius: 20,
    padding: 3,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
    alignSelf: 'center',
  },
  speedButton: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    justifyContent: 'center',
    alignItems: 'center',
  },
  speedButtonActive: {
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.15,
        shadowRadius: 3,
      },
      android: {
        elevation: 3,
      },
      web: {
        boxShadow: '0 2px 4px rgba(0, 0, 0, 0.15)',
      } as any,
    }),
  },
  speedText: {
    fontSize: 13,
    fontWeight: '800',
  },
  speedTextActive: {
    fontWeight: '900',
  },
  speedTextInactive: {
    color: 'rgba(255, 255, 255, 0.85)',
  },
});
