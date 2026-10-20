export type Language = 'fr' | 'en';

export interface Translations {
  // Navigation & Common
  appTitle: string;
  home: string;
  back: string;
  close: string;
  cancel: string;
  replay: string;
  nextLevel: string;
  loading: string;
  
  // HeaderStats
  stars: string;
  coins: string;
  mute: string;
  unmute: string;
  langSwitch: string;

  // LevelMap
  quickExplorerTitle: string;
  quickExplorerSubtitle: string;
  quickAvatarTitle: string;
  quickAvatarSubtitle: string;
  discoverLessonBtn: string;
  bubbleGameLabel: string;
  targetGameLabel: string;
  wordBuilderGameLabel: string;
  miniGameLabel: string;
  levelPrefix: string;

  // LessonModal
  pedagogicalGuide: string;
  lessonSummary: string;
  tapToListenInstruction: string;
  startExercisesBtn: string;
  tipPrefix: string;

  // BubbleGame
  bubbleInstructionLetter: string;
  bubbleInstructionWord: string;
  bubbleInstructionPhrase: string;
  bubbleInstructionShape: string;
  bubbleReplayHint: string;
  bubbleShapePrefix: string;

  // TargetGame
  targetStageTitleSound: string;
  targetStageTitlePosition: string;
  targetStageSubtitleSound: string;
  targetStageSubtitleWord: string;
  targetStageSubtitlePhrase: string;
  targetStageSubtitlePosition: string;
  targetReplay: string;

  // WordBuilderGame
  listenWordBtn: string;
  orderLettersInstruction: string;
  clearBtn: string;

  // VictoryModal
  perfectEncouragementAr: string;
  perfectEncouragementText: string;
  greatEncouragementAr: string;
  greatEncouragementText: string;
  goodEncouragementAr: string;
  goodEncouragementText: string;
  scoreAccuracy: string;
  coinsWon: string;
  validateModuleTitle: string;
  validateModuleDesc: string;
  validateBtn: string;
  validatedBadge: string;
  alreadyValidatedBadge: string;
  savedInMemoryNotice: string;
  replayWithoutSaving: string;
  exitWithoutSaving: string;
  validatedTagOnMap: string;
  currentLevelBadge: string;
  resetProgressTitle: string;
  resetProgressMessage: string;
  resetProgressConfirm: string;

  // AvatarCustomizer
  avatarShopTitle: string;
  chooseAvatarSection: string;
  accessoriesSection: string;
  equippedBadge: string;
  equipBtn: string;
  buyBtn: string;
  priceCoins: string;

  // Avatars & Accessories names
  avatarLion: string;
  avatarFalcon: string;
  avatarBoy: string;
  avatarGirl: string;
  avatarCat: string;
  accCap: string;
  accCrown: string;
  accGlasses: string;
  accStarHat: string;
  accMedal: string;

  // SoundExplorer
  soundExplorerTitle: string;
  soundExplorerTitleAr: string;
  tabRawLetters: string;
  tabFatha: string;
  tabDamma: string;
  tabKasra: string;
  tabSukun: string;
  explorerHint: string;

  // Letter Positions
  posInitial: string;
  posMedial: string;
  posFinal: string;
  posIsolated: string;
}

export const TRANSLATIONS: Record<Language, Translations> = {
  fr: {
    appTitle: 'Qalamo — Apprendre à lire l\'arabe',
    home: 'Accueil',
    back: 'Retour',
    close: 'Fermer',
    cancel: 'Annuler',
    replay: 'Rejouer',
    nextLevel: 'Niveau Suivant',
    loading: 'Chargement...',

    stars: 'Étoiles',
    coins: 'Pièces',
    mute: 'Couper le son',
    unmute: 'Activer le son',
    langSwitch: 'FR',

    quickExplorerTitle: 'Explorateur',
    quickExplorerSubtitle: 'Écouter l\'alphabet',
    quickAvatarTitle: 'Mon Avatar',
    quickAvatarSubtitle: 'Boutique & Styles',
    discoverLessonBtn: '📖 Découvrir la Leçon & Règles',
    bubbleGameLabel: 'Jeu de Bulles',
    targetGameLabel: 'Tir Sonore',
    wordBuilderGameLabel: 'Mots & Syllabes',
    miniGameLabel: 'Mini-jeu',
    levelPrefix: 'Niveau',

    pedagogicalGuide: 'Fiche Pédagogique',
    lessonSummary: 'Résumé de la Leçon',
    tapToListenInstruction: '👉 Touchez une carte pour écouter le son :',
    startExercisesBtn: 'C\'est compris, passer aux exercices !',
    tipPrefix: '💡 Conseil :',

    bubbleInstructionLetter: 'Écoute et trouve la bonne lettre :',
    bubbleInstructionWord: 'Écoute et trouve le bon mot :',
    bubbleInstructionPhrase: 'Écoute et choisis la bonne phrase :',
    bubbleInstructionShape: 'Trouve la forme :',
    bubbleReplayHint: 'Touche le haut-parleur pour réécouter',
    bubbleShapePrefix: 'Position :',

    targetStageTitleSound: 'Tir Sonore / تَطَابُقُ الأَصْوَات',
    targetStageTitlePosition: 'Position de la Lettre / مَوْقِعُ الحَرْف',
    targetStageSubtitleSound: 'Quel signe correspond à ce son ?',
    targetStageSubtitleWord: 'Quel mot as-tu entendu ?',
    targetStageSubtitlePhrase: 'Quelle phrase as-tu entendue ?',
    targetStageSubtitlePosition: 'Trouve la forme :',
    targetReplay: 'Réécouter',

    listenWordBtn: 'Écouter le mot',
    orderLettersInstruction: 'Touche les lettres dans le bon ordre :',
    clearBtn: 'Effacer',

    perfectEncouragementAr: 'مُمْتَاز !',
    perfectEncouragementText: 'Parfait ! Tu es un champion !',
    greatEncouragementAr: 'أَحْسَنْت !',
    greatEncouragementText: 'Très bien ! Continue ainsi !',
    goodEncouragementAr: 'جَيِّد !',
    goodEncouragementText: 'Bien joué ! Entraîne-toi encore !',
    scoreAccuracy: 'Précision',
    coinsWon: 'Pièces gagnées',
    validateModuleTitle: 'Valider ce module ?',
    validateModuleDesc: 'Voulez-vous valider ce niveau et conserver votre réussite en mémoire pour vos prochaines connexions ?',
    validateBtn: 'Valider ce module',
    validatedBadge: 'Module validé avec succès !',
    alreadyValidatedBadge: 'Ce module est déjà validé',
    savedInMemoryNotice: 'Conservé en mémoire pour la prochaine connexion',
    replayWithoutSaving: 'Refaire sans valider',
    exitWithoutSaving: 'Retour à la carte sans valider',
    validatedTagOnMap: 'Validé',
    currentLevelBadge: 'À faire 🎯',
    resetProgressTitle: 'Réinitialiser la progression ?',
    resetProgressMessage: 'Toutes vos étoiles, vos pièces et vos niveaux validés seront remis à zéro. Êtes-vous sûr de vouloir recommencer depuis le début ?',
    resetProgressConfirm: 'Réinitialiser',

    avatarShopTitle: 'Mon Avatar & Boutique',
    chooseAvatarSection: 'Choisis ton Avatar',
    accessoriesSection: 'Accessoires & Chapeaux',
    equippedBadge: 'Équipé',
    equipBtn: 'Équiper',
    buyBtn: 'Acheter',
    priceCoins: 'pièces',

    avatarLion: 'Lionceau Courageux',
    avatarFalcon: 'Faucon Rapide',
    avatarBoy: 'Petit Explorateur',
    avatarGirl: 'Petite Aventurière',
    avatarCat: 'Chat Curieux',
    accCap: 'Casquette Cool',
    accCrown: 'Couronne Royale',
    accGlasses: 'Lunettes Savantes',
    accStarHat: 'Chapeau d\'Étoiles',
    accMedal: 'Médaille d\'Or',

    soundExplorerTitle: 'Explorateur Sonore',
    soundExplorerTitleAr: 'مُسْتَكْشِفُ الأَصْوَات',
    tabRawLetters: 'Lettres brutes',
    tabFatha: 'Avec Fatḥah ( ـَ )',
    tabDamma: 'Avec Ḍammah ( ـُ )',
    tabKasra: 'Avec Kasrah ( ـِ )',
    tabSukun: 'Avec Sukūn ( ـْ )',
    explorerHint: 'Touchez n\'importe quelle lettre pour entendre sa vocalisation studio',

    posInitial: 'Début de mot',
    posMedial: 'Milieu de mot',
    posFinal: 'Fin de mot',
    posIsolated: 'Forme isolée',
  },

  en: {
    appTitle: 'Qalamo — Learn to Read Arabic',
    home: 'Home',
    back: 'Back',
    close: 'Close',
    cancel: 'Cancel',
    replay: 'Replay',
    nextLevel: 'Next Level',
    loading: 'Loading...',

    stars: 'Stars',
    coins: 'Coins',
    mute: 'Mute audio',
    unmute: 'Unmute audio',
    langSwitch: 'EN',

    quickExplorerTitle: 'Explorer',
    quickExplorerSubtitle: 'Listen to the alphabet',
    quickAvatarTitle: 'My Avatar',
    quickAvatarSubtitle: 'Shop & Styles',
    discoverLessonBtn: '📖 Discover Lesson & Rules',
    bubbleGameLabel: 'Bubble Game',
    targetGameLabel: 'Sound Target',
    wordBuilderGameLabel: 'Words & Syllables',
    miniGameLabel: 'Mini-game',
    levelPrefix: 'Level',

    pedagogicalGuide: 'Pedagogical Guide',
    lessonSummary: 'Lesson Summary',
    tapToListenInstruction: '👉 Tap a card to listen to the sound:',
    startExercisesBtn: 'Got it, start the exercises!',
    tipPrefix: '💡 Tip:',

    bubbleInstructionLetter: 'Listen and find the right letter:',
    bubbleInstructionWord: 'Listen and find the right word:',
    bubbleInstructionPhrase: 'Listen and choose the right sentence:',
    bubbleInstructionShape: 'Find the shape:',
    bubbleReplayHint: 'Tap the speaker to replay',
    bubbleShapePrefix: 'Position:',

    targetStageTitleSound: 'Sound Target / تَطَابُقُ الأَصْوَات',
    targetStageTitlePosition: 'Letter Position / مَوْقِعُ الحَرْف',
    targetStageSubtitleSound: 'Which sign corresponds to this sound?',
    targetStageSubtitleWord: 'Which word did you hear?',
    targetStageSubtitlePhrase: 'Which sentence did you hear?',
    targetStageSubtitlePosition: 'Find the shape:',
    targetReplay: 'Replay',

    listenWordBtn: 'Listen to the word',
    orderLettersInstruction: 'Tap the letters in the correct order:',
    clearBtn: 'Clear',

    perfectEncouragementAr: 'مُمْتَاز !',
    perfectEncouragementText: 'Perfect! You are a champion!',
    greatEncouragementAr: 'أَحْسَنْت !',
    greatEncouragementText: 'Great job! Keep it up!',
    goodEncouragementAr: 'جَيِّد !',
    goodEncouragementText: 'Well done! Keep practicing!',
    scoreAccuracy: 'Accuracy',
    coinsWon: 'Coins earned',
    validateModuleTitle: 'Validate this module?',
    validateModuleDesc: 'Do you want to validate this level and keep your achievement in memory for your next sessions?',
    validateBtn: 'Validate this module',
    validatedBadge: 'Module successfully validated!',
    alreadyValidatedBadge: 'This module is already validated',
    savedInMemoryNotice: 'Saved in memory for next session',
    replayWithoutSaving: 'Replay without validating',
    exitWithoutSaving: 'Back to map without validating',
    validatedTagOnMap: 'Validated',
    currentLevelBadge: 'Next up 🎯',
    resetProgressTitle: 'Reset progress?',
    resetProgressMessage: 'All your stars, coins, and validated levels will be reset to zero. Are you sure you want to start over from the beginning?',
    resetProgressConfirm: 'Reset',

    avatarShopTitle: 'My Avatar & Shop',
    chooseAvatarSection: 'Choose your Avatar',
    accessoriesSection: 'Accessories & Hats',
    equippedBadge: 'Equipped',
    equipBtn: 'Equip',
    buyBtn: 'Buy',
    priceCoins: 'coins',

    avatarLion: 'Brave Lion Cub',
    avatarFalcon: 'Swift Falcon',
    avatarBoy: 'Little Explorer',
    avatarGirl: 'Little Adventurer',
    avatarCat: 'Curious Cat',
    accCap: 'Cool Cap',
    accCrown: 'Royal Crown',
    accGlasses: 'Scholar Glasses',
    accStarHat: 'Star Top Hat',
    accMedal: 'Gold Medal',

    soundExplorerTitle: 'Sound Explorer',
    soundExplorerTitleAr: 'مُسْتَكْشِفُ الأَصْوَات',
    tabRawLetters: 'Raw letters',
    tabFatha: 'With Fatḥah ( ـَ )',
    tabDamma: 'With Ḍammah ( ـُ )',
    tabKasra: 'With Kasrah ( ـِ )',
    tabSukun: 'With Sukūn ( ـْ )',
    explorerHint: 'Tap any letter to hear its clear studio pronunciation',

    posInitial: 'Beginning of word',
    posMedial: 'Middle of word',
    posFinal: 'End of word',
    posIsolated: 'Isolated form',
  },
};
