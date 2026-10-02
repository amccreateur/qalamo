export interface LessonSample {
  char: string;
  transcription: string;
  audioKey?: string;
  audioText?: string;
  label: string;
}

export interface LessonSection {
  title: string;
  titleAr?: string;
  content: string;
  tip?: string;
  samples?: LessonSample[];
}

export interface WorldLesson {
  worldId: number;
  title: string;
  titleAr: string;
  subtitle: string;
  icon: string;
  color: string;
  summary: string;
  sections: LessonSection[];
}

export const WORLD_LESSONS: Record<number, WorldLesson> = {
  // ==========================================
  // MONDE 1 : L'ALPHABET & LES SONS FONDAMENTAUX
  // ==========================================
  1: {
    worldId: 1,
    title: 'Monde 1 : L\'Alphabet & les 28 Sons',
    titleAr: 'حُرُوفُ الهِجَاءِ وَأَصْوَاتُهَا',
    subtitle: 'Les fondations de la lecture arabe',
    icon: 'text',
    color: '#3B82F6',
    summary: 'L\'alphabet arabe compte 28 lettres fondamentales. L\'arabe se lit et s\'écrit de droite à gauche (RTL). Chaque lettre possède un son unique et précis.',
    sections: [
      {
        title: '1. Reconnaître les lettres par leurs points',
        titleAr: 'تَمْيِيزُ الحُرُوفِ بِالنِّقَاط',
        content: 'En arabe, plusieurs lettres partagent le même corps de base (le "bateau" ou la "boucle"). Seul le nombre et la position des points permettent de les distinguer !',
        tip: '💡 Astuce : Comptez toujours bien les points ! 1 point en bas = Ba (ب), 2 points en haut = Ta (ت), 3 points bien séparés = Tha (ث).',
        samples: [
          { char: 'ب', transcription: 'Ba', audioKey: 'ba', label: '1 point en bas' },
          { char: 'ت', transcription: 'Ta', audioKey: 'ta', label: '2 points en haut' },
          { char: 'ث', transcription: 'Tha', audioKey: 'tha', label: '3 points en haut' },
          { char: 'ن', transcription: 'Noon', audioKey: 'noon', label: '1 point en haut' },
        ],
      },
      {
        title: '2. La famille des boucles (Jeem, Ḥa, Kha)',
        titleAr: 'عَائِلَةُ الجِيمِ وَالحَاءِ وَالخَاء',
        content: 'Ces 3 lettres ont exactement la même forme de vague. Observez attentivement le point :',
        tip: '💡 Jeem a un point dans le ventre, Kha a un point sur la tête, Ḥa n\'a aucun point et vient du fond de la gorge.',
        samples: [
          { char: 'ج', transcription: 'Jeem (Ja)', audioKey: 'jeem', label: 'Point au ventre' },
          { char: 'ح', transcription: 'Ḥa (gorge)', audioKey: 'hha', label: 'Sans point' },
          { char: 'خ', transcription: 'Kha (raclement)', audioKey: 'kha', label: 'Point au-dessus' },
        ],
      },
      {
        title: '3. Les lettres simples vs les lettres emphatiques',
        titleAr: 'الحُرُوفُ المُرَقَّقَة وَالمُفَخَّمَة',
        content: 'Certaines lettres se prononcent avec la bouche fine (mince), d\'autres avec la bouche ronde et puissante (emphatiques).',
        samples: [
          { char: 'س', transcription: 'Seen (fin)', audioKey: 'seen', label: 'Son "S" doux' },
          { char: 'ص', transcription: 'Ṣad (épais)', audioKey: 'sad', label: 'Son "Ṣ" puissant' },
          { char: 'ت', transcription: 'Ta (fin)', audioKey: 'ta', label: 'Son "T" doux' },
          { char: 'ط', transcription: 'Ṭa (épais)', audioKey: 'ttaa', label: 'Son "Ṭ" puissant' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 2 : LES FORMES DES LETTRES (POSITIONS)
  // ==========================================
  2: {
    worldId: 2,
    title: 'Monde 2 : Les Formes des Lettres',
    titleAr: 'أَشْكَالُ الحُرُوفِ فِي الكَلِمَة',
    subtitle: 'Comment les 28 lettres s\'attachent pour former des mots',
    icon: 'shapes',
    color: '#8B5CF6',
    summary: 'L\'arabe est une écriture cursive (attachée). Comme les enfants qui se donnent la main, chaque lettre tend un bras selon sa position : au Début, au Milieu ou à la Fin du mot.',
    sections: [
      {
        title: '1. Les 6 Lettres Magiques Non-Attachantes (أ د ذ ر ز و)',
        titleAr: 'الحُرُوفُ الرَّافِضَة ( أ ، د ، ذ ، ر ، ز ، و )',
        content: 'Règle d\'or fondamentale : ces 6 lettres ne s\'attachent JAMAIS vers la gauche. La lettre suivante recommence donc en position début !',
        tip: '💡 Retenez bien ce groupe de 6 : Alif (أ), Dal (د), Dhal (ذ), Ra (ر), Zay (ز), Waw (و).',
        samples: [
          { char: 'أ', transcription: 'Alif', audioKey: 'alif', label: 'Ne s\'attache pas à gauche' },
          { char: 'د', transcription: 'Dal', audioKey: 'dal', label: 'Ne s\'attache pas à gauche' },
          { char: 'ذ', transcription: 'Dhal', audioKey: 'dhal', label: 'Ne s\'attache pas à gauche' },
          { char: 'ر', transcription: 'Ra', audioKey: 'ra', label: 'Ne s\'attache pas à gauche' },
          { char: 'ز', transcription: 'Zay', audioKey: 'zay', label: 'Ne s\'attache pas à gauche' },
          { char: 'و', transcription: 'Waw', audioKey: 'waw', label: 'Ne s\'attache pas à gauche' },
        ],
      },
      {
        title: '2. Les 22 Lettres au Début du mot (ـ...) : Le bras gauche tendu',
        titleAr: 'فِي أَوَّلِ الكَلِمَة ( جَمِيعُ الحُرُوف )',
        content: 'La lettre coupe sa fin pour tendre la main vers la gauche :',
        samples: [
          { char: 'بـ', transcription: 'b-', audioKey: 'ba', label: 'Ba début' },
          { char: 'تـ', transcription: 't-', audioKey: 'ta', label: 'Ta début' },
          { char: 'ثـ', transcription: 'th-', audioKey: 'tha', label: 'Tha début' },
          { char: 'جـ', transcription: 'j-', audioKey: 'jeem', label: 'Jeem début' },
          { char: 'حـ', transcription: 'ḥ-', audioKey: 'hha', label: 'Ḥa début' },
          { char: 'خـ', transcription: 'kh-', audioKey: 'kha', label: 'Kha début' },
          { char: 'سـ', transcription: 's-', audioKey: 'seen', label: 'Seen début' },
          { char: 'شـ', transcription: 'sh-', audioKey: 'sheen', label: 'Sheen début' },
          { char: 'صـ', transcription: 'ṣ-', audioKey: 'sad', label: 'Ṣad début' },
          { char: 'ضـ', transcription: 'ḍ-', audioKey: 'dad', label: 'Ḍad début' },
          { char: 'طـ', transcription: 'ṭ-', audioKey: 'ttaa', label: 'Ṭa début' },
          { char: 'ظـ', transcription: 'ẓ-', audioKey: 'zha', label: 'Ẓa début' },
          { char: 'عـ', transcription: 'ʿ-', audioKey: 'ayn', label: 'Ayn début' },
          { char: 'غـ', transcription: 'gh-', audioKey: 'ghayn', label: 'Ghayn début' },
          { char: 'فـ', transcription: 'f-', audioKey: 'fa', label: 'Fa début' },
          { char: 'قـ', transcription: 'q-', audioKey: 'qaf', label: 'Qaf début' },
          { char: 'كـ', transcription: 'k-', audioKey: 'kaf', label: 'Kaf début' },
          { char: 'لـ', transcription: 'l-', audioKey: 'lam', label: 'Lam début' },
          { char: 'مـ', transcription: 'm-', audioKey: 'meem', label: 'Meem début' },
          { char: 'نـ', transcription: 'n-', audioKey: 'noon', label: 'Noon début' },
          { char: 'هـ', transcription: 'h-', audioKey: 'haa', label: 'Haa début' },
          { char: 'يـ', transcription: 'y-', audioKey: 'yaa', label: 'Yaa début' },
        ],
      },
      {
        title: '3. Les 22 Lettres au Milieu du mot (ـ...ـ) : Les 2 bras ouverts',
        titleAr: 'فِي وَسَطِ الكَلِمَة ( جَمِيعُ الحُرُوف )',
        content: 'La lettre est reliée avant et après par ses deux bras :',
        samples: [
          { char: 'ـبـ', transcription: '-b-', audioKey: 'ba', label: 'Ba milieu' },
          { char: 'ـتـ', transcription: '-t-', audioKey: 'ta', label: 'Ta milieu' },
          { char: 'ـثـ', transcription: '-th-', audioKey: 'tha', label: 'Tha milieu' },
          { char: 'ـجـ', transcription: '-j-', audioKey: 'jeem', label: 'Jeem milieu' },
          { char: 'ـحـ', transcription: '-ḥ-', audioKey: 'hha', label: 'Ḥa milieu' },
          { char: 'ـخـ', transcription: '-kh-', audioKey: 'kha', label: 'Kha milieu' },
          { char: 'ـسـ', transcription: '-s-', audioKey: 'seen', label: 'Seen milieu' },
          { char: 'ـشـ', transcription: '-sh-', audioKey: 'sheen', label: 'Sheen milieu' },
          { char: 'ـصـ', transcription: '-ṣ-', audioKey: 'sad', label: 'Ṣad milieu' },
          { char: 'ـضـ', transcription: '-ḍ-', audioKey: 'dad', label: 'Ḍad milieu' },
          { char: 'ـطـ', transcription: '-ṭ-', audioKey: 'ttaa', label: 'Ṭa milieu' },
          { char: 'ـظـ', transcription: '-ẓ-', audioKey: 'zha', label: 'Ẓa milieu' },
          { char: 'ـعـ', transcription: '-ʿ-', audioKey: 'ayn', label: 'Ayn milieu' },
          { char: 'ـغـ', transcription: '-gh-', audioKey: 'ghayn', label: 'Ghayn milieu' },
          { char: 'ـفـ', transcription: '-f-', audioKey: 'fa', label: 'Fa milieu' },
          { char: 'ـقـ', transcription: '-q-', audioKey: 'qaf', label: 'Qaf milieu' },
          { char: 'ـكـ', transcription: '-k-', audioKey: 'kaf', label: 'Kaf milieu' },
          { char: 'ـلـ', transcription: '-l-', audioKey: 'lam', label: 'Lam milieu' },
          { char: 'ـمـ', transcription: '-m-', audioKey: 'meem', label: 'Meem milieu' },
          { char: 'ـنـ', transcription: '-n-', audioKey: 'noon', label: 'Noon milieu' },
          { char: 'ـهـ', transcription: '-h-', audioKey: 'haa', label: 'Haa milieu' },
          { char: 'ـيـ', transcription: '-y-', audioKey: 'yaa', label: 'Yaa milieu' },
        ],
      },
      {
        title: '4. Les 22 Lettres à la Fin du mot (...ـ) : La fermeture',
        titleAr: 'فِي آخِرِ الكَلِمَة ( جَمِيعُ الحُرُوف )',
        content: 'La lettre reçoit l\'attache précédente et referme sa forme entière :',
        samples: [
          { char: 'ـب', transcription: '-b', audioKey: 'ba', label: 'Ba fin' },
          { char: 'ـت', transcription: '-t', audioKey: 'ta', label: 'Ta fin' },
          { char: 'ـث', transcription: '-th', audioKey: 'tha', label: 'Tha fin' },
          { char: 'ـج', transcription: '-j', audioKey: 'jeem', label: 'Jeem fin' },
          { char: 'ـح', transcription: '-ḥ', audioKey: 'hha', label: 'Ḥa fin' },
          { char: 'ـخ', transcription: '-kh', audioKey: 'kha', label: 'Kha fin' },
          { char: 'ـس', transcription: '-s', audioKey: 'seen', label: 'Seen fin' },
          { char: 'ـش', transcription: '-sh', audioKey: 'sheen', label: 'Sheen fin' },
          { char: 'ـص', transcription: '-ṣ', audioKey: 'sad', label: 'Ṣad fin' },
          { char: 'ـض', transcription: '-ḍ', audioKey: 'dad', label: 'Ḍad fin' },
          { char: 'ـط', transcription: '-ṭ', audioKey: 'ttaa', label: 'Ṭa fin' },
          { char: 'ـظ', transcription: '-ẓ', audioKey: 'zha', label: 'Ẓa fin' },
          { char: 'ـع', transcription: '-ʿ', audioKey: 'ayn', label: 'Ayn fin' },
          { char: 'ـغ', transcription: '-gh', audioKey: 'ghayn', label: 'Ghayn fin' },
          { char: 'ـف', transcription: '-f', audioKey: 'fa', label: 'Fa fin' },
          { char: 'ـق', transcription: '-q', audioKey: 'qaf', label: 'Qaf fin' },
          { char: 'ـك', transcription: '-k', audioKey: 'kaf', label: 'Kaf fin' },
          { char: 'ـل', transcription: '-l', audioKey: 'lam', label: 'Lam fin' },
          { char: 'ـم', transcription: '-m', audioKey: 'meem', label: 'Meem fin' },
          { char: 'ـن', transcription: '-n', audioKey: 'noon', label: 'Noon fin' },
          { char: 'ـه', transcription: '-h', audioKey: 'haa', label: 'Haa fin' },
          { char: 'ـي', transcription: '-y', audioKey: 'yaa', label: 'Yaa fin' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 3 : LES VOYELLES COURTES (HARAKĀT)
  // ==========================================
  3: {
    worldId: 3,
    title: 'Monde 3 : Les Voyelles Courtes (الحركات)',
    titleAr: 'الحَرَكَاتُ القَصِيرَة : الفَتْحَة وَالضَّمَّة وَالكَسْرَة',
    subtitle: 'Donner vie aux consonnes en 1 temps vif',
    icon: 'volume-high',
    color: '#10B981',
    summary: 'Les lettres arabes sont des consonnes. Pour les faire chanter, on leur ajoute de petits signes voyelles (Harakāt). Ces voyelles sont courtes, nettes et durent 1 seul temps (environ 250ms).',
    sections: [
      {
        title: '1. La Fatḥah (ـَ) : Le son "A" ouvert',
        titleAr: 'الفَتْحَة ( ـَ )',
        content: 'Un petit trait oblique placé au-dessus de la lettre. On ouvre la bouche pour faire un son "A" franc et rapide.',
        samples: [
          { char: 'بَ', transcription: 'Ba', audioKey: 'ba_fatha', label: 'B + A' },
          { char: 'تَ', transcription: 'Ta', audioKey: 'ta_fatha', label: 'T + A' },
          { char: 'دَ', transcription: 'Da', audioKey: 'da_fatha', label: 'D + A' },
          { char: 'سَ', transcription: 'Sa', audioKey: 'sa_fatha', label: 'S + A' },
        ],
      },
      {
        title: '2. La Ḍammah (ـُ) : Le son "OU" arrondi',
        titleAr: 'الضَّمَّة ( ـُ )',
        content: 'Un petit 9 miniature posé au-dessus de la lettre. On arrondit les lèvres pour produire un son "OU" bref.',
        samples: [
          { char: 'بُ', transcription: 'Bou', audioKey: 'bu_damma', label: 'B + OU' },
          { char: 'تُ', transcription: 'Tou', audioKey: 'tu_damma', label: 'T + OU' },
          { char: 'دُ', transcription: 'Dou', audioKey: 'du_damma', label: 'D + OU' },
          { char: 'مُ', transcription: 'Mou', audioKey: 'mu_damma', label: 'M + OU' },
        ],
      },
      {
        title: '3. La Kasrah (ـِ) : Le son "I" souriant',
        titleAr: 'الكَسْرَة ( ـِ )',
        content: 'Un petit trait oblique placé sous la lettre. On tire légèrement les lèvres en souriant pour faire un son "I" net.',
        samples: [
          { char: 'بِ', transcription: 'Bi', audioKey: 'bi_kasra', label: 'B + I' },
          { char: 'تِ', transcription: 'Ti', audioKey: 'ti_kasra', label: 'T + I' },
          { char: 'دِ', transcription: 'Di', audioKey: 'di_kasra', label: 'D + I' },
          { char: 'رِ', transcription: 'Ri', audioKey: 'ri_kasra', label: 'R + I' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 4 : SUKŪN & VOYELLES LONGUES (MADD)
  // ==========================================
  4: {
    worldId: 4,
    title: 'Monde 4 : Sukūn & Voyelles Longues (المَدّ)',
    titleAr: 'السُّكُونُ وَحُرُوفُ المَدِّ الثَّلَاثَة',
    subtitle: 'L\'arrêt consonnantique vs l\'allongement en 2 temps',
    icon: 'pulse',
    color: '#06B6D4',
    summary: 'Deux notions indispensables : le Sukūn (qui stoppe net la consonne sans voyelle) et le Madd (qui étire la voyelle sur 2 temps complets, soit deux fois plus long que la Harakah).',
    sections: [
      {
        title: '1. Le Sukūn (ـْ) : L\'arrêt net',
        titleAr: 'السُّكُون ( ـْ )',
        content: 'Le petit cercle au-dessus de la lettre indique qu\'aucune voyelle n\'est prononcée : la consonne se bloque net.',
        samples: [
          { char: 'أَبْ', transcription: 'Ab', audioKey: 'ab_sukun', label: 'A + B net' },
          { char: 'قُلْ', transcription: 'Qul', audioKey: 'qul_sukun', label: 'Qu + L net' },
          { char: 'مِنْ', transcription: 'Min', audioKey: 'min_sukun', label: 'Mi + N net' },
          { char: 'قَدْ', transcription: 'Qad', audioKey: 'qad_sukun', label: 'Qa + D net' },
        ],
      },
      {
        title: '2. Les 3 Lettres de Prolongation (Madd)',
        titleAr: 'حُرُوفُ المَدّ ( ا ، و ، ي )',
        content: 'Quand une Harakah rencontre sa lettre amie (Fatḥah + Alif, Ḍammah + Waw, Kasrah + Ya), le son devient long (2 temps bien audibles).',
        tip: '💡 Règle d\'or : 1 temps = Court (بَ = Ba) | 2 temps = Long (بَا = Bââ).',
        samples: [
          { char: 'بَا', transcription: 'Bââ (2t)', audioKey: 'baa_long', label: 'Madd Alif (ـَا)' },
          { char: 'بُو', transcription: 'Bouu (2t)', audioKey: 'boo_long', label: 'Madd Waw (ـُو)' },
          { char: 'بِي', transcription: 'Biii (2t)', audioKey: 'bee_long', label: 'Madd Ya (ـِي)' },
        ],
      },
      {
        title: '3. Comparaison directe : Court (1t) vs Long (2t)',
        titleAr: 'المُقَارَنَةُ بَيْنَ القَصِيرِ وَالطَّوِيل',
        content: 'Entraînez votre oreille à distinguer immédiatement la durée :',
        samples: [
          { char: 'بَ', transcription: 'Ba (1t)', audioKey: 'ba_fatha', label: 'Court (1t)' },
          { char: 'بَا', transcription: 'Bââ (2t)', audioKey: 'baa_long', label: 'Long (2t)' },
          { char: 'دُ', transcription: 'Dou (1t)', audioKey: 'du_damma', label: 'Court (1t)' },
          { char: 'دُو', transcription: 'Douuu (2t)', audioKey: 'doo_long', label: 'Long (2t)' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 5 : SHADDAH, TANWĪN & ALIF-LĀM
  // ==========================================
  5: {
    worldId: 5,
    title: 'Monde 5 : Shaddah, Tanwīn & Alif-Lām',
    titleAr: 'الشَّدَّةُ وَالتَّنْوِينُ وَلاَمُ التَّعْرِيف',
    subtitle: 'Les secrets de la lecture courante',
    icon: 'flash',
    color: '#E11D48',
    summary: 'Trois règles majeures pour lire les mots avec précision : doubler une consonne avec la Shaddah, nasaliser avec le Tanwīn, et distinguer les lettres solaires et lunaires avec Alif-Lām (الـ).',
    sections: [
      {
        title: '1. La Shaddah (ـّ) : La consonne appuyée',
        titleAr: 'الشَّدَّة ( ـّ )',
        content: 'Ce signe en forme de petit "w" indique que la lettre est doublée : on marque une pause ferme et on appuie sur la lettre.',
        samples: [
          { char: 'رَبَّ', transcription: 'Rab-ba', audioKey: 'rabba', label: 'Appuyé sur le B' },
          { char: 'مَدَّ', transcription: 'Mad-da', audioKey: 'madda', label: 'Appuyé sur le D' },
          { char: 'عَلَّمَ', transcription: '\'Al-lama', audioKey: 'allama', label: 'Appuyé sur le L' },
        ],
      },
      {
        title: '2. Le Tanwīn Fatḥah (ـً) : Terminaison ouverte en "-an"',
        titleAr: 'تَنْوِينُ الفَتْحِ : صَوْتُ أَنْ (ـً)',
        content: 'Deux traits obliques au-dessus de la dernière lettre (généralement soutenus par un Alif). La voix produit le son "AN" nasalisé.',
        samples: [
          { char: 'كِتَابًا', transcription: 'Kitāban', audioKey: 'kitaban', label: 'Un livre (-an)' },
          { char: 'وَلَدًا', transcription: 'Waladan', audioKey: 'waladan', label: 'Un garçon (-an)' },
          { char: 'بَيْتًا', transcription: 'Baytan', audioKey: 'baytan', label: 'Une maison (-an)' },
        ],
      },
      {
        title: '3. Le Tanwīn Ḍammah (ـٌ) : Terminaison fermée en "-oun"',
        titleAr: 'تَنْوِينُ الضَّمِّ : صَوْتُ أُنْ (ـٌ)',
        content: 'Deux petites boucles au-dessus de la dernière lettre. La voix produit le son "OUN" (un "OU" nasalisé en "N").',
        samples: [
          { char: 'كِتَابٌ', transcription: 'Kitābun', audioKey: 'kitabun', label: 'Un livre (-oun)' },
          { char: 'وَلَدٌ', transcription: 'Waladun', audioKey: 'waladun', label: 'Un garçon (-oun)' },
          { char: 'بَيْتٌ', transcription: 'Baytun', audioKey: 'baytun', label: 'Une maison (-oun)' },
        ],
      },
      {
        title: '4. Le Tanwīn Kasrah (ـٍ) : Terminaison en "-in"',
        titleAr: 'تَنْوِينُ الكَسْرِ : صَوْتُ إِنْ (ـٍ)',
        content: 'Deux traits obliques placés sous la dernière lettre. La voix produit le son "IN" nasalisé.',
        samples: [
          { char: 'كِتَابٍ', transcription: 'Kitābin', audioKey: 'kitabin', label: 'D\'un livre (-in)' },
          { char: 'وَلَدٍ', transcription: 'Waladin', audioKey: 'waladin', label: 'D\'un garçon (-in)' },
          { char: 'بَيْتٍ', transcription: 'Baytin', audioKey: 'baytin', label: 'D\'une maison (-in)' },
        ],
      },
      {
        title: '5. L\'article Alif-Lām (الـ) : Lunaires vs Solaires',
        titleAr: 'اللاَّمُ القَمَرِيَّةُ وَالشَّمْسِيَّة',
        content: '• Lettres Lunaires : Le "L" s\'entend clairement (ex: القَمَر = Al-Qamar).\n• Lettres Solaires : Le "L" est muet et la lettre suivante prend une Shaddah (ex: الشَّمْس = Ash-Shams).',
        samples: [
          { char: 'القَمَر', transcription: 'Al-Qamar', audioKey: 'al_qamar', label: 'Lunaire (L prononcé)' },
          { char: 'الشَّمْس', transcription: 'Ash-Shams', audioKey: 'ash_shams', label: 'Solaire (L muet + Shaddah)' },
          { char: 'الكِتَاب', transcription: 'Al-Kitāb', audioKey: 'al_kitaab', label: 'Lunaire (L prononcé)' },
          { char: 'النَّجْم', transcription: 'An-Najm', audioKey: 'an_najm', label: 'Solaire (L muet + Shaddah)' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 6 : LE VOCABULAIRE & LA FUSION DE MOTS
  // ==========================================
  6: {
    worldId: 6,
    title: 'Monde 6 : Le Vocabulaire & Mots',
    titleAr: 'تَرْكِيبُ الكَلِمَاتِ وَالمُفْرَدَات',
    subtitle: 'La lecture autonome et rapide de mots complets',
    icon: 'cube',
    color: '#D97706',
    summary: 'Toutes les règles précédentes s\'unissent ! On apprend à fusionner les lettres et syllabes pour lire instantanément des verbes, des objets du quotidien, des animaux et des aliments.',
    sections: [
      {
        title: '1. Fusionner les 3 lettres d\'un verbe',
        titleAr: 'تَرْكِيبُ الأَفْعَالِ الثُّلَاثِيَّة',
        content: 'Chaque lettre s\'attache et s\'articule avec sa voyelle : كَ + تَ + بَ = كَتَبَ ("Il a écrit").',
        samples: [
          { char: 'كَتَبَ', transcription: 'Kataba', audioKey: 'kataba', label: 'Il a écrit' },
          { char: 'دَرَسَ', transcription: 'Darasa', audioKey: 'darasa', label: 'Il a étudié' },
          { char: 'قَرَأَ', transcription: 'Qara\'a', audioKey: 'qaraa', label: 'Il a lu' },
          { char: 'جَلَسَ', transcription: 'Jalasa', audioKey: 'jalasa', label: 'Il s\'est assis' },
        ],
      },
      {
        title: '2. Mots de la maison et objets du quotidien',
        titleAr: 'كَلِمَاتٌ مِنَ البَيْتِ وَالمَدْرَسَة',
        content: 'Combinez les sons courts, les allongements et les arrêts nets pour lire les objets qui vous entourent :',
        samples: [
          { char: 'بَاب', transcription: 'Bāb', audioKey: 'bab', label: 'Porte' },
          { char: 'بَيْت', transcription: 'Bayt', audioKey: 'bayt', label: 'Maison' },
          { char: 'كِتَاب', transcription: 'Kitāb', audioKey: 'kitab', label: 'Livre' },
          { char: 'كُرْسِيّ', transcription: 'Kursiyy', audioKey: 'kursiy', label: 'Chaise' },
        ],
      },
      {
        title: '3. Les animaux et la nature',
        titleAr: 'الحَيَوَانَاتُ وَالطَّبِيعَة',
        content: 'Enrichissez votre vocabulaire avec les créatures et les éléments du monde :',
        samples: [
          { char: 'أَسَد', transcription: 'Asad', audioKey: 'asad', label: 'Lion' },
          { char: 'جَمَل', transcription: 'Jamal', audioKey: 'jamal', label: 'Chameau' },
          { char: 'شَمْس', transcription: 'Shams', audioKey: 'shams', label: 'Soleil' },
          { char: 'بَحْر', transcription: 'Baḥr', audioKey: 'bahr', label: 'Mer' },
        ],
      },
    ],
  },

  // ==========================================
  // MONDE 7 : PHRASES, DIALOGUES & LECTURE FLUIDE
  // ==========================================
  7: {
    worldId: 7,
    title: 'Monde 7 : Phrases & Textes Courts',
    titleAr: 'قِرَاءَةُ الجُمَلِ وَالنُّصُوصِ القَصِيرَة',
    subtitle: 'L\'accès à la lecture fluide et à la compréhension',
    icon: 'reader',
    color: '#E11D48',
    summary: 'Le sommet de l\'apprentissage ! Vous lisez maintenant de vraies phrases complètes, des descriptions, des expressions de politesse et des mini-histoires en arabe.',
    sections: [
      {
        title: '1. La Phrase Nominale (Sujet + Description)',
        titleAr: 'الجُمْلَةُ الاسْمِيَّةُ ( مُبْتَدَأ + خَبَر )',
        content: 'En arabe, une phrase nominale relie directement un nom et son adjectif ou son état, sans besoin du verbe "être" au présent !',
        tip: '💡 Exemple : البَيْتُ كَبِيرٌ = "La maison est grande" ! Les deux mots prennent généralement la Damma finale.',
        samples: [
          { char: 'البَيْتُ كَبِيرٌ', transcription: 'Al-baytu kabeerun', audioKey: 'albayt_kabeer', label: 'La maison est grande' },
          { char: 'المَاءُ بَارِدٌ', transcription: 'Al-mā\'u bāridun', audioKey: 'almaa_baarid', label: 'L\'eau est fraîche' },
          { char: 'الكِتَابُ مُفِيدٌ', transcription: 'Al-kitābu mufeedun', audioKey: 'alkitaab_mufeed', label: 'Le livre est utile' },
          { char: 'الشَّمْسُ مُشْرِقَةٌ', transcription: 'Ash-shamsu mushriqatun', audioKey: 'ashshams_mushriqa', label: 'Le soleil brille' },
        ],
      },
      {
        title: '2. La Phrase Verbale (Action + Sujet + Objet)',
        titleAr: 'الجُمْلَةُ الفِعْلِيَّةُ ( فِعْل + فَاعِل + مَفْعُول )',
        content: 'La phrase commence par le verbe d\'action, suivi de la personne qui fait l\'action, puis de l\'objet :',
        samples: [
          { char: 'كَتَبَ الوَلَدُ', transcription: 'Kataba al-waladu', audioKey: 'kataba_alwalad', label: 'L\'enfant a écrit' },
          { char: 'قَرَأَ الوَلَدُ الكِتَابَ', transcription: 'Qara\'a al-waladu al-kitāba', audioKey: 'qaraa_alwalad_alkitaab', label: 'L\'enfant a lu le livre' },
          { char: 'شَرِبَ الطِّفْلُ الحَلِيبَ', transcription: 'Shariba aṭ-ṭiflu al-ḥaleeba', audioKey: 'shariba_attifl_alhaleeb', label: 'L\'enfant a bu le lait' },
          { char: 'فَتَحَ الأَبُ البَابَ', transcription: 'Fataḥa al-abu al-bāba', audioKey: 'fataha_alab_albaab', label: 'Le père a ouvert la porte' },
        ],
      },
      {
        title: '3. Les Formules de Politesse & Expressions',
        titleAr: 'التَّحِيَّاتُ وَآدَابُ التَّحَدُّث',
        content: 'Les phrases et salutations chaleureuses indispensables du monde arabe :',
        samples: [
          { char: 'السَّلَامُ عَلَيْكُمْ', transcription: 'As-salāmu \'alaykum', audioKey: 'assalamu_alaykum', label: 'Que la paix soit sur vous' },
          { char: 'أَهْلًا وَسَهْلًا', transcription: 'Ahlan wa sahlan', audioKey: 'ahlan_wa_sahlan', label: 'Bienvenue' },
          { char: 'شُكْرًا جَزِيلًا', transcription: 'Shukran jazeelan', audioKey: 'shukran_jazeelan', label: 'Merci beaucoup' },
          { char: 'صَبَاحُ الخَيْرِ', transcription: 'Ṣabāḥu al-khayri', audioKey: 'sabahu_alkhayr', label: 'Bonjour' },
        ],
      },
    ],
  },
};
