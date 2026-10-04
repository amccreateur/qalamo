import json

lessons_fr = {
  1: {
    "worldId": 1,
    "title": "Monde 1 : L'Alphabet & les 28 Sons",
    "titleAr": "حُرُوفُ الهِجَاءِ وَأَصْوَاتُهَا",
    "subtitle": "Les fondations de la lecture arabe",
    "icon": "text",
    "color": "#3B82F6",
    "summary": "L'alphabet arabe compte 28 lettres fondamentales. L'arabe se lit et s'écrit de droite à gauche (RTL). Chaque lettre possède un son unique et précis.",
    "sections": [
      {
        "title": "1. Les 28 Lettres de l'Alphabet",
        "titleAr": "حُرُوفُ الهِجَاءِ الثَّمَانِيَة وَالعِشْرُون",
        "content": "Touchez chaque lettre pour écouter sa prononciation. L'alphabet arabe se lit de droite à gauche et compte 28 lettres consonantiques.",
        "tip": "💡 Astuce : Entraînez-vous à écouter et répéter chaque lettre à voix haute !",
        "samples": [
          { "char": "أ", "transcription": "Alif", "audioKey": "alif", "label": "Alif" },
          { "char": "ب", "transcription": "Bā'", "audioKey": "ba", "label": "Bā'" },
          { "char": "ت", "transcription": "Tā'", "audioKey": "ta", "label": "Tā'" },
          { "char": "ث", "transcription": "Thā'", "audioKey": "tha", "label": "Thā' (langue entre dents)" },
          { "char": "ج", "transcription": "Jeem", "audioKey": "jeem", "label": "Jeem" },
          { "char": "ح", "transcription": "Ḥā'", "audioKey": "hha", "label": "Ḥā' (gorge profonde)" },
          { "char": "خ", "transcription": "Khā'", "audioKey": "kha", "label": "Khā' (raclement)" },
          { "char": "د", "transcription": "Dāl", "audioKey": "dal", "label": "Dāl" },
          { "char": "ذ", "transcription": "Dhāl", "audioKey": "dhal", "label": "Dhāl (langue entre dents)" },
          { "char": "ر", "transcription": "Rā'", "audioKey": "ra", "label": "Rā' (roulé)" },
          { "char": "ز", "transcription": "Zāy", "audioKey": "zay", "label": "Zāy" },
          { "char": "س", "transcription": "Seen", "audioKey": "seen", "label": "Seen (fin)" },
          { "char": "ش", "transcription": "Sheen", "audioKey": "sheen", "label": "Sheen" },
          { "char": "ص", "transcription": "Ṣād", "audioKey": "sad", "label": "Ṣād (emphatique)" },
          { "char": "ض", "transcription": "Ḍād", "audioKey": "dad", "label": "Ḍād (emphatique)" },
          { "char": "ط", "transcription": "Ṭā'", "audioKey": "ttaa", "label": "Ṭā' (emphatique)" },
          { "char": "ظ", "transcription": "Ẓā'", "audioKey": "zha", "label": "Ẓā' (emphatique)" },
          { "char": "ع", "transcription": "ʿAyn", "audioKey": "ayn", "label": "ʿAyn (gorge)" },
          { "char": "غ", "transcription": "Ghayn", "audioKey": "ghayn", "label": "Ghayn (gutturale)" },
          { "char": "ف", "transcription": "Fā'", "audioKey": "fa", "label": "Fā'" },
          { "char": "ق", "transcription": "Qāf", "audioKey": "qaf", "label": "Qāf (fond du palais)" },
          { "char": "ك", "transcription": "Kāf", "audioKey": "kaf", "label": "Kāf (fin)" },
          { "char": "ل", "transcription": "Lām", "audioKey": "lam", "label": "Lām" },
          { "char": "م", "transcription": "Meem", "audioKey": "meem", "label": "Meem" },
          { "char": "ن", "transcription": "Noon", "audioKey": "noon", "label": "Noon" },
          { "char": "ه", "transcription": "Hā'", "audioKey": "haa", "label": "Hā' (souffle doux)" },
          { "char": "و", "transcription": "Wāw", "audioKey": "waw", "label": "Wāw" },
          { "char": "ي", "transcription": "Yā'", "audioKey": "yaa", "label": "Yā'" }
        ]
      },
      {
        "title": "2. Les Sons de la Gorge (Ḥa, ʿAyn, Kha, Ghayn, Qaf)",
        "titleAr": "حُرُوفُ الحَلْقِ وَمَخَارِجُهَا",
        "content": "Ces 5 lettres n'existent pas en français standard. Voici les astuces pour les sortir facilement :\n\n• Ḥa (ح) : \"La buée\" → Ouvrez la gorge et soufflez chaudement comme pour faire de la buée sur un miroir ou des lunettes.\n• ʿAyn (ع) : \"Le bâtonnet\" → Serrez légèrement le milieu de la gorge, comme quand le médecin appuie sur votre langue et dit \"Aaaah\".\n• Kha (خ) : \"Le raclement\" → Faites vibrer le haut du palais, comme la \"jota\" espagnole (Juan) ou le \"ch\" du compositeur Bach.\n• Ghayn (غ) : \"Le gargarisme\" → C'est exactement le son produit quand on se gargarise avec de l'eau au fond de la gorge (un \"R\" très gras).\n• Qaf (ق) : \"Le K profond\" → Bloquez l'air tout au fond de la luette et relâchez sèchement (plus profond que le K français).",
        "tip": "💡 Conseil d'entraînement : Posez 2 doigts sur votre cou pour sentir les vibrations dans la gorge.",
        "samples": [
          { "char": "ح", "transcription": "Ḥā' (Buée)", "audioKey": "hha", "label": "Souffle chaud sur vitre" },
          { "char": "ع", "transcription": "ʿAyn (Gorge)", "audioKey": "ayn", "label": "Contraction milieu gorge" },
          { "char": "خ", "transcription": "Khā' (Râpé)", "audioKey": "kha", "label": "Raclement type \"Bach\"" },
          { "char": "غ", "transcription": "Ghayn (Gras)", "audioKey": "ghayn", "label": "Comme un gargarisme" },
          { "char": "ق", "transcription": "Qāf (Profond)", "audioKey": "qaf", "label": "K sec au fond du palais" }
        ]
      },
      {
        "title": "3. Les 3 Lettres \"Langue entre les Dents\" (Interdentales)",
        "titleAr": "الحُرُوفُ اللِّثَوِيَّة ( ث ، ذ ، ظ )",
        "content": "Pour ces 3 lettres, posez délicatement le bout de votre langue entre les incisives du haut et du bas (sans mordre !) :\n\n• Tha (ث) : Comme le \"th\" anglais de \"think\" (air qui siffle doucement).\n• Dhal (ذ) : Comme le \"th\" anglais de \"this\" ou \"the\" (avec la voix qui vibre).\n• Ẓa (ظ) : La version lourde et puissante de Dhal (la langue entre les dents + la bouche remplie d'air).",
        "tip": "💡 Regardez-vous dans un miroir : le bout de la langue doit dépasser de 2 millimètres.",
        "samples": [
          { "char": "ث", "transcription": "Thā'", "audioKey": "tha", "label": "Comme \"think\" (langue)" },
          { "char": "ذ", "transcription": "Dhāl", "audioKey": "dhal", "label": "Comme \"this\" (langue)" },
          { "char": "ظ", "transcription": "Ẓā'", "audioKey": "zha", "label": "Langue + bouche pleine" }
        ]
      },
      {
        "title": "4. Lettres Simples (Mince) vs Emphatiques (Bouche Pleine)",
        "titleAr": "الحُرُوفُ المُرَقَّقَة وَالمُفَخَّمَة ( التَّفْخِيم )",
        "content": "En arabe, 4 consonnes changent complètement selon l'ouverture de la bouche :\n\n• Mince (Muraqqaq) : On sourit légèrement, le son est fin et aigu.\n• Emphatique (Mufakhkham) : On arrondit l'intérieur de la bouche comme pour retenir une gorgée d'air, le son devient grave et puissant.",
        "tip": "💡 Écoutez attentivement la différence de profondeur entre chaque paire ci-dessous :",
        "samples": [
          { "char": "س", "transcription": "Seen (Fin)", "audioKey": "seen", "label": "Souriant (\"serpent\")" },
          { "char": "ص", "transcription": "Ṣād (Lourd)", "audioKey": "sad", "label": "Bouche pleine d'air" },
          { "char": "ت", "transcription": "Tā' (Fin)", "audioKey": "ta", "label": "Doux (\"tasse\")" },
          { "char": "ط", "transcription": "Ṭā' (Lourd)", "audioKey": "ttaa", "label": "Claquant et puissant" },
          { "char": "د", "transcription": "Dāl (Fin)", "audioKey": "dal", "label": "Doux (\"dune\")" },
          { "char": "ض", "transcription": "Ḍād (Lourd)", "audioKey": "dad", "label": "Molaires + bouche ronde" }
        ]
      },
      {
        "title": "5. Reconnaître les lettres par leurs points",
        "titleAr": "تَمْيِيزُ الحُرُوفِ بِالنِّقَاط",
        "content": "Plusieurs lettres partagent le même corps de base (le \"bateau\" ou la \"boucle\"). Seul le nombre et la position des points permettent de les distinguer :",
        "tip": "💡 Mnémonique : 1 point en bas = Ba (ب) | 2 points en haut = Ta (ت) | 3 points en haut = Tha (ث) | 1 point au ventre = Jeem (ج) | 1 point sur la tête = Kha (خ).",
        "samples": [
          { "char": "ب", "transcription": "Ba", "audioKey": "ba", "label": "1 point en bas" },
          { "char": "ت", "transcription": "Ta", "audioKey": "ta", "label": "2 points en haut" },
          { "char": "ث", "transcription": "Tha", "audioKey": "tha", "label": "3 points en haut" },
          { "char": "ج", "transcription": "Jeem", "audioKey": "jeem", "label": "Point au ventre" },
          { "char": "ح", "transcription": "Ḥa", "audioKey": "hha", "label": "Sans point (gorge)" },
          { "char": "خ", "transcription": "Kha", "audioKey": "kha", "label": "Point au-dessus" }
        ]
      }
    ]
  },
  2: {
    "worldId": 2,
    "title": "Monde 2 : Les Formes des Lettres",
    "titleAr": "أَشْكَالُ الحُرُوفِ فِي الكَلِمَة",
    "subtitle": "Comment les 28 lettres s'attachent pour former des mots",
    "icon": "shapes",
    "color": "#8B5CF6",
    "summary": "L'arabe est une écriture cursive (attachée). Comme les enfants qui se donnent la main, chaque lettre tend un bras selon sa position : au Début, au Milieu ou à la Fin du mot.",
    "sections": [
      {
        "title": "1. Les 6 Lettres Rebelles (أ د ذ ر ز و)",
        "titleAr": "الحُرُوفُ الرَّافِضَة ( أ ، د ، ذ ، ر ، ز ، و )",
        "content": "Règle absolue : ces 6 lettres ne s'attachent JAMAIS à gauche. La lettre qui suit doit redémarrer sous sa forme isolée ou initiale !",
        "tip": "💡 Retiens bien les 6 rebelles : Alif (أ), Dal (د), Dhal (ذ), Ra (ر), Zay (ز), Waw (و).",
        "samples": [
          { "char": "أ", "transcription": "Alif", "audioKey": "alif", "label": "Ne s'attache pas à gauche" },
          { "char": "د", "transcription": "Dal", "audioKey": "dal", "label": "Ne s'attache pas à gauche" },
          { "char": "ذ", "transcription": "Dhal", "audioKey": "dhal", "label": "Ne s'attache pas à gauche" },
          { "char": "ر", "transcription": "Ra", "audioKey": "ra", "label": "Ne s'attache pas à gauche" },
          { "char": "ز", "transcription": "Zay", "audioKey": "zay", "label": "Ne s'attache pas à gauche" },
          { "char": "و", "transcription": "Waw", "audioKey": "waw", "label": "Ne s'attache pas à gauche" }
        ]
      },
      {
        "title": "2. Forme Initiale (Au Début du mot)",
        "titleAr": "الحُرُوفُ فِي أَوَّلِ الكَلِمَة",
        "content": "Au début d'un mot, la lettre coupe sa queue finale et tend son bras gauche pour attraper la suivante.",
        "samples": [
          { "char": "بـ", "transcription": "B-", "audioKey": "ba", "label": "Ba initial" },
          { "char": "تـ", "transcription": "T-", "audioKey": "ta", "label": "Ta initial" },
          { "char": "جـ", "transcription": "J-", "audioKey": "jeem", "label": "Jeem initial" },
          { "char": "سـ", "transcription": "S-", "audioKey": "seen", "label": "Seen initial" },
          { "char": "عـ", "transcription": "ʿ-", "audioKey": "ayn", "label": "Ayn initial" },
          { "char": "مـ", "transcription": "M-", "audioKey": "meem", "label": "Meem initial" }
        ]
      },
      {
        "title": "3. Forme Médiane (Au Milieu du mot)",
        "titleAr": "الحُرُوفُ فِي وَسَطِ الكَلِمَة",
        "content": "Au milieu d'un mot, la lettre tend ses deux bras (à droite et à gauche) pour relier ses voisines.",
        "samples": [
          { "char": "ـبـ", "transcription": "-B-", "audioKey": "ba", "label": "Ba médian" },
          { "char": "ـتـ", "transcription": "-T-", "audioKey": "ta", "label": "Ta médian" },
          { "char": "ـجـ", "transcription": "-J-", "audioKey": "jeem", "label": "Jeem médian" },
          { "char": "ـسـ", "transcription": "-S-", "audioKey": "seen", "label": "Seen médian" },
          { "char": "ـعـ", "transcription": "-ʿ-", "audioKey": "ayn", "label": "Ayn médian" },
          { "char": "ـمـ", "transcription": "-M-", "audioKey": "meem", "label": "Meem médian" }
        ]
      },
      {
        "title": "4. Forme Finale (À la Fin du mot)",
        "titleAr": "الحُرُوفُ فِي آخِرِ الكَلِمَة",
        "content": "À la fin d'un mot, la lettre reprend sa queue d'origine pour clore élégamment le mot.",
        "samples": [
          { "char": "ـب", "transcription": "-B", "audioKey": "ba", "label": "Ba final" },
          { "char": "ـت", "transcription": "-T", "audioKey": "ta", "label": "Ta final" },
          { "char": "ـج", "transcription": "-J", "audioKey": "jeem", "label": "Jeem final" },
          { "char": "ـس", "transcription": "-S", "audioKey": "seen", "label": "Seen final" },
          { "char": "ـع", "transcription": "-ʿ", "audioKey": "ayn", "label": "Ayn final" },
          { "char": "ـم", "transcription": "-M", "audioKey": "meem", "label": "Meem final" }
        ]
      }
    ]
  },
  3: {
    "worldId": 3,
    "title": "Monde 3 : Les Voyelles Courtes (Harakāt)",
    "titleAr": "الحَرَكَاتُ القَصِيرَة : الفَتْحَة وَالضَّمَّة وَالكَسْرَة",
    "subtitle": "Donner vie aux consonnes en 1 temps sec",
    "icon": "volume-high",
    "color": "#10B981",
    "summary": "Les lettres arabes sont des consonnes. Pour les vocaliser, on leur ajoute des voyelles courtes (Harakāt). Ces voyelles sont courtes, nettes et durent exactement 1 temps (~250ms).",
    "sections": [
      {
        "title": "1. La Fatḥah (ـَ) : Le Son \"A\"",
        "titleAr": "الفَتْحَة ( ـَ )",
        "content": "Un petit trait au-dessus de la lettre. On ouvre la bouche pour produire un \"A\" clair et bref.",
        "samples": [
          { "char": "بَ", "transcription": "Ba", "audioKey": "ba_fatha", "label": "B + A" },
          { "char": "تَ", "transcription": "Ta", "audioKey": "ta_fatha", "label": "T + A" },
          { "char": "دَ", "transcription": "Da", "audioKey": "da_fatha", "label": "D + A" },
          { "char": "سَ", "transcription": "Sa", "audioKey": "sa_fatha", "label": "S + A" }
        ]
      },
      {
        "title": "2. La Ḍammah (ـُ) : Le Son \"OU\"",
        "titleAr": "الضَّمَّة ( ـُ )",
        "content": "Un petit \"9\" au-dessus de la lettre. On arrondit les lèvres pour produire un \"OU\" court.",
        "samples": [
          { "char": "بُ", "transcription": "Bou", "audioKey": "bu_damma", "label": "B + OU" },
          { "char": "تُ", "transcription": "Tou", "audioKey": "tu_damma", "label": "T + OU" },
          { "char": "دُ", "transcription": "Dou", "audioKey": "du_damma", "label": "D + OU" },
          { "char": "مُ", "transcription": "Mou", "audioKey": "mu_damma", "label": "M + OU" }
        ]
      },
      {
        "title": "3. La Kasrah (ـِ) : Le Son \"I\"",
        "titleAr": "الكَسْرَة ( ـِ )",
        "content": "Un petit trait en dessous de la lettre. On sourit légèrement pour produire un \"I\" net.",
        "samples": [
          { "char": "بِ", "transcription": "Bi", "audioKey": "bi_kasra", "label": "B + I" },
          { "char": "تِ", "transcription": "Ti", "audioKey": "ti_kasra", "label": "T + I" },
          { "char": "دِ", "transcription": "Di", "audioKey": "di_kasra", "label": "D + I" },
          { "char": "رِ", "transcription": "Ri", "audioKey": "ri_kasra", "label": "R + I" }
        ]
      }
    ]
  },
  4: {
    "worldId": 4,
    "title": "Monde 4 : Combinaisons de 2 Voyelles",
    "titleAr": "العالم الرابع : تَرْكِيبُ الحَرَكَاتِ الثُّنَائِيَّة",
    "subtitle": "L'enchaînement fluide de deux voyelles courtes consécutives sur les 28 lettres",
    "icon": "layers",
    "color": "#F59E0B",
    "summary": "Après avoir maîtrisé les voyelles isolées, entraîne ton oreille et ta voix à enchaîner deux syllabes vocalisées consécutives sans saccade, sur les lettres simples et emphatiques.",
    "sections": [
      {
        "title": "1. Le Principe d'Enchaînement à 2 Voyelles",
        "titleAr": "مَبْدَأُ تَرْكِيبِ الحَرَكَتَيْن",
        "content": "Pour lire couramment, on lie deux consonnes vocalisées dans le même souffle.\n\nChaque voyelle dure exactement 1 temps sec (~250ms) sans pause ni traînée :\n\n• صَ + دَ = صَدَ (Ṣād Emphatique)\n• ضَ + رُ = ضَرُ (Ḍād Emphatique)\n• طُ + بِ = طُبِ (Ṭā' Emphatique)\n• كُ + تِ = كُتِ (Kāf Fin)",
        "tip": "💡 Règle d'or : Garde un rythme régulier de métronome (tac-tac), en donnant la même durée à chaque syllabe !"
      },
      {
        "title": "2. Série A + A & A + OU (Emphatiques & Ouvertures)",
        "titleAr": "الفَتْحَة مَعَ الفَتْحَة وَالضَّمَّة",
        "content": "Travaillez la résonance des consonnes emphatiques et simples avec une belle ouverture vocale :",
        "samples": [
          { "char": "صَدَ", "transcription": "صَ + دَ", "audioKey": "sada", "label": "Ṣād Emphatique" },
          { "char": "طَلَ", "transcription": "طَ + لَ", "audioKey": "tala", "label": "Ṭā' Emphatique" },
          { "char": "غَفَ", "transcription": "غَ + فَ", "audioKey": "ghafa", "label": "Ghayn Emphatique" },
          { "char": "خَلَ", "transcription": "خَ + لَ", "audioKey": "khala", "label": "Khā' Emphatique" },
          { "char": "ضَرُ", "transcription": "ضَ + رُ", "audioKey": "daru_emph", "label": "Ḍād Emphatique" },
          { "char": "ظَفُ", "transcription": "ظَ + فُ", "audioKey": "zhafu", "label": "Ẓā' Emphatique" },
          { "char": "قَتُ", "transcription": "قَ + تُ", "audioKey": "qatu", "label": "Qāf Emphatique" },
          { "char": "حَسُ", "transcription": "حَ + سُ", "audioKey": "hasu", "label": "Ḥā' de gorge" },
          { "char": "بَتَ", "transcription": "بَ + تَ", "audioKey": "bata", "label": "Fatḥah + Fatḥah" }
        ]
      },
      {
        "title": "3. Série OU + I & OU + A (Emphatiques & Pronoms)",
        "titleAr": "الضَّمَّة مَعَ الكَسْرَة وَالفَتْحَة",
        "content": "Arrondissez bien les lèvres sur la première consonne (Ḍammah) puis enchaînez précisément vers la Kasrah ou Fatḥah :",
        "samples": [
          { "char": "صُرِ", "transcription": "صُ + رِ", "audioKey": "suri_emph", "label": "Ṣād Emphatique" },
          { "char": "ضُرِ", "transcription": "ضُ + رِ", "audioKey": "duri_emph", "label": "Ḍād Emphatique" },
          { "char": "طُبِ", "transcription": "طُ + بِ", "audioKey": "tubi", "label": "Ṭā' Emphatique" },
          { "char": "ظُلِ", "transcription": "ظُ + لِ", "audioKey": "zhuli", "label": "Ẓā' Emphatique" },
          { "char": "قُرِ", "transcription": "قُ + رِ", "audioKey": "quri", "label": "Qāf Emphatique" },
          { "char": "غُفِ", "transcription": "غُ + فِ", "audioKey": "ghufi", "label": "Ghayn Emphatique" },
          { "char": "خُلِ", "transcription": "خُ + لِ", "audioKey": "khuli", "label": "Khā' Emphatique" },
          { "char": "حُمِ", "transcription": "حُ + مِ", "audioKey": "humi", "label": "Ḥā' de la gorge" },
          { "char": "ثُبِ", "transcription": "ثُ + بِ", "audioKey": "thubi", "label": "Thā' Interdentale" },
          { "char": "هُوَ", "transcription": "هُ + وَ", "audioKey": "huwa", "label": "Pronom \"Il\"" },
          { "char": "رُبَ", "transcription": "رُ + بَ", "audioKey": "ruba", "label": "Mot \"Peut-être\"" }
        ]
      }
    ]
  },
  5: {
    "worldId": 5,
    "title": "Monde 5 : Sukūn & Voyelles Longues (المَدّ)",
    "titleAr": "السُّكُونُ وَحُرُوفُ المَدِّ الثَّلَاثَة",
    "subtitle": "L'arrêt consonnantique vs l'allongement en 2 temps",
    "icon": "pulse",
    "color": "#06B6D4",
    "summary": "Deux notions indispensables : le Sukūn (qui stoppe net la consonne sans voyelle) et le Madd (qui étire la voyelle sur 2 temps complets, soit deux fois plus long que la Harakah).",
    "sections": [
      {
        "title": "1. Le Sukūn (ـْ) : L'arrêt net",
        "titleAr": "السُّكُون ( ـْ )",
        "content": "Le petit cercle au-dessus de la lettre indique qu'aucune voyelle n'est prononcée : la consonne se bloque net.",
        "samples": [
          { "char": "أَبْ", "transcription": "Ab", "audioKey": "ab_sukun", "label": "A + B net" },
          { "char": "قُلْ", "transcription": "Qul", "audioKey": "qul_sukun", "label": "Qu + L net" },
          { "char": "مِنْ", "transcription": "Min", "audioKey": "min_sukun", "label": "Mi + N net" },
          { "char": "قَدْ", "transcription": "Qad", "audioKey": "qad_sukun", "label": "Qa + D net" }
        ]
      },
      {
        "title": "2. Les 3 Lettres de Prolongation (Madd)",
        "titleAr": "حُرُوفُ المَدّ ( ا ، و ، ي )",
        "content": "Quand une Harakah rencontre sa lettre amie (Fatḥah + Alif, Ḍammah + Waw, Kasrah + Ya), le son devient long (2 temps bien audibles).",
        "tip": "💡 Règle d'or : 1 temps = Court (بَ = Ba) | 2 temps = Long (بَا = Bââ).",
        "samples": [
          { "char": "بَا", "transcription": "Bââ (2t)", "audioKey": "baa_long", "label": "Madd Alif (ـَا)" },
          { "char": "بُو", "transcription": "Bouu (2t)", "audioKey": "boo_long", "label": "Madd Waw (ـُو)" },
          { "char": "بِي", "transcription": "Biii (2t)", "audioKey": "bee_long", "label": "Madd Ya (ـِي)" }
        ]
      }
    ]
  },
  6: {
    "worldId": 6,
    "title": "Monde 6 : Shaddah, Tanwīn & Alif-Lām",
    "titleAr": "الشَّدَّةُ وَالتَّنْوِينُ وَلاَمُ التَّعْرِيف",
    "subtitle": "Les secrets de la lecture courante",
    "icon": "flash",
    "color": "#E11D48",
    "summary": "Trois règles majeures pour lire les mots avec précision : doubler une consonne avec la Shaddah, nasaliser avec le Tanwīn, et distinguer les lettres solaires et lunaires avec Alif-Lām (الـ).",
    "sections": [
      {
        "title": "1. La Shaddah (ـّ) : La consonne appuyée",
        "titleAr": "الشَّدَّة ( ـّ )",
        "content": "Ce signe en forme de petit \"w\" indique que la lettre est doublée : on marque une pause ferme et on appuie sur la lettre.",
        "samples": [
          { "char": "رَبَّ", "transcription": "Rabba", "audioKey": "rabba", "label": "Double B appuyé" },
          { "char": "مَدَّ", "transcription": "Madda", "audioKey": "madda", "label": "Double D appuyé" }
        ]
      },
      {
        "title": "2. Le Tanwīn : La double voyelle nasalisée (-an, -oun, -in)",
        "titleAr": "التَّنْوِين ( ـً ، ـٌ ، ـٍ )",
        "content": "Le Tanwīn ajoute le son \"N\" à la fin du nom (nunation).",
        "samples": [
          { "char": "كِتَابًا", "transcription": "Kitāban", "audioKey": "kitaban", "label": "Tanwīn Fatḥ (-an)" },
          { "char": "كِتَابٌ", "transcription": "Kitābun", "audioKey": "kitabun", "label": "Tanwīn Ḍamm (-un)" },
          { "char": "كِتَابٍ", "transcription": "Kitābin", "audioKey": "kitabin", "label": "Tanwīn Kasr (-in)" }
        ]
      }
    ]
  },
  7: {
    "worldId": 7,
    "title": "Monde 7 : Le Vocabulaire & Mots",
    "titleAr": "المُفْرَدَاتُ وَالكَلِمَات",
    "subtitle": "Lire et assembler des mots entiers du quotidien",
    "icon": "book",
    "color": "#4F46E5",
    "summary": "Mets en pratique toutes les règles apprises pour lire des verbes d'action, des noms d'objets, d'animaux et de la nature en arabe.",
    "sections": [
      {
        "title": "1. Les Verbes d'Action à 3 Lettres",
        "titleAr": "الأَفْعَالُ الثُّلَاثِيَّة",
        "content": "En arabe, la majorité des verbes de base sont formés de 3 lettres avec la Fatḥah.",
        "samples": [
          { "char": "كَتَبَ", "transcription": "Kataba", "audioKey": "kataba", "label": "Écrire" },
          { "char": "دَرَسَ", "transcription": "Darasa", "audioKey": "darasa", "label": "Étudier" },
          { "char": "قَرَأَ", "transcription": "Qara'a", "audioKey": "qaraa", "label": "Lire" },
          { "char": "رَسَمَ", "transcription": "Rasama", "audioKey": "rasama", "label": "Dessiner" }
        ]
      }
    ]
  },
  8: {
    "worldId": 8,
    "title": "Monde 8 : Phrases & Textes Courts",
    "titleAr": "الجُمَلُ وَالنُّصُوصُ القَصِيرَة",
    "subtitle": "La lecture fluide et courante en arabe",
    "icon": "trophy",
    "color": "#D97706",
    "summary": "Le couronnement de ton apprentissage : lis des phrases complètes, comprends les liaisons (Hamzat al-Wasl), et gagne en vitesse et en fluidité.",
    "sections": [
      {
        "title": "1. Les Phrases Nominales (Sujet + Description)",
        "titleAr": "الجُمْلَةُ الاسْمِيَّة",
        "content": "Une phrase nominale commence par un nom et décrit son état ou sa qualité.",
        "samples": [
          { "char": "البَيْتُ كَبِيرٌ", "transcription": "Al-baytu kabeerun", "audioKey": "albayt_kabeer", "label": "La maison est grande" },
          { "char": "المَاءُ بَارِدٌ", "transcription": "Al-mā'u bāridun", "audioKey": "almaa_baarid", "label": "L'eau est fraîche" }
        ]
      }
    ]
  }
}

lessons_en = {
  1: {
    "worldId": 1,
    "title": "World 1: The Alphabet & 28 Sounds",
    "titleAr": "حُرُوفُ الهِجَاءِ وَأَصْوَاتُهَا",
    "subtitle": "The foundations of Arabic reading",
    "icon": "text",
    "color": "#3B82F6",
    "summary": "The Arabic alphabet consists of 28 fundamental letters. Arabic is read and written from right to left (RTL). Each letter has a unique, precise sound.",
    "sections": [
      {
        "title": "1. The 28 Letters of the Alphabet",
        "titleAr": "حُرُوفُ الهِجَاءِ الثَّمَانِيَة وَالعِشْرُون",
        "content": "Tap each letter to listen to its pronunciation. Arabic is read from right to left and has 28 consonantal letters.",
        "tip": "💡 Tip: Practice listening and repeating each letter out loud!",
        "samples": [
          { "char": "أ", "transcription": "Alif", "audioKey": "alif", "label": "Alif" },
          { "char": "ب", "transcription": "Bā'", "audioKey": "ba", "label": "Bā'" },
          { "char": "ت", "transcription": "Tā'", "audioKey": "ta", "label": "Tā'" },
          { "char": "ث", "transcription": "Thā'", "audioKey": "tha", "label": "Thā' (tongue between teeth)" },
          { "char": "ج", "transcription": "Jeem", "audioKey": "jeem", "label": "Jeem" },
          { "char": "ح", "transcription": "Ḥā'", "audioKey": "hha", "label": "Ḥā' (deep throat)" },
          { "char": "خ", "transcription": "Khā'", "audioKey": "kha", "label": "Khā' (rasping)" },
          { "char": "د", "transcription": "Dāl", "audioKey": "dal", "label": "Dāl" },
          { "char": "ذ", "transcription": "Dhāl", "audioKey": "dhal", "label": "Dhāl (tongue between teeth)" },
          { "char": "ر", "transcription": "Rā'", "audioKey": "ra", "label": "Rā' (rolled)" },
          { "char": "ز", "transcription": "Zāy", "audioKey": "zay", "label": "Zāy" },
          { "char": "س", "transcription": "Seen", "audioKey": "seen", "label": "Seen (light)" },
          { "char": "ش", "transcription": "Sheen", "audioKey": "sheen", "label": "Sheen" },
          { "char": "ص", "transcription": "Ṣād", "audioKey": "sad", "label": "Ṣād (emphatic)" },
          { "char": "ض", "transcription": "Ḍād", "audioKey": "dad", "label": "Ḍād (emphatic)" },
          { "char": "ط", "transcription": "Ṭā'", "audioKey": "ttaa", "label": "Ṭā' (emphatic)" },
          { "char": "ظ", "transcription": "Ẓā'", "audioKey": "zha", "label": "Ẓā' (emphatic)" },
          { "char": "ع", "transcription": "ʿAyn", "audioKey": "ayn", "label": "ʿAyn (throat)" },
          { "char": "غ", "transcription": "Ghayn", "audioKey": "ghayn", "label": "Ghayn (guttural)" },
          { "char": "ف", "transcription": "Fā'", "audioKey": "fa", "label": "Fā'" },
          { "char": "ق", "transcription": "Qāf", "audioKey": "qaf", "label": "Qāf (deep palate)" },
          { "char": "ك", "transcription": "Kāf", "audioKey": "kaf", "label": "Kāf (light)" },
          { "char": "ل", "transcription": "Lām", "audioKey": "lam", "label": "Lām" },
          { "char": "م", "transcription": "Meem", "audioKey": "meem", "label": "Meem" },
          { "char": "ن", "transcription": "Noon", "audioKey": "noon", "label": "Noon" },
          { "char": "ه", "transcription": "Hā'", "audioKey": "haa", "label": "Hā' (soft breath)" },
          { "char": "و", "transcription": "Wāw", "audioKey": "waw", "label": "Wāw" },
          { "char": "ي", "transcription": "Yā'", "audioKey": "yaa", "label": "Yā'" }
        ]
      },
      {
        "title": "2. Throat Letters (Ḥa, ʿAyn, Kha, Ghayn, Qaf)",
        "titleAr": "حُرُوفُ الحَلْقِ وَمَخَارِجُهَا",
        "content": "These 5 letters require special throat articulation:\n\n• Ḥa (ح): Soft friction from the middle of the throat, like breathing warm air onto glass.\n• ʿAyn (ع): Tighten the middle of the throat slightly.\n• Kha (خ): Rasping friction at the back of the palate, like the Spanish \"j\" in Juan.\n• Ghayn (غ): Like gargling with water at the back of the throat.\n• Qaf (ق): Deep \"K\" sound produced at the very back of the uvula.",
        "tip": "💡 Training tip: Place two fingers gently on your throat to feel the vibrations.",
        "samples": [
          { "char": "ح", "transcription": "Ḥā'", "audioKey": "hha", "label": "Warm breath on glass" },
          { "char": "ع", "transcription": "ʿAyn", "audioKey": "ayn", "label": "Middle throat contraction" },
          { "char": "خ", "transcription": "Khā'", "audioKey": "kha", "label": "Rasping sound" },
          { "char": "غ", "transcription": "Ghayn", "audioKey": "ghayn", "label": "Gargling sound" },
          { "char": "ق", "transcription": "Qāf", "audioKey": "qaf", "label": "Deep K at uvula" }
        ]
      },
      {
        "title": "3. Interdental Letters (Tongue Between Teeth)",
        "titleAr": "الحُرُوفُ اللِّثَوِيَّة ( ث ، ذ ، ظ )",
        "content": "For these 3 letters, place the tip of your tongue lightly between upper and lower teeth:\n\n• Tha (ث): Like the English \"th\" in \"think\".\n• Dhal (ذ): Like the English \"th\" in \"this\" or \"the\".\n• Ẓa (ظ): The deep, emphatic version of Dhal with full mouth resonance.",
        "tip": "💡 Look in a mirror: the tip of your tongue should peek out by 2 mm.",
        "samples": [
          { "char": "ث", "transcription": "Thā'", "audioKey": "tha", "label": "Like \"think\"" },
          { "char": "ذ", "transcription": "Dhāl", "audioKey": "dhal", "label": "Like \"this\"" },
          { "char": "ظ", "transcription": "Ẓā'", "audioKey": "zha", "label": "Deep tongue + full mouth" }
        ]
      },
      {
        "title": "4. Light vs Emphatic Letters",
        "titleAr": "الحُرُوفُ المُرَقَّقَة وَالمُفَخَّمَة ( التَّفْخِيم )",
        "content": "In Arabic, 4 consonants change dramatically based on mouth resonance:\n\n• Light (Muraqqaq): Slight smile, light and high-pitched.\n• Emphatic (Mufakhkham): Round the mouth cavity to create deep, powerful resonance.",
        "tip": "💡 Listen carefully to the contrast between light and heavy pairs below:",
        "samples": [
          { "char": "س", "transcription": "Seen (Light)", "audioKey": "seen", "label": "Smiling (\"snake\")" },
          { "char": "ص", "transcription": "Ṣād (Heavy)", "audioKey": "sad", "label": "Full mouth resonance" },
          { "char": "ت", "transcription": "Tā' (Light)", "audioKey": "ta", "label": "Soft (\"tea\")" },
          { "char": "ط", "transcription": "Ṭā' (Heavy)", "audioKey": "ttaa", "label": "Crisp & powerful" },
          { "char": "د", "transcription": "Dāl (Light)", "audioKey": "dal", "label": "Soft (\"door\")" },
          { "char": "ض", "transcription": "Ḍād (Heavy)", "audioKey": "dad", "label": "Deep molar pressure" }
        ]
      },
      {
        "title": "5. Recognizing Letters by Their Dots",
        "titleAr": "تَمْيِيزُ الحُرُوفِ بِالنِّقَاط",
        "content": "Many letters share the same basic body shape. The number and placement of dots make all the difference:",
        "tip": "💡 Mnemonic: 1 dot below = Ba (ب) | 2 dots above = Ta (ت) | 3 dots above = Tha (ث) | 1 dot inside = Jeem (ج) | 1 dot above = Kha (خ).",
        "samples": [
          { "char": "ب", "transcription": "Ba", "audioKey": "ba", "label": "1 dot below" },
          { "char": "ت", "transcription": "Ta", "audioKey": "ta", "label": "2 dots above" },
          { "char": "ث", "transcription": "Tha", "audioKey": "tha", "label": "3 dots above" },
          { "char": "ج", "transcription": "Jeem", "audioKey": "jeem", "label": "Dot inside belly" },
          { "char": "ح", "transcription": "Ḥa", "audioKey": "hha", "label": "No dots (throat)" },
          { "char": "خ", "transcription": "Kha", "audioKey": "kha", "label": "Dot above head" }
        ]
      }
    ]
  },
  2: {
    "worldId": 2,
    "title": "World 2: Letter Shapes & Positions",
    "titleAr": "أَشْكَالُ الحُرُوفِ فِي الكَلِمَة",
    "subtitle": "How the 28 letters connect to form words",
    "icon": "shapes",
    "color": "#8B5CF6",
    "summary": "Arabic is a cursive script. Like children holding hands, each letter reaches out an arm depending on its position: at the Beginning, in the Middle, or at the End of a word.",
    "sections": [
      {
        "title": "1. The 6 Non-Connecting Letters (أ د ذ ر ز و)",
        "titleAr": "الحُرُوفُ الرَّافِضَة ( أ ، د ، ذ ، ر ، ز ، و )",
        "content": "Golden rule: these 6 letters NEVER connect to the left. The following letter must start anew in initial shape!",
        "tip": "💡 Remember this group of 6: Alif (أ), Dal (د), Dhal (ذ), Ra (ر), Zay (ز), Waw (و).",
        "samples": [
          { "char": "أ", "transcription": "Alif", "audioKey": "alif", "label": "Does not connect to left" },
          { "char": "د", "transcription": "Dal", "audioKey": "dal", "label": "Does not connect to left" },
          { "char": "ذ", "transcription": "Dhal", "audioKey": "dhal", "label": "Does not connect to left" },
          { "char": "ر", "transcription": "Ra", "audioKey": "ra", "label": "Does not connect to left" },
          { "char": "ز", "transcription": "Zay", "audioKey": "zay", "label": "Does not connect to left" },
          { "char": "و", "transcription": "Waw", "audioKey": "waw", "label": "Does not connect to left" }
        ]
      },
      {
        "title": "2. Initial Forms (At the Beginning)",
        "titleAr": "الحُرُوفُ فِي أَوَّلِ الكَلِمَة",
        "content": "At the beginning, the letter drops its final tail and extends an arm to the left to catch the next letter.",
        "samples": [
          { "char": "بـ", "transcription": "B-", "audioKey": "ba", "label": "Ba initial" },
          { "char": "تـ", "transcription": "T-", "audioKey": "ta", "label": "Ta initial" },
          { "char": "جـ", "transcription": "J-", "audioKey": "jeem", "label": "Jeem initial" },
          { "char": "سـ", "transcription": "S-", "audioKey": "seen", "label": "Seen initial" },
          { "char": "عـ", "transcription": "ʿ-", "audioKey": "ayn", "label": "Ayn initial" },
          { "char": "مـ", "transcription": "M-", "audioKey": "meem", "label": "Meem initial" }
        ]
      },
      {
        "title": "3. Medial Forms (In the Middle)",
        "titleAr": "الحُرُوفُ فِي وَسَطِ الكَلِمَة",
        "content": "In the middle, the letter extends both arms (left and right) to bridge between neighboring letters.",
        "samples": [
          { "char": "ـبـ", "transcription": "-B-", "audioKey": "ba", "label": "Ba medial" },
          { "char": "ـتـ", "transcription": "-T-", "audioKey": "ta", "label": "Ta medial" },
          { "char": "ـجـ", "transcription": "-J-", "audioKey": "jeem", "label": "Jeem medial" },
          { "char": "ـسـ", "transcription": "-S-", "audioKey": "seen", "label": "Seen medial" },
          { "char": "ـعـ", "transcription": "-ʿ-", "audioKey": "ayn", "label": "Ayn medial" },
          { "char": "ـمـ", "transcription": "-M-", "audioKey": "meem", "label": "Meem medial" }
        ]
      },
      {
        "title": "4. Final Forms (At the End)",
        "titleAr": "الحُرُوفُ فِي آخِرِ الكَلِمَة",
        "content": "At the end of a word, the letter regains its full original tail, gracefully closing the word.",
        "samples": [
          { "char": "ـب", "transcription": "-B", "audioKey": "ba", "label": "Ba final" },
          { "char": "ـت", "transcription": "-T", "audioKey": "ta", "label": "Ta final" },
          { "char": "ـج", "transcription": "-J", "audioKey": "jeem", "label": "Jeem final" },
          { "char": "ـس", "transcription": "-S", "audioKey": "seen", "label": "Seen final" },
          { "char": "ـع", "transcription": "-ʿ", "audioKey": "ayn", "label": "Ayn final" },
          { "char": "ـم", "transcription": "-M", "audioKey": "meem", "label": "Meem final" }
        ]
      }
    ]
  },
  3: {
    "worldId": 3,
    "title": "World 3: Short Vowels (Harakāt)",
    "titleAr": "الحَرَكَاتُ القَصِيرَة : الفَتْحَة وَالضَّمَّة وَالكَسْرَة",
    "subtitle": "Bringing consonants to life in 1 quick beat",
    "icon": "volume-high",
    "color": "#10B981",
    "summary": "Arabic letters are consonants. To vocalize them, we add short vowel marks (Harakāt). These vowels are crisp, short, and last exactly 1 beat (~250ms).",
    "sections": [
      {
        "title": "1. Fatḥah (ـَ) : Open \"A\" Sound",
        "titleAr": "الفَتْحَة ( ـَ )",
        "content": "A small diagonal stroke above the letter. Open your mouth to produce a crisp, short \"A\" sound.",
        "samples": [
          { "char": "بَ", "transcription": "Ba", "audioKey": "ba_fatha", "label": "B + A" },
          { "char": "تَ", "transcription": "Ta", "audioKey": "ta_fatha", "label": "T + A" },
          { "char": "دَ", "transcription": "Da", "audioKey": "da_fatha", "label": "D + A" },
          { "char": "سَ", "transcription": "Sa", "audioKey": "sa_fatha", "label": "S + A" }
        ]
      },
      {
        "title": "2. Ḍammah (ـُ) : Rounded \"U\" Sound",
        "titleAr": "الضَّمَّة ( ـُ )",
        "content": "A tiny \"9\" mark placed above the letter. Round your lips to produce a short \"U\" (oo) sound.",
        "samples": [
          { "char": "بُ", "transcription": "Bu", "audioKey": "bu_damma", "label": "B + U" },
          { "char": "تُ", "transcription": "Tu", "audioKey": "tu_damma", "label": "T + U" },
          { "char": "دُ", "transcription": "Du", "audioKey": "du_damma", "label": "D + U" },
          { "char": "مُ", "transcription": "Mu", "audioKey": "mu_damma", "label": "M + U" }
        ]
      },
      {
        "title": "3. Kasrah (ـِ) : Smiling \"I\" Sound",
        "titleAr": "الكَسْرَة ( ـِ )",
        "content": "A small diagonal stroke under the letter. Smile slightly to produce a crisp, clear \"I\" (ee) sound.",
        "samples": [
          { "char": "بِ", "transcription": "Bi", "audioKey": "bi_kasra", "label": "B + I" },
          { "char": "تِ", "transcription": "Ti", "audioKey": "ti_kasra", "label": "T + I" },
          { "char": "دِ", "transcription": "Di", "audioKey": "di_kasra", "label": "D + I" },
          { "char": "رِ", "transcription": "Ri", "audioKey": "ri_kasra", "label": "R + I" }
        ]
      }
    ]
  },
  4: {
    "worldId": 4,
    "title": "World 4: 2-Vowel Combinations",
    "titleAr": "العالم الرابع : تَرْكِيبُ الحَرَكَاتِ الثُّنَائِيَّة",
    "subtitle": "Fluently chaining two consecutive short vowels across all 28 letters",
    "icon": "layers",
    "color": "#F59E0B",
    "summary": "After mastering isolated short vowels, train your ear and voice to chain two consecutive vocalized syllables smoothly across emphatic and standard letters.",
    "sections": [
      {
        "title": "1. The 2-Vowel Chaining Principle",
        "titleAr": "مَبْدَأُ تَرْكِيبِ الحَرَكَتَيْن",
        "content": "To read fluently, connect two vocalized consonants in one smooth breath.\n\nEach vowel lasts exactly 1 crisp beat (~250ms) without pausing or rushing:\n\n• صَ + دَ = صَدَ (Emphatic Ṣād)\n• ضَ + رُ = ضَرُ (Emphatic Ḍād)\n• طُ + بِ = طُبِ (Emphatic Ṭā')\n• كُ + تِ = كُتِ (Light Kāf)",
        "tip": "💡 Golden rule: Keep a steady metronome rhythm (tac-tac), giving equal duration to each syllable!"
      },
      {
        "title": "2. Series A + A & A + U (Emphatic & Open Sounds)",
        "titleAr": "الفَتْحَة مَعَ الفَتْحَة وَالضَّمَّة",
        "content": "Practice resonant emphatic and light consonants with dynamic openness:",
        "samples": [
          { "char": "صَدَ", "transcription": "صَ + دَ", "audioKey": "sada", "label": "Emphatic Ṣād" },
          { "char": "طَلَ", "transcription": "طَ + لَ", "audioKey": "tala", "label": "Emphatic Ṭā'" },
          { "char": "غَفَ", "transcription": "غَ + فَ", "audioKey": "ghafa", "label": "Emphatic Ghayn" },
          { "char": "خَلَ", "transcription": "خَ + لَ", "audioKey": "khala", "label": "Emphatic Khā'" },
          { "char": "ضَرُ", "transcription": "ضَ + رُ", "audioKey": "daru_emph", "label": "Emphatic Ḍād" },
          { "char": "ظَفُ", "transcription": "ظَ + فُ", "audioKey": "zhafu", "label": "Emphatic Ẓā'" },
          { "char": "قَتُ", "transcription": "قَ + تُ", "audioKey": "qatu", "label": "Emphatic Qāf" },
          { "char": "حَسُ", "transcription": "حَ + سُ", "audioKey": "hasu", "label": "Throat Ḥā'" },
          { "char": "بَتَ", "transcription": "بَ + تَ", "audioKey": "bata", "label": "Fatḥah + Fatḥah" }
        ]
      },
      {
        "title": "3. Series U + I & U + A (Emphatics & Pronouns)",
        "titleAr": "الضَّمَّة مَعَ الكَسْرَة وَالفَتْحَة",
        "content": "Round lips on the first consonant (Ḍammah) then transition accurately to Kasrah or Fatḥah:",
        "samples": [
          { "char": "صُرِ", "transcription": "صُ + رِ", "audioKey": "suri_emph", "label": "Emphatic Ṣād" },
          { "char": "ضُرِ", "transcription": "ضُ + رِ", "audioKey": "duri_emph", "label": "Emphatic Ḍād" },
          { "char": "طُبِ", "transcription": "طُ + بِ", "audioKey": "tubi", "label": "Emphatic Ṭā'" },
          { "char": "ظُلِ", "transcription": "ظُ + لِ", "audioKey": "zhuli", "label": "Emphatic Ẓā'" },
          { "char": "قُرِ", "transcription": "قُ + رِ", "audioKey": "quri", "label": "Emphatic Qāf" },
          { "char": "غُفِ", "transcription": "غُ + فِ", "audioKey": "ghufi", "label": "Emphatic Ghayn" },
          { "char": "خُلِ", "transcription": "خُ + لِ", "audioKey": "khuli", "label": "Emphatic Khā'" },
          { "char": "حُمِ", "transcription": "حُ + مِ", "audioKey": "humi", "label": "Throat Ḥā'" },
          { "char": "ثُبِ", "transcription": "ثُ + بِ", "audioKey": "thubi", "label": "Interdental Thā'" },
          { "char": "هُوَ", "transcription": "هُ + وَ", "audioKey": "huwa", "label": "Pronoun \"He\"" },
          { "char": "رُبَ", "transcription": "رُ + بَ", "audioKey": "ruba", "label": "Word \"Maybe\"" }
        ]
      }
    ]
  },
  5: {
    "worldId": 5,
    "title": "World 5: Sukūn & Long Vowels (Madd)",
    "titleAr": "السُّكُونُ وَحُرُوفُ المَدِّ الثَّلَاثَة",
    "subtitle": "Consonant stops vs 2-beat long vowel extensions",
    "icon": "pulse",
    "color": "#06B6D4",
    "summary": "Two essential rules: Sukūn (which stops the consonant clean without any vowel) and Madd (which stretches the vowel over 2 full beats, twice as long as Harakah).",
    "sections": [
      {
        "title": "1. The Sukūn (ـْ) : The Clean Stop",
        "titleAr": "السُّكُون ( ـْ )",
        "content": "The small circle above a letter indicates that no vowel is pronounced: the consonant locks cleanly.",
        "samples": [
          { "char": "أَبْ", "transcription": "Ab", "audioKey": "ab_sukun", "label": "Clean A + B" },
          { "char": "قُلْ", "transcription": "Qul", "audioKey": "qul_sukun", "label": "Clean Qu + L" },
          { "char": "مِنْ", "transcription": "Min", "audioKey": "min_sukun", "label": "Clean Mi + N" },
          { "char": "قَدْ", "transcription": "Qad", "audioKey": "qad_sukun", "label": "Clean Qa + D" }
        ]
      },
      {
        "title": "2. The 3 Long Vowels (Madd)",
        "titleAr": "حُرُوفُ المَدّ ( ا ، و ، ي )",
        "content": "When a Harakah meets its matching elongation letter (Fatḥah + Alif, Ḍammah + Waw, Kasrah + Ya), the vowel stretches to 2 full beats.",
        "tip": "💡 Golden rule: 1 beat = Short (بَ = Ba) | 2 beats = Long (بَا = Bāā).",
        "samples": [
          { "char": "بَا", "transcription": "Bāā (2t)", "audioKey": "baa_long", "label": "Madd Alif (ـَا)" },
          { "char": "بُو", "transcription": "Būū (2t)", "audioKey": "boo_long", "label": "Madd Waw (ـُو)" },
          { "char": "بِي", "transcription": "Bīī (2t)", "audioKey": "bee_long", "label": "Madd Ya (ـِي)" }
        ]
      }
    ]
  },
  6: {
    "worldId": 6,
    "title": "World 6: Shaddah, Tanwīn & Alif-Lām",
    "titleAr": "الشَّدَّةُ وَالتَّنْوِينُ وَلاَمُ التَّعْرِيف",
    "subtitle": "The keys to fluent Quranic and Arabic reading",
    "icon": "flash",
    "color": "#E11D48",
    "summary": "Three major reading rules: doubling consonants with Shaddah, nunation with Tanwīn, and distinguishing Solar vs Lunar letters with Alif-Lām (الـ).",
    "sections": [
      {
        "title": "1. The Shaddah (ـّ) : Doubled Consonant",
        "titleAr": "الشَّدَّة ( ـّ )",
        "content": "This small \"w\" mark indicates the consonant is doubled: hold a firm pause and stress the letter.",
        "samples": [
          { "char": "رَبَّ", "transcription": "Rabba", "audioKey": "rabba", "label": "Doubled stressed B" },
          { "char": "مَدَّ", "transcription": "Madda", "audioKey": "madda", "label": "Doubled stressed D" }
        ]
      },
      {
        "title": "2. Tanwīn: Double Vowel Nunation (-an, -un, -in)",
        "titleAr": "التَّنْوِين ( ـً ، ـٌ ، ـٍ )",
        "content": "Tanwīn adds an \"N\" sound to the end of indefinite nouns.",
        "samples": [
          { "char": "كِتَابًا", "transcription": "Kitāban", "audioKey": "kitaban", "label": "Tanwīn Fatḥ (-an)" },
          { "char": "كِتَابٌ", "transcription": "Kitābun", "audioKey": "kitabun", "label": "Tanwīn Ḍamm (-un)" },
          { "char": "كِتَابٍ", "transcription": "Kitābin", "audioKey": "kitabin", "label": "Tanwīn Kasr (-in)" }
        ]
      }
    ]
  },
  7: {
    "worldId": 7,
    "title": "World 7: Vocabulary & Words",
    "titleAr": "المُفْرَدَاتُ وَالكَلِمَات",
    "subtitle": "Reading and assembling complete everyday Arabic words",
    "icon": "book",
    "color": "#4F46E5",
    "summary": "Put all reading rules into practice by assembling action verbs, everyday nouns, animals, and nature words in Arabic.",
    "sections": [
      {
        "title": "1. 3-Letter Base Action Verbs",
        "titleAr": "الأَفْعَالُ الثُّلَاثِيَّة",
        "content": "In Arabic, most base verbs are composed of 3 letters with Fatḥah.",
        "samples": [
          { "char": "كَتَبَ", "transcription": "Kataba", "audioKey": "kataba", "label": "To write" },
          { "char": "دَرَسَ", "transcription": "Darasa", "audioKey": "darasa", "label": "To study" },
          { "char": "قَرَأَ", "transcription": "Qara'a", "audioKey": "qaraa", "label": "To read" },
          { "char": "رَسَمَ", "transcription": "Rasama", "audioKey": "rasama", "label": "To draw" }
        ]
      }
    ]
  },
  8: {
    "worldId": 8,
    "title": "World 8: Sentences & Short Texts",
    "titleAr": "الجُمَلُ وَالنُّصُوصُ القَصِيرَة",
    "subtitle": "Fluent reading and sentence comprehension",
    "icon": "trophy",
    "color": "#D97706",
    "summary": "The culmination of your journey: read full sentences, understand Hamzat al-Wasl connections, and build reading speed and confidence.",
    "sections": [
      {
        "title": "1. Nominal Sentences (Subject + Description)",
        "titleAr": "الجُمْلَةُ الاسْمِيَّة",
        "content": "A nominal sentence starts with a noun and describes its state or attribute.",
        "samples": [
          { "char": "البَيْتُ كَبِيرٌ", "transcription": "Al-baytu kabeerun", "audioKey": "albayt_kabeer", "label": "The house is big" },
          { "char": "المَاءُ بَارِدٌ", "transcription": "Al-mā'u bāridun", "audioKey": "almaa_baarid", "label": "The water is cold" }
        ]
      }
    ]
  }
}

ts_file = f"""export interface LessonSample {{
  char: string;
  transcription: string;
  audioKey?: string;
  audioText?: string;
  label: string;
}}

export interface LessonSection {{
  title: string;
  titleAr?: string;
  content: string;
  tip?: string;
  samples?: LessonSample[];
}}

export interface WorldLesson {{
  worldId: number;
  title: string;
  titleAr: string;
  subtitle: string;
  icon: string;
  color: string;
  summary: string;
  sections: LessonSection[];
}}

export const WORLD_LESSONS_FR: Record<number, WorldLesson> = {json.dumps(lessons_fr, ensure_ascii=False, indent=2)};

export const WORLD_LESSONS_EN: Record<number, WorldLesson> = {json.dumps(lessons_en, ensure_ascii=False, indent=2)};

export const WORLD_LESSONS = WORLD_LESSONS_FR;

export const getWorldLessons = (lang: 'fr' | 'en' = 'fr'): Record<number, WorldLesson> => {{
  return lang === 'en' ? WORLD_LESSONS_EN : WORLD_LESSONS_FR;
}};
"""

with open('src/data/lessons.ts', 'w', encoding='utf-8') as f:
    f.write(ts_file)

print("Generated clean and valid TypeScript in src/data/lessons.ts!")
