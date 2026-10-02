import React from 'react';
import {
  Modal,
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WorldLesson, LessonSample } from '../data/lessons';
import { soundService } from '../services/soundService';

interface LessonModalProps {
  visible: boolean;
  lesson: WorldLesson | null;
  onClose: () => void;
  onStartExercises?: () => void;
}

export const LessonModal: React.FC<LessonModalProps> = ({
  visible,
  lesson,
  onClose,
  onStartExercises,
}) => {
  if (!lesson) return null;

  const handlePlaySample = (sample: LessonSample) => {
    soundService.triggerPop();
    soundService.playSound(sample.audioKey, sample.audioText || sample.char);
  };

  return (
    <Modal
      visible={visible}
      animationType="slide"
      transparent={true}
      onRequestClose={onClose}
    >
      <View style={styles.modalOverlay}>
        <View style={styles.modalContent}>
          {/* Header Gradient */}
          <LinearGradient
            colors={[lesson.color, '#1E293B']}
            style={styles.headerGradient}
          >
            <View style={styles.headerTop}>
              <View style={styles.badgePill}>
                <Ionicons name="book" size={14} color="#FFFFFF" />
                <Text style={styles.badgeText}>Fiche Pédagogique</Text>
              </View>

              <TouchableOpacity style={styles.closeBtn} onPress={onClose} activeOpacity={0.8}>
                <Ionicons name="close" size={22} color="#FFFFFF" />
              </TouchableOpacity>
            </View>

            <Text style={styles.headerTitle}>{lesson.title}</Text>
            <Text style={styles.headerTitleAr}>{lesson.titleAr}</Text>
            <Text style={styles.headerSubtitle}>{lesson.subtitle}</Text>
          </LinearGradient>

          {/* Scrollable Lesson Body */}
          <ScrollView
            style={styles.bodyScroll}
            contentContainerStyle={styles.bodyScrollContent}
            showsVerticalScrollIndicator={false}
          >
            {/* World Summary Box */}
            <View style={styles.summaryCard}>
              <Ionicons name="bulb" size={22} color="#F59E0B" style={styles.summaryIcon} />
              <Text style={styles.summaryText}>{lesson.summary}</Text>
            </View>

            {/* Lesson Sections */}
            {lesson.sections.map((section, sIdx) => (
              <View key={sIdx} style={styles.sectionCard}>
                <View style={styles.sectionHeader}>
                  <Text style={styles.sectionTitle}>{section.title}</Text>
                  {section.titleAr && (
                    <Text style={styles.sectionTitleAr}>{section.titleAr}</Text>
                  )}
                </View>

                <Text style={styles.sectionContent}>{section.content}</Text>

                {section.tip && (
                  <View style={styles.tipBox}>
                    <Text style={styles.tipText}>{section.tip}</Text>
                  </View>
                )}

                {/* Interactive Audio Sample Cards */}
                {section.samples && section.samples.length > 0 && (
                  <View style={styles.samplesContainer}>
                    <Text style={styles.samplesInstruction}>
                      👉 Touchez une carte pour écouter le son :
                    </Text>
                    <View style={styles.samplesGrid}>
                      {section.samples.map((sample, idx) => {
                        const isWide = sample.char.length > 5 || sample.char.includes(' ');
                        return (
                          <TouchableOpacity
                            key={idx}
                            style={[styles.sampleChip, isWide && styles.sampleChipWide]}
                            onPress={() => handlePlaySample(sample)}
                            activeOpacity={0.7}
                          >
                            <LinearGradient
                              colors={['#FFFFFF', '#F8FAFC']}
                              style={styles.sampleChipGradient}
                            >
                              <View style={styles.speakerMiniCircle}>
                                <Ionicons name="volume-high" size={14} color="#3B82F6" />
                              </View>
                              <Text
                                style={[
                                  styles.sampleArabicChar,
                                  isWide && styles.sampleArabicCharWide,
                                ]}
                                numberOfLines={2}
                                adjustsFontSizeToFit
                              >
                                {sample.char}
                              </Text>
                              <Text style={styles.sampleTranscription}>{sample.transcription}</Text>
                              <Text style={styles.sampleLabel}>{sample.label}</Text>
                            </LinearGradient>
                          </TouchableOpacity>
                        );
                      })}
                    </View>
                  </View>
                )}
              </View>
            ))}
          </ScrollView>

          {/* Bottom Action Footer */}
          <View style={styles.footerBar}>
            <TouchableOpacity
              style={styles.primaryBtn}
              onPress={() => {
                onClose();
                if (onStartExercises) onStartExercises();
              }}
              activeOpacity={0.8}
            >
              <LinearGradient
                colors={['#10B981', '#059669']}
                style={styles.primaryBtnGradient}
              >
                <Text style={styles.primaryBtnText}>C'est compris, passer aux exercices !</Text>
                <Ionicons name="arrow-forward" size={18} color="#FFFFFF" />
              </LinearGradient>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(15, 23, 42, 0.75)',
    justifyContent: 'flex-end',
  },
  modalContent: {
    backgroundColor: '#F8FAFC',
    borderTopLeftRadius: 28,
    borderTopRightRadius: 28,
    height: '90%',
    overflow: 'hidden',
  },
  headerGradient: {
    padding: 20,
    paddingTop: 16,
    borderTopLeftRadius: 28,
    borderTopRightRadius: 28,
  },
  headerTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  badgePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  badgeText: {
    fontSize: 12,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  closeBtn: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: '900',
    color: '#FFFFFF',
  },
  headerTitleAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 22,
    fontWeight: '700',
    color: '#FEF08A',
    marginTop: 2,
    lineHeight: 32,
  },
  headerSubtitle: {
    fontSize: 13,
    fontWeight: '600',
    color: 'rgba(255, 255, 255, 0.85)',
    marginTop: 4,
  },
  bodyScroll: {
    flex: 1,
  },
  bodyScrollContent: {
    padding: 16,
    paddingBottom: 30,
    gap: 16,
  },
  summaryCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    backgroundColor: '#EFF6FF',
    borderRadius: 18,
    padding: 14,
    borderWidth: 1,
    borderColor: '#BFDBFE',
    gap: 10,
  },
  summaryIcon: {
    marginTop: 2,
  },
  summaryText: {
    flex: 1,
    fontSize: 14,
    fontWeight: '600',
    color: '#1E3A8A',
    lineHeight: 20,
  },
  sectionCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 20,
    padding: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.05, shadowRadius: 4 },
      android: { elevation: 2 },
      web: { boxShadow: '0 2px 4px rgba(0,0,0,0.04)' } as any,
    }),
  },
  sectionHeader: {
    marginBottom: 8,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  sectionTitleAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 17,
    fontWeight: '700',
    color: '#3B82F6',
    marginTop: 2,
  },
  sectionContent: {
    fontSize: 14,
    fontWeight: '500',
    color: '#334155',
    lineHeight: 22,
    marginBottom: 10,
  },
  tipBox: {
    backgroundColor: '#FFFBEB',
    borderLeftWidth: 4,
    borderLeftColor: '#F59E0B',
    padding: 10,
    borderRadius: 8,
    marginBottom: 12,
  },
  tipText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#92400E',
    lineHeight: 18,
  },
  samplesContainer: {
    marginTop: 6,
  },
  samplesInstruction: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    marginBottom: 8,
  },
  samplesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 10,
  },
  sampleChip: {
    flex: 1,
    minWidth: '45%',
    maxWidth: '48%',
    borderRadius: 16,
    overflow: 'hidden',
    borderWidth: 1.5,
    borderColor: '#CBD5E1',
  },
  sampleChipWide: {
    minWidth: '96%',
    maxWidth: '100%',
  },
  sampleChipGradient: {
    padding: 12,
    alignItems: 'center',
    position: 'relative',
  },
  speakerMiniCircle: {
    position: 'absolute',
    top: 6,
    right: 6,
    width: 22,
    height: 22,
    borderRadius: 11,
    backgroundColor: '#EFF6FF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  sampleArabicChar: {
    fontFamily: 'Amiri-Bold',
    fontSize: 38,
    fontWeight: '700',
    color: '#0F172A',
    includeFontPadding: true,
    textAlign: 'center',
    lineHeight: 52,
    marginVertical: 4,
  },
  sampleArabicCharWide: {
    fontSize: 32,
    lineHeight: 46,
  },
  sampleTranscription: {
    fontSize: 14,
    fontWeight: '800',
    color: '#3B82F6',
    marginTop: 2,
    textAlign: 'center',
  },
  sampleLabel: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
    textAlign: 'center',
    marginTop: 2,
  },
  footerBar: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    paddingBottom: Platform.OS === 'ios' ? 30 : 16,
    borderTopWidth: 1,
    borderTopColor: '#E2E8F0',
  },
  primaryBtn: {
    borderRadius: 18,
    overflow: 'hidden',
    ...Platform.select({
      ios: { shadowColor: '#10B981', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.3, shadowRadius: 6 },
      android: { elevation: 4 },
      web: { boxShadow: '0 4px 6px rgba(16, 185, 129, 0.3)' } as any,
    }),
  },
  primaryBtnGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 14,
    paddingHorizontal: 20,
    gap: 8,
  },
  primaryBtnText: {
    fontSize: 15,
    fontWeight: '800',
    color: '#FFFFFF',
  },
});
