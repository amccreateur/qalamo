import { createAudioPlayer, setAudioModeAsync, AudioPlayer } from 'expo-audio';
import * as Speech from 'expo-speech';
import * as Haptics from 'expo-haptics';
import { Platform } from 'react-native';
import { ALL_AUDIO_ASSETS, CHAR_TO_KEY } from './audioMap';
import { storageService } from './storageService';

class SoundService {
  private isMuted: boolean = false;
  private currentWebAudio: any = null;
  private currentNativePlayer: AudioPlayer | null = null;
  private isAudioModeConfigured: boolean = false;
  private playbackSpeed: number = 1.0;

  constructor() {
    this.initAudioMode();
    this.initPlaybackSpeed();
  }

  private async initPlaybackSpeed() {
    try {
      const speed = await storageService.getPlaybackSpeed();
      this.playbackSpeed = speed;
    } catch (_) {}
  }

  public setPlaybackSpeed(speed: number) {
    this.playbackSpeed = speed;
    storageService.setPlaybackSpeed(speed);
  }

  public getPlaybackSpeed(): number {
    return this.playbackSpeed;
  }

  private async initAudioMode() {
    if (Platform.OS !== 'web' && !this.isAudioModeConfigured) {
      try {
        await setAudioModeAsync({
          playsInSilentMode: true,
          interruptionMode: 'duckOthers',
          shouldPlayInBackground: false,
        });
        this.isAudioModeConfigured = true;
      } catch (e) {
        // Ignore initial configuration error
      }
    }
  }

  public setMuted(muted: boolean) {
    this.isMuted = muted;
    this.stopSpeaking();
  }

  public getMuted(): boolean {
    return this.isMuted;
  }

  /**
   * Play studio letter/vowel/word sound on Android, iOS, and Web
   */
  public async playSound(itemId?: string, fallbackText?: string, speed?: number): Promise<void> {
    if (this.isMuted) return;

    const effectiveSpeed = speed !== undefined ? speed : this.playbackSpeed;

    // 1. Determine key: by explicit id or by matching character
    let soundKey = itemId;
    if (!soundKey || !ALL_AUDIO_ASSETS[soundKey]) {
      if (fallbackText && CHAR_TO_KEY[fallbackText.trim()]) {
        soundKey = CHAR_TO_KEY[fallbackText.trim()];
      }
    }

    const asset = soundKey ? ALL_AUDIO_ASSETS[soundKey] : null;

    if (asset) {
      // A. Web Platform
      if (Platform.OS === 'web' && typeof window !== 'undefined') {
        try {
          if (this.currentWebAudio) {
            this.currentWebAudio.pause();
            this.currentWebAudio.currentTime = 0;
          }

          const uri = typeof asset === 'string' ? asset : asset?.default || asset?.uri || asset;
          const WebAudioClass = (window as any).Audio;
          if (WebAudioClass) {
            this.currentWebAudio = new WebAudioClass(uri);
            this.currentWebAudio.loop = false;
            this.currentWebAudio.playbackRate = effectiveSpeed;
            await this.currentWebAudio.play();
            return;
          }
        } catch (e) {
          console.warn('Web Audio play error:', e);
        }
      }

      // B. Native Android / iOS Platform (using modern expo-audio)
      if (Platform.OS !== 'web') {
        try {
          await this.initAudioMode();

          if (this.currentNativePlayer) {
            try {
              this.currentNativePlayer.pause();
              this.currentNativePlayer.release();
            } catch (_) {}
            this.currentNativePlayer = null;
          }

          const player = createAudioPlayer(asset);
          player.loop = false;
          if (typeof (player as any).setPlaybackRate === 'function') {
            (player as any).setPlaybackRate(effectiveSpeed);
          } else {
            player.playbackRate = effectiveSpeed;
          }
          player.shouldCorrectPitch = true;
          this.currentNativePlayer = player;
          player.play();

          return;
        } catch (e) {
          console.warn('Native Audio play error with expo-audio:', e);
        }
      }
    }

    // 2. Fallback to Speech only if no asset is available
    if (fallbackText) {
      try {
        await Speech.stop();
        Speech.speak(fallbackText, {
          language: 'ar-SA',
          pitch: 0.85,
          rate: 0.82 * effectiveSpeed,
        });
      } catch (e) {
        console.warn('Speech fallback error:', e);
      }
    }
  }

  /**
   * Pronounce text directly (tries asset first, fallback to Speech)
   */
  public async speakArabic(text: string, rate?: number): Promise<void> {
    if (this.isMuted) return;

    const cleanText = text.trim();
    if (CHAR_TO_KEY[cleanText]) {
      await this.playSound(CHAR_TO_KEY[cleanText], text);
      return;
    }

    const effectiveRate = rate !== undefined ? rate : 0.82 * this.playbackSpeed;
    try {
      await Speech.stop();
      Speech.speak(text, {
        language: 'ar-SA',
        pitch: 0.85,
        rate: effectiveRate,
      });
    } catch (e) {
      console.warn('Speech error:', e);
    }
  }

  public async stopSpeaking() {
    try {
      await Speech.stop();
    } catch (_) {}

    if (this.currentWebAudio) {
      try {
        this.currentWebAudio.pause();
      } catch (_) {}
    }

    if (this.currentNativePlayer) {
      try {
        this.currentNativePlayer.pause();
        this.currentNativePlayer.release();
        this.currentNativePlayer = null;
      } catch (_) {}
    }
  }

  public triggerSuccess() {
    if (Platform.OS !== 'web') {
      try {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      } catch (_) {}
    }
    this.playTone(587.33, 0.1);
    setTimeout(() => this.playTone(880, 0.15), 100);
  }

  public triggerError() {
    if (Platform.OS !== 'web') {
      try {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
      } catch (_) {}
    }
    this.playTone(220, 0.2);
  }

  public triggerPop() {
    if (Platform.OS !== 'web') {
      try {
        Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
      } catch (_) {}
    }
    this.playTone(440, 0.05);
  }

  public triggerVictory() {
    if (Platform.OS !== 'web') {
      try {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      } catch (_) {}
    }
    const notes = [523.25, 659.25, 783.99, 1046.5];
    notes.forEach((freq, idx) => {
      setTimeout(() => this.playTone(freq, 0.18), idx * 120);
    });
  }

  private playTone(frequency: number, duration: number) {
    if (this.isMuted) return;

    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      try {
        const AudioContext = window.AudioContext || (window as any).webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(frequency, ctx.currentTime);

        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (_) {}
    }
  }
}

export const soundService = new SoundService();
