import React, { useEffect, useRef } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, Animated, Platform } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../theme/colors';
import { soundService } from '../services/soundService';

interface VictoryModalProps {
  visible: boolean;
  stars: number;
  earnedCoins: number;
  score: number;
  totalQuestions: number;
  onReplay: () => void;
  onNext: () => void;
  onHome: () => void;
}

export const VictoryModal: React.FC<VictoryModalProps> = ({
  visible,
  stars,
  earnedCoins,
  score,
  totalQuestions,
  onReplay,
  onNext,
  onHome,
}) => {
  const scaleAnim = useRef(new Animated.Value(0.3)).current;
  const starScale1 = useRef(new Animated.Value(0)).current;
  const starScale2 = useRef(new Animated.Value(0)).current;
  const starScale3 = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    if (visible) {
      soundService.triggerVictory();

      scaleAnim.setValue(0.3);
      starScale1.setValue(0);
      starScale2.setValue(0);
      starScale3.setValue(0);

      Animated.spring(scaleAnim, {
        toValue: 1,
        friction: 5,
        tension: 40,
        useNativeDriver: true,
      }).start();

      setTimeout(() => {
        if (stars >= 1) {
          Animated.spring(starScale1, { toValue: 1, friction: 4, useNativeDriver: true }).start();
        }
      }, 300);

      setTimeout(() => {
        if (stars >= 2) {
          Animated.spring(starScale2, { toValue: 1, friction: 4, useNativeDriver: true }).start();
        }
      }, 600);

      setTimeout(() => {
        if (stars >= 3) {
          Animated.spring(starScale3, { toValue: 1, friction: 4, useNativeDriver: true }).start();
        }
      }, 900);
    }
  }, [visible, stars]);

  const getEncouragement = (s: number) => {
    if (s === 3) return { ar: 'مُمْتَاز !', fr: 'Parfait ! Tu es un champion !' };
    if (s === 2) return { ar: 'أَحْسَنْت !', fr: 'Très bien ! Continue ainsi !' };
    return { ar: 'جَيِّد !', fr: 'Bien joué ! Entraîne-toi encore !' };
  };

  const enc = getEncouragement(stars);

  return (
    <Modal visible={visible} transparent animationType="fade">
      <View style={styles.overlay}>
        <Animated.View style={[styles.card, { transform: [{ scale: scaleAnim }] }]}>
          {/* Header Banner */}
          <View style={styles.banner}>
            <Text style={styles.bannerAr}>{enc.ar}</Text>
            <Text style={styles.bannerFr}>{enc.fr}</Text>
          </View>

          {/* Stars Display */}
          <View style={styles.starsContainer}>
            <Animated.View style={{ transform: [{ scale: starScale1 }] }}>
              <Ionicons name={stars >= 1 ? 'star' : 'star-outline'} size={50} color="#F59E0B" />
            </Animated.View>
            <Animated.View style={[{ transform: [{ scale: starScale2 }], marginTop: -15 }]}>
              <Ionicons name={stars >= 2 ? 'star' : 'star-outline'} size={65} color="#F59E0B" />
            </Animated.View>
            <Animated.View style={{ transform: [{ scale: starScale3 }] }}>
              <Ionicons name={stars >= 3 ? 'star' : 'star-outline'} size={50} color="#F59E0B" />
            </Animated.View>
          </View>

          {/* Score & Rewards */}
          <View style={styles.rewardsRow}>
            <View style={styles.rewardItem}>
              <Ionicons name="checkmark-circle" size={24} color="#10B981" />
              <Text style={styles.rewardText}>{score} / {totalQuestions}</Text>
            </View>
            <View style={styles.rewardItem}>
              <Ionicons name="diamond" size={24} color="#06B6D4" />
              <Text style={styles.rewardText}>+{earnedCoins}</Text>
            </View>
          </View>

          {/* Buttons */}
          <View style={styles.buttonsContainer}>
            <TouchableOpacity style={styles.replayButton} onPress={onReplay} activeOpacity={0.8}>
              <Ionicons name="refresh" size={24} color="#475569" />
              <Text style={styles.replayText}>Rejouer</Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.nextButton} onPress={onNext} activeOpacity={0.8}>
              <Text style={styles.nextText}>Niveau Suivant</Text>
              <Ionicons name="arrow-forward" size={24} color="#FFFFFF" />
            </TouchableOpacity>
          </View>

          <TouchableOpacity style={styles.homeLink} onPress={onHome} activeOpacity={0.7}>
            <Ionicons name="map" size={18} color="#64748B" />
            <Text style={styles.homeText}>Retour à la carte des mondes</Text>
          </TouchableOpacity>
        </Animated.View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(15, 23, 42, 0.75)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  card: {
    width: '100%',
    maxWidth: 380,
    backgroundColor: '#FFFFFF',
    borderRadius: 32,
    padding: 24,
    alignItems: 'center',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 10 }, shadowOpacity: 0.25, shadowRadius: 20 },
      android: { elevation: 10 },
      web: { boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.2)' } as any,
    }),
  },
  banner: {
    alignItems: 'center',
    marginBottom: 20,
  },
  bannerAr: {
    fontSize: 34,
    fontWeight: '900',
    color: '#3B82F6',
    marginBottom: 4,
  },
  bannerFr: {
    fontSize: 16,
    fontWeight: '700',
    color: '#475569',
    textAlign: 'center',
  },
  starsContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 12,
    marginBottom: 24,
    height: 70,
  },
  rewardsRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 20,
    backgroundColor: '#F8FAFC',
    borderRadius: 20,
    paddingVertical: 12,
    paddingHorizontal: 24,
    marginBottom: 24,
    width: '100%',
  },
  rewardItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  rewardText: {
    fontSize: 18,
    fontWeight: '800',
    color: '#1E293B',
  },
  buttonsContainer: {
    flexDirection: 'row',
    gap: 12,
    width: '100%',
    marginBottom: 16,
  },
  replayButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    backgroundColor: '#F1F5F9',
    paddingVertical: 14,
    borderRadius: 18,
  },
  replayText: {
    fontSize: 15,
    fontWeight: '700',
    color: '#475569',
  },
  nextButton: {
    flex: 1.6,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: '#10B981',
    paddingVertical: 14,
    borderRadius: 18,
    ...Platform.select({
      ios: { shadowColor: '#10B981', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.3, shadowRadius: 6 },
      android: { elevation: 4 },
      web: { boxShadow: '0 4px 6px -1px rgba(16, 185, 129, 0.4)' } as any,
    }),
  },
  nextText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  homeLink: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 6,
  },
  homeText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#64748B',
  },
});

