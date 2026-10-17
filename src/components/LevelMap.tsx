import React from 'react';
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
import { World, Level, UserProgress } from '../types/game';
import { WORLDS } from '../data/curriculum';
import { soundService } from '../services/soundService';
import { useLanguage } from '../i18n/LanguageContext';

interface LevelMapProps {
  progress: UserProgress;
  onSelectLevel: (level: Level) => void;
  onOpenExplorer: () => void;
  onOpenAvatar: () => void;
  onOpenLesson: (worldId: number) => void;
}

export const LevelMap: React.FC<LevelMapProps> = ({
  progress,
  onSelectLevel,
  onOpenExplorer,
  onOpenAvatar,
  onOpenLesson,
}) => {
  const { language, t } = useLanguage();

  // Find all levels in order to identify the first unvalidated one
  const allLevels = React.useMemo(() => {
    let list: Level[] = [];
    WORLDS.forEach((w) => {
      list = [...list, ...w.levels];
    });
    return list;
  }, []);

  const firstUnvalidatedLevel = React.useMemo(() => {
    return allLevels.find((l) => !progress.validatedLevels?.[l.id]) || allLevels[0];
  }, [allLevels, progress.validatedLevels]);

  const scrollViewRef = React.useRef<ScrollView>(null);
  const worldLayoutY = React.useRef<Record<number, number>>({});
  const levelsListY = React.useRef<Record<number, number>>({});
  const levelLayoutY = React.useRef<Record<number, number>>({});
  const hasAutoScrolled = React.useRef(false);

  const attemptScrollToTarget = React.useCallback(() => {
    if (hasAutoScrolled.current || !firstUnvalidatedLevel) return;

    if (firstUnvalidatedLevel.id === 1) {
      hasAutoScrolled.current = true;
      return;
    }

    const wY = worldLayoutY.current[firstUnvalidatedLevel.worldId];
    const listY = levelsListY.current[firstUnvalidatedLevel.worldId] || 0;
    const lY = levelLayoutY.current[firstUnvalidatedLevel.id];

    if (wY !== undefined && lY !== undefined) {
      hasAutoScrolled.current = true;
      const targetY = Math.max(0, wY + listY + lY - 110);
      setTimeout(() => {
        scrollViewRef.current?.scrollTo({
          y: targetY,
          animated: true,
        });
      }, 350);
    }
  }, [firstUnvalidatedLevel]);

  // Scroll smoothly back to top when progress is reset
  const prevValidatedCount = React.useRef(Object.keys(progress.validatedLevels || {}).length);
  React.useEffect(() => {
    const currentCount = Object.keys(progress.validatedLevels || {}).length;
    if (prevValidatedCount.current > 0 && currentCount === 0) {
      hasAutoScrolled.current = true;
      scrollViewRef.current?.scrollTo({ y: 0, animated: true });
    }
    prevValidatedCount.current = currentCount;
  }, [progress.validatedLevels]);

  const getGameIcon = (type: Level['gameType']) => {
    switch (type) {
      case 'bubble': return 'radio-button-on';
      case 'target': return 'disc';
      case 'wordBuilder': return 'extension-puzzle';
      default: return 'play';
    }
  };

  const getGameLabel = (type: Level['gameType']) => {
    switch (type) {
      case 'bubble': return t.bubbleGameLabel;
      case 'target': return t.targetGameLabel;
      case 'wordBuilder': return t.wordBuilderGameLabel;
      default: return t.miniGameLabel;
    }
  };

  return (
    <ScrollView
      ref={scrollViewRef}
      style={styles.container}
      contentContainerStyle={styles.scrollContent}
    >
      {/* Quick Access Top Bar */}
      <View style={styles.quickAccessRow}>
        <TouchableOpacity style={styles.quickCard} onPress={onOpenExplorer} activeOpacity={0.8}>
          <LinearGradient colors={['#3B82F6', '#1D4ED8']} style={styles.quickGradient}>
            <Ionicons name="mic" size={24} color="#FFFFFF" />
            <View>
              <Text style={styles.quickTitle}>{t.quickExplorerTitle}</Text>
              <Text style={styles.quickSubtitle}>{t.quickExplorerSubtitle}</Text>
            </View>
          </LinearGradient>
        </TouchableOpacity>

        <TouchableOpacity style={styles.quickCard} onPress={onOpenAvatar} activeOpacity={0.8}>
          <LinearGradient colors={['#F59E0B', '#D97706']} style={styles.quickGradient}>
            <Ionicons name="shirt" size={24} color="#FFFFFF" />
            <View>
              <Text style={styles.quickTitle}>{t.quickAvatarTitle}</Text>
              <Text style={styles.quickSubtitle}>{t.quickAvatarSubtitle}</Text>
            </View>
          </LinearGradient>
        </TouchableOpacity>
      </View>

      {/* Worlds and Levels List */}
      {WORLDS.map((world: World, wIdx: number) => {
        const worldName = language === 'en' ? (world.nameEn || world.name) : world.name;
        const worldDesc = language === 'en' ? (world.descriptionEn || world.description) : world.description;

        return (
          <View
            key={world.id}
            style={styles.worldContainer}
            onLayout={(e) => {
              worldLayoutY.current[world.id] = e.nativeEvent.layout.y;
              attemptScrollToTarget();
            }}
          >
            {/* World Header Card */}
            <View style={styles.worldHeader}>
              <View style={[styles.worldIconCircle, { backgroundColor: world.color }]}>
                <Ionicons name="planet" size={24} color="#FFFFFF" />
              </View>
              <View style={styles.worldTitleBox}>
                <Text style={styles.worldName}>{worldName}</Text>
                <Text style={styles.worldNameAr}>{world.nameAr}</Text>
                <Text style={styles.worldDesc}>{worldDesc}</Text>

                {/* Lesson button for the world */}
                <TouchableOpacity
                  style={[styles.lessonPillBtn, { backgroundColor: `${world.color}15`, borderColor: world.color }]}
                  onPress={() => onOpenLesson(world.id)}
                  activeOpacity={0.7}
                >
                  <Ionicons name="book" size={14} color={world.color} />
                  <Text style={[styles.lessonPillText, { color: world.color }]}>
                    {t.discoverLessonBtn}
                  </Text>
                  <Ionicons name="chevron-forward" size={12} color={world.color} />
                </TouchableOpacity>
              </View>
            </View>

            {/* Levels along the road */}
            <View
              style={styles.levelsList}
              onLayout={(e) => {
                levelsListY.current[world.id] = e.nativeEvent.layout.y;
                attemptScrollToTarget();
              }}
            >
              {world.levels.map((level: Level, lIdx: number) => {
                const isUnlocked = true; // Débloqué pour tests
                const isValidated = !!progress.validatedLevels?.[level.id];
                const isCurrentTarget = level.id === firstUnvalidatedLevel?.id && !isValidated;
                const earnedStars = isValidated ? (progress.starsByLevel[level.id] || 0) : 0;
                const levelTitle = language === 'en' ? (level.titleEn || level.title) : level.title;

                return (
                  <TouchableOpacity
                    key={level.id}
                    style={[
                      styles.levelCard,
                      !isUnlocked && styles.levelCardLocked,
                      isCurrentTarget && styles.levelCardCurrent,
                    ]}
                    onLayout={(e) => {
                      levelLayoutY.current[level.id] = e.nativeEvent.layout.y;
                      if (level.id === firstUnvalidatedLevel?.id) {
                        attemptScrollToTarget();
                      }
                    }}
                    onPress={() => {
                      if (isUnlocked) {
                        soundService.triggerPop();
                        onSelectLevel(level);
                      } else {
                        soundService.triggerError();
                      }
                    }}
                    activeOpacity={isUnlocked ? 0.7 : 1}
                  >
                    <LinearGradient
                      colors={isUnlocked ? level.bgColor : ['#E2E8F0', '#CBD5E1']}
                      style={styles.levelCardGradient}
                    >
                      {/* Left Number & Status */}
                      <View style={[styles.levelNumberCircle, isValidated && styles.levelNumberCircleValidated]}>
                        {isUnlocked ? (
                          <Text style={[styles.levelNumber, isValidated && styles.levelNumberValidated]}>{level.id}</Text>
                        ) : (
                          <Ionicons name="lock-closed" size={18} color="#94A3B8" />
                        )}
                      </View>

                      {/* Middle Content */}
                      <View style={styles.levelInfo}>
                        <View style={styles.tagRow}>
                          <View style={styles.gameTypeTag}>
                            <Ionicons
                              name={getGameIcon(level.gameType) as any}
                              size={12}
                              color={isUnlocked ? '#FFFFFF' : '#64748B'}
                            />
                            <Text
                              style={[
                                styles.gameTypeText,
                                { color: isUnlocked ? 'rgba(255,255,255,0.9)' : '#64748B' },
                              ]}
                            >
                              {getGameLabel(level.gameType)}
                            </Text>
                          </View>

                          {isValidated && (
                            <View style={styles.validatedBadge}>
                              <Ionicons name="checkmark-circle" size={11} color="#FFFFFF" />
                              <Text style={styles.validatedBadgeText}>{t.validatedTagOnMap}</Text>
                            </View>
                          )}

                          {isCurrentTarget && (
                            <View style={styles.currentLevelBadge}>
                              <Ionicons name="sparkles" size={11} color="#92400E" />
                              <Text style={styles.currentLevelBadgeText}>{t.currentLevelBadge}</Text>
                            </View>
                          )}
                        </View>

                        <Text style={[styles.levelTitle, { color: isUnlocked ? '#FFFFFF' : '#475569' }]}>
                          {levelTitle}
                        </Text>
                        <Text style={[styles.levelTitleAr, { color: isUnlocked ? '#FEF08A' : '#94A3B8' }]}>
                          {level.titleAr}
                        </Text>
                      </View>

                      {/* Right Stars */}
                      <View style={styles.starsColumn}>
                        <View style={styles.starsRow}>
                          {[1, 2, 3].map((starIdx) => (
                            <Ionicons
                              key={starIdx}
                              name={earnedStars >= starIdx ? 'star' : 'star-outline'}
                              size={18}
                              color={earnedStars >= starIdx ? '#FBBF24' : isUnlocked ? 'rgba(255,255,255,0.5)' : '#94A3B8'}
                            />
                          ))}
                        </View>
                        {isUnlocked && (
                          <View style={[
                            styles.playButtonPill, 
                            isValidated && styles.playButtonPillValidated,
                            isCurrentTarget && styles.playButtonPillCurrent,
                          ]}>
                            <Text style={[
                              styles.playButtonText, 
                              isValidated && styles.playButtonTextValidated,
                              isCurrentTarget && styles.playButtonTextCurrent,
                            ]}>
                              {isValidated 
                                ? (language === 'en' ? 'Replay' : 'Revoir')
                                : (language === 'en' ? 'Play' : 'Jouer')}
                            </Text>
                            <Ionicons 
                              name="chevron-forward" 
                              size={14} 
                              color={isValidated ? '#047857' : isCurrentTarget ? '#B45309' : '#1E293B'} 
                            />
                          </View>
                        )}
                      </View>
                    </LinearGradient>
                  </TouchableOpacity>
                );
              })}
            </View>
          </View>
        );
      })}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F1F5F9',
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 50,
  },
  quickAccessRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 20,
  },
  quickCard: {
    flex: 1,
    borderRadius: 20,
    overflow: 'hidden',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.1, shadowRadius: 6 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.1)' } as any,
    }),
  },
  quickGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    padding: 14,
  },
  quickTitle: {
    fontSize: 15,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  quickSubtitle: {
    fontSize: 11,
    fontWeight: '600',
    color: 'rgba(255, 255, 255, 0.85)',
  },
  worldContainer: {
    marginBottom: 28,
  },
  worldHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 24,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.05, shadowRadius: 4 },
      android: { elevation: 2 },
      web: { boxShadow: '0 2px 4px rgba(0,0,0,0.05)' } as any,
    }),
  },
  worldIconCircle: {
    width: 48,
    height: 48,
    borderRadius: 24,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 14,
  },
  worldTitleBox: {
    flex: 1,
  },
  worldName: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
  },
  worldNameAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 18,
    fontWeight: '700',
    color: '#3B82F6',
    marginTop: 2,
  },
  worldDesc: {
    fontSize: 12,
    fontWeight: '500',
    color: '#64748B',
    marginTop: 2,
  },
  lessonPillBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'flex-start',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 12,
    borderWidth: 1,
    marginTop: 8,
  },
  lessonPillText: {
    fontSize: 12,
    fontWeight: '800',
  },
  levelsList: {
    gap: 12,
  },
  levelCard: {
    borderRadius: 22,
    overflow: 'hidden',
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.12, shadowRadius: 6 },
      android: { elevation: 3 },
      web: { boxShadow: '0 4px 6px rgba(0,0,0,0.08)' } as any,
    }),
  },
  levelCardLocked: {
    opacity: 0.75,
  },
  levelCardGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    gap: 12,
  },
  levelNumberCircle: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: '#FFFFFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  levelNumber: {
    fontSize: 18,
    fontWeight: '900',
    color: '#1E293B',
  },
  levelNumberCircleValidated: {
    borderWidth: 2,
    borderColor: '#10B981',
    backgroundColor: '#F0FDF4',
  },
  levelNumberValidated: {
    color: '#047857',
  },
  levelInfo: {
    flex: 1,
  },
  tagRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 4,
    flexWrap: 'wrap',
  },
  gameTypeTag: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  validatedBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    backgroundColor: 'rgba(16, 185, 129, 0.45)',
    borderColor: '#10B981',
    borderWidth: 1,
    paddingHorizontal: 7,
    paddingVertical: 1.5,
    borderRadius: 10,
  },
  validatedBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  gameTypeText: {
    fontSize: 11,
    fontWeight: '700',
  },
  levelTitle: {
    fontSize: 15,
    fontWeight: '800',
  },
  levelTitleAr: {
    fontFamily: 'Amiri-Bold',
    fontSize: 21,
    fontWeight: '700',
    marginTop: 2,
  },
  starsColumn: {
    alignItems: 'flex-end',
    gap: 6,
  },
  starsRow: {
    flexDirection: 'row',
    gap: 2,
  },
  playButtonPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    gap: 2,
  },
  playButtonPillValidated: {
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#86EFAC',
  },
  playButtonPillCurrent: {
    backgroundColor: '#FEF3C7',
    borderWidth: 1,
    borderColor: '#F59E0B',
  },
  playButtonText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#1E293B',
  },
  playButtonTextValidated: {
    color: '#047857',
  },
  playButtonTextCurrent: {
    color: '#92400E',
    fontWeight: '900',
  },
  levelCardCurrent: {
    borderWidth: 2.5,
    borderColor: '#F59E0B',
    ...Platform.select({
      ios: { shadowColor: '#F59E0B', shadowOffset: { width: 0, height: 4 }, shadowOpacity: 0.35, shadowRadius: 8 },
      android: { elevation: 6 },
      web: { boxShadow: '0 4px 14px rgba(245, 158, 11, 0.4)' } as any,
    }),
  },
  currentLevelBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    backgroundColor: '#FEF3C7',
    borderColor: '#F59E0B',
    borderWidth: 1,
    paddingHorizontal: 7,
    paddingVertical: 1.5,
    borderRadius: 10,
  },
  currentLevelBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#92400E',
  },
});
