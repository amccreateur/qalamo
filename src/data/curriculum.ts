import { World } from '../types/game';

export const WORLDS: World[] = [
  {
    "id": 1,
    "name": "Monde 1 : L'Alphabet & Sons",
    "nameAr": "العالم الأول : حروف الهجاء والأصوات",
    "description": "Découvre le son authentique studio de chaque lettre de l'alphabet arabe.",
    "icon": "text",
    "color": "#3B82F6",
    "levels": [
      {
        "id": 1,
        "worldId": 1,
        "title": "Groupe 1 : أ, ب, ت, ث",
        "titleAr": "أ ، ب ، ت ، ث",
        "description": "Écoute le son et attrape la bonne lettre.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#38BDF8",
          "#3B82F6"
        ],
        "items": [
          {
            "id": "alif",
            "grapheme": "أ",
            "audioText": "أ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ت",
              "ث"
            ]
          },
          {
            "id": "ba",
            "grapheme": "ب",
            "audioText": "ب",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "أ",
              "ت",
              "ن"
            ]
          },
          {
            "id": "ta",
            "grapheme": "ت",
            "audioText": "ت",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ث",
              "ي"
            ]
          },
          {
            "id": "tha",
            "grapheme": "ث",
            "audioText": "ث",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ب",
              "ن"
            ]
          },
          {
            "id": "alif",
            "grapheme": "أ",
            "audioText": "أ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ث",
              "ب"
            ]
          },
          {
            "id": "ba",
            "grapheme": "ب",
            "audioText": "ب",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ث",
              "أ",
              "ت"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 1 : أ, ب, ت, ث",
        "descriptionEn": "Listen to the sound and catch the correct letter."
      },
      {
        "id": 2,
        "worldId": 1,
        "title": "Groupe 2 : ج, ح, خ, د",
        "titleAr": "ج ، ح ، خ ، د",
        "description": "Distingue les sons Ja, Ḥa, Kha et Da.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#34D399",
          "#059669"
        ],
        "items": [
          {
            "id": "jeem",
            "grapheme": "ج",
            "audioText": "ج",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ح",
              "خ",
              "د"
            ]
          },
          {
            "id": "hha",
            "grapheme": "ح",
            "audioText": "ح",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ج",
              "خ",
              "هـ"
            ]
          },
          {
            "id": "kha",
            "grapheme": "خ",
            "audioText": "خ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ح",
              "ج",
              "غ"
            ]
          },
          {
            "id": "dal",
            "grapheme": "د",
            "audioText": "د",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ذ",
              "ر",
              "ز"
            ]
          },
          {
            "id": "jeem",
            "grapheme": "ج",
            "audioText": "ج",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "خ",
              "ح",
              "د"
            ]
          },
          {
            "id": "hha",
            "grapheme": "ح",
            "audioText": "ح",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "د",
              "ج",
              "خ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 2 : ج, ح, خ, د",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 3,
        "worldId": 1,
        "title": "Groupe 3 : ذ, ر, ز, س",
        "titleAr": "ذ ، ر ، ز ، س",
        "description": "Écoute attentivement chaque son et attrape la bonne lettre.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#F59E0B",
          "#D97706"
        ],
        "items": [
          {
            "id": "dhal",
            "grapheme": "ذ",
            "audioText": "ذ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "د",
              "ز",
              "ر"
            ]
          },
          {
            "id": "ra",
            "grapheme": "ر",
            "audioText": "ر",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ز",
              "د",
              "و"
            ]
          },
          {
            "id": "zay",
            "grapheme": "ز",
            "audioText": "ز",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ر",
              "ذ",
              "س"
            ]
          },
          {
            "id": "seen",
            "grapheme": "س",
            "audioText": "س",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ش",
              "ص",
              "ز"
            ]
          },
          {
            "id": "ra",
            "grapheme": "ر",
            "audioText": "ر",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ذ",
              "ز",
              "س"
            ]
          },
          {
            "id": "zay",
            "grapheme": "ز",
            "audioText": "ز",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "س",
              "ر",
              "ذ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 3 : ذ, ر, ز, س",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 4,
        "worldId": 1,
        "title": "Groupe 4 : ش, ص, ض, ط",
        "titleAr": "ش ، ص ، ض ، ط",
        "description": "Reconnais les sons Sha, et les emphatiques Ṣa, Ḍa, Ṭa.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#8B5CF6",
          "#6D28D9"
        ],
        "items": [
          {
            "id": "sheen",
            "grapheme": "ش",
            "audioText": "ش",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "س",
              "ص",
              "ض"
            ]
          },
          {
            "id": "sad",
            "grapheme": "ص",
            "audioText": "ص",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "س",
              "ض",
              "ط"
            ]
          },
          {
            "id": "dad",
            "grapheme": "ض",
            "audioText": "ض",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ص",
              "د",
              "ظ"
            ]
          },
          {
            "id": "ttaa",
            "grapheme": "ط",
            "audioText": "ط",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ظ",
              "ض"
            ]
          },
          {
            "id": "sheen",
            "grapheme": "ش",
            "audioText": "ش",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ط",
              "ص",
              "س"
            ]
          },
          {
            "id": "sad",
            "grapheme": "ص",
            "audioText": "ص",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ض",
              "ش",
              "ط"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 4 : ش, ص, ض, ط",
        "descriptionEn": "Recognize the correct Arabic phrase and meaning."
      },
      {
        "id": 5,
        "worldId": 1,
        "title": "Groupe 5 : ظ, ع, غ, ف",
        "titleAr": "ظ ، ع ، غ ، ف",
        "description": "Les sons Ẓa, 'A, Gha et Fa.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#EC4899",
          "#BE185D"
        ],
        "items": [
          {
            "id": "zhaa",
            "grapheme": "ظ",
            "audioText": "ظ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ط",
              "ض",
              "ذ"
            ]
          },
          {
            "id": "ayn",
            "grapheme": "ع",
            "audioText": "ع",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غ",
              "ح",
              "أ"
            ]
          },
          {
            "id": "ghayn",
            "grapheme": "غ",
            "audioText": "غ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ع",
              "خ",
              "ف"
            ]
          },
          {
            "id": "faa",
            "grapheme": "ف",
            "audioText": "ف",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ق",
              "غ",
              "ب"
            ]
          },
          {
            "id": "ayn",
            "grapheme": "ع",
            "audioText": "ع",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ظ",
              "ف",
              "غ"
            ]
          },
          {
            "id": "ghayn",
            "grapheme": "غ",
            "audioText": "غ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ع",
              "ظ",
              "ف"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 5 : ظ, ع, غ, ف",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 6,
        "worldId": 1,
        "title": "Groupe 6 : ق, ك, ل, م",
        "titleAr": "ق ، ك ، ل ، م",
        "description": "Distingue Qa et Ka, puis La et Ma.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#06B6D4",
          "#0E7490"
        ],
        "items": [
          {
            "id": "qaf",
            "grapheme": "ق",
            "audioText": "ق",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ك",
              "ف",
              "غ"
            ]
          },
          {
            "id": "kaf",
            "grapheme": "ك",
            "audioText": "ك",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ق",
              "ل",
              "د"
            ]
          },
          {
            "id": "lam",
            "grapheme": "ل",
            "audioText": "ل",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ك",
              "أ",
              "م"
            ]
          },
          {
            "id": "meem",
            "grapheme": "م",
            "audioText": "م",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ن",
              "ل",
              "و"
            ]
          },
          {
            "id": "qaf",
            "grapheme": "ق",
            "audioText": "ق",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ل",
              "ك",
              "م"
            ]
          },
          {
            "id": "kaf",
            "grapheme": "ك",
            "audioText": "ك",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "م",
              "ق",
              "ل"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 6 : ق, ك, ل, م",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 7,
        "worldId": 1,
        "title": "Groupe 7 : ن, هـ, و, ي",
        "titleAr": "ن ، هـ ، و ، ي",
        "description": "Les sons Na, Ha, Wa et Ya.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#10B981",
          "#047857"
        ],
        "items": [
          {
            "id": "noon",
            "grapheme": "ن",
            "audioText": "ن",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ت",
              "ي"
            ]
          },
          {
            "id": "haa",
            "grapheme": "هـ",
            "audioText": "هـ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ح",
              "ع",
              "ة"
            ]
          },
          {
            "id": "waw",
            "grapheme": "و",
            "audioText": "و",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ر",
              "ز",
              "ف"
            ]
          },
          {
            "id": "yaa",
            "grapheme": "ي",
            "audioText": "ي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ن",
              "ب",
              "ت"
            ]
          },
          {
            "id": "noon",
            "grapheme": "ن",
            "audioText": "ن",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ي",
              "هـ",
              "و"
            ]
          },
          {
            "id": "yaa",
            "grapheme": "ي",
            "audioText": "ي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "هـ",
              "ن",
              "و"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Group 7 : ن, هـ, و, ي",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 8,
        "worldId": 1,
        "title": "Duel des Points : ب, ت, ث, ن, ي",
        "titleAr": "تَحَدِّي النِّقَاط : ب ، ت ، ث ، ن ، ي",
        "description": "Distingue les lettres qui partagent la même forme de bateau !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#3B82F6",
          "#1D4ED8"
        ],
        "items": [
          {
            "id": "ba",
            "grapheme": "ب",
            "audioText": "ب",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ث",
              "ن"
            ]
          },
          {
            "id": "ta",
            "grapheme": "ت",
            "audioText": "ت",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ث",
              "ي"
            ]
          },
          {
            "id": "tha",
            "grapheme": "ث",
            "audioText": "ث",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ب",
              "ن"
            ]
          },
          {
            "id": "noon",
            "grapheme": "ن",
            "audioText": "ن",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ت",
              "ي"
            ]
          },
          {
            "id": "yaa",
            "grapheme": "ي",
            "audioText": "ي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ن",
              "ب"
            ]
          },
          {
            "id": "tha",
            "grapheme": "ث",
            "audioText": "ث",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ت",
              "ن"
            ]
          },
          {
            "id": "ba",
            "grapheme": "ب",
            "audioText": "ب",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ي",
              "ث",
              "ت"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Duel des Points : ب, ت, ث, ن, ي",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 9,
        "worldId": 1,
        "title": "Duel Emphatiques & Gutturales",
        "titleAr": "تَحَدِّي الحُرُوف المُفَخَّمَة وَالحَلْقِيَّة",
        "description": "Affine ton oreille sur les sons profonds et puissants.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#059669",
          "#047857"
        ],
        "items": [
          {
            "id": "hha",
            "grapheme": "ح",
            "audioText": "ح",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "خ",
              "ع",
              "هـ"
            ]
          },
          {
            "id": "kha",
            "grapheme": "خ",
            "audioText": "خ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ح",
              "غ",
              "ق"
            ]
          },
          {
            "id": "sad",
            "grapheme": "ص",
            "audioText": "ص",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "س",
              "ض",
              "ط"
            ]
          },
          {
            "id": "ttaa",
            "grapheme": "ط",
            "audioText": "ط",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ظ",
              "ض"
            ]
          },
          {
            "id": "ayn",
            "grapheme": "ع",
            "audioText": "ع",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غ",
              "ح",
              "أ"
            ]
          },
          {
            "id": "qaf",
            "grapheme": "ق",
            "audioText": "ق",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ك",
              "غ",
              "ف"
            ]
          },
          {
            "id": "ghayn",
            "grapheme": "غ",
            "audioText": "غ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ع",
              "خ",
              "ق"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Duel Emphatiques & Gutturales",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 10,
        "worldId": 1,
        "title": "Grand Défi de l'Alphabet",
        "titleAr": "تَحَدِّي الحُرُوف الكُبْرَى (28 حَرْف)",
        "description": "Teste ta vitesse et ta maîtrise sur toutes les lettres !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#6366F1",
          "#4338CA"
        ],
        "items": [
          {
            "id": "alif",
            "grapheme": "أ",
            "audioText": "أ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ب",
              "ت",
              "ث"
            ]
          },
          {
            "id": "jeem",
            "grapheme": "ج",
            "audioText": "ج",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ح",
              "خ",
              "د"
            ]
          },
          {
            "id": "sad",
            "grapheme": "ص",
            "audioText": "ص",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "س",
              "ض",
              "ط"
            ]
          },
          {
            "id": "ttaa",
            "grapheme": "ط",
            "audioText": "ط",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ت",
              "ظ",
              "ض"
            ]
          },
          {
            "id": "ayn",
            "grapheme": "ع",
            "audioText": "ع",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غ",
              "ح",
              "أ"
            ]
          },
          {
            "id": "qaf",
            "grapheme": "ق",
            "audioText": "ق",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ك",
              "ف",
              "غ"
            ]
          },
          {
            "id": "kaf",
            "grapheme": "ك",
            "audioText": "ك",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ق",
              "ل",
              "م"
            ]
          },
          {
            "id": "meem",
            "grapheme": "م",
            "audioText": "م",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ن",
              "ل",
              "و"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Grand Challenge de l'Alphabet",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      }
    ],
    "nameEn": "World 1: The Alphabet & 28 Sounds",
    "descriptionEn": "Discover the clear studio sound of each fundamental Arabic letter."
  },
  {
    "id": 2,
    "name": "Monde 2 : Les Formes des Lettres",
    "nameAr": "العالم الثاني : أشكال الحروف ومواقعها",
    "description": "Reconnais chaque lettre selon sa position : Début, Milieu, Fin et lettres non-attachantes.",
    "icon": "shapes",
    "color": "#8B5CF6",
    "levels": [
      {
        "id": 11,
        "worldId": 2,
        "title": "Début (ـ...) : Famille Bateau & Boucles",
        "titleAr": "فِي أَوَّل الكَلِمَة - المَجْمُوعَة الأُولَى",
        "description": "Repère Ba, Ta, Tha, Jeem, Ḥa et Kha au début du mot.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#8B5CF6",
          "#6D28D9"
        ],
        "items": [
          {
            "id": "ba_init",
            "grapheme": "بـ",
            "audioText": "ب",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "تـ",
              "نـ",
              "يـ"
            ]
          },
          {
            "id": "ta_init",
            "grapheme": "تـ",
            "audioText": "ت",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "بـ",
              "ثـ",
              "نـ"
            ]
          },
          {
            "id": "tha_init",
            "grapheme": "ثـ",
            "audioText": "ث",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "تـ",
              "بـ",
              "نـ"
            ]
          },
          {
            "id": "jeem_init",
            "grapheme": "جـ",
            "audioText": "ج",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "حـ",
              "خـ",
              "د"
            ]
          },
          {
            "id": "hha_init",
            "grapheme": "حـ",
            "audioText": "ح",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "جـ",
              "خـ",
              "هـ"
            ]
          },
          {
            "id": "kha_init",
            "grapheme": "خـ",
            "audioText": "خ",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "حـ",
              "جـ",
              "غـ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Début (ـ...) : Famille Bateau & Boucles",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 12,
        "worldId": 2,
        "title": "Début (ـ...) : Sifflantes, Emphatiques & Autres",
        "titleAr": "فِي أَوَّل الكَلِمَة - المَجْمُوعَة الثَّانِيَة",
        "description": "Repère Seen, Sheen, Ṣad, Ayn, Fa, Kaf, Lam, Meem au début.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#A855F7",
          "#7E22CE"
        ],
        "items": [
          {
            "id": "seen_init",
            "grapheme": "سـ",
            "audioText": "س",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "شـ",
              "صـ",
              "ز"
            ]
          },
          {
            "id": "sheen_init",
            "grapheme": "شـ",
            "audioText": "ش",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "سـ",
              "صـ",
              "ضـ"
            ]
          },
          {
            "id": "sad_init",
            "grapheme": "صـ",
            "audioText": "ص",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "سـ",
              "ضـ",
              "طـ"
            ]
          },
          {
            "id": "ayn_init",
            "grapheme": "عـ",
            "audioText": "ع",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "غـ",
              "حـ",
              "أ"
            ]
          },
          {
            "id": "kaf_init",
            "grapheme": "كـ",
            "audioText": "ك",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "قـ",
              "لـ",
              "د"
            ]
          },
          {
            "id": "lam_init",
            "grapheme": "لـ",
            "audioText": "ل",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "كـ",
              "أ",
              "مـ"
            ]
          },
          {
            "id": "meem_init",
            "grapheme": "مـ",
            "audioText": "م",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "نـ",
              "لـ",
              "و"
            ]
          },
          {
            "id": "noon_init",
            "grapheme": "نـ",
            "audioText": "ن",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "بـ",
              "تـ",
              "يـ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Début (ـ...) : Sifflantes, Emphatiques & Autres",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 13,
        "worldId": 2,
        "title": "Milieu (ـ...ـ) : Famille Bateau & Boucles",
        "titleAr": "فِي وَسَط الكَلِمَة - المَجْمُوعَة الأُولَى",
        "description": "Repère les lettres à deux bras au milieu du mot.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#C084FC",
          "#9333EA"
        ],
        "items": [
          {
            "id": "ba_med",
            "grapheme": "ـبـ",
            "audioText": "ب",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـتـ",
              "ـثـ",
              "ـنـ"
            ]
          },
          {
            "id": "ta_med",
            "grapheme": "ـتـ",
            "audioText": "ت",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـبـ",
              "ـيـ",
              "ـثـ"
            ]
          },
          {
            "id": "tha_med",
            "grapheme": "ـثـ",
            "audioText": "ث",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـتـ",
              "ـبـ",
              "ـنـ"
            ]
          },
          {
            "id": "jeem_med",
            "grapheme": "ـجـ",
            "audioText": "ج",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـحـ",
              "ـخـ",
              "ـسـ"
            ]
          },
          {
            "id": "hha_med",
            "grapheme": "ـحـ",
            "audioText": "ح",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـجـ",
              "ـخـ",
              "ـهـ"
            ]
          },
          {
            "id": "kha_med",
            "grapheme": "ـخـ",
            "audioText": "خ",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـحـ",
              "ـغـ",
              "ـجـ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Milieu (ـ...ـ) : Famille Bateau & Boucles",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 14,
        "worldId": 2,
        "title": "Milieu (ـ...ـ) : Sifflantes, Emphatiques & Autres",
        "titleAr": "فِي وَسَط الكَلِمَة - المَجْمُوعَة الثَّانِيَة",
        "description": "Repère Seen, Sheen, Ṣad, Ayn, Kaf, Lam, Meem au milieu.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#7C3AED",
          "#5B21B6"
        ],
        "items": [
          {
            "id": "seen_med",
            "grapheme": "ـسـ",
            "audioText": "س",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـشـ",
              "ـصـ",
              "ـضـ"
            ]
          },
          {
            "id": "sheen_med",
            "grapheme": "ـشـ",
            "audioText": "ش",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـسـ",
              "ـصـ",
              "ـضـ"
            ]
          },
          {
            "id": "sad_med",
            "grapheme": "ـصـ",
            "audioText": "ص",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـضـ",
              "ـسـ",
              "ـطـ"
            ]
          },
          {
            "id": "ayn_med",
            "grapheme": "ـعـ",
            "audioText": "ع",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـغـ",
              "ـفـ",
              "ـحـ"
            ]
          },
          {
            "id": "kaf_med",
            "grapheme": "ـكـ",
            "audioText": "ك",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـقـ",
              "ـلـ",
              "ـد"
            ]
          },
          {
            "id": "lam_med",
            "grapheme": "ـلـ",
            "audioText": "ل",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـكـ",
              "ـمـ",
              "ـأ"
            ]
          },
          {
            "id": "meem_med",
            "grapheme": "ـمـ",
            "audioText": "م",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـنـ",
              "ـهـ",
              "ـلـ"
            ]
          },
          {
            "id": "yaa_med",
            "grapheme": "ـيـ",
            "audioText": "ي",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "ـبـ",
              "ـتـ",
              "ـنـ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Milieu (ـ...ـ) : Sifflantes, Emphatiques & Autres",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 15,
        "worldId": 2,
        "title": "Fin (...ـ) : Famille Bateau & Boucles",
        "titleAr": "فِي آخِر الكَلِمَة - المَجْمُوعَة الأُولَى",
        "description": "Repère les lettres qui ferment leur forme à la fin du mot.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#6366F1",
          "#4338CA"
        ],
        "items": [
          {
            "id": "ba_fin",
            "grapheme": "ـب",
            "audioText": "ب",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـت",
              "ـث",
              "ـن"
            ]
          },
          {
            "id": "ta_fin",
            "grapheme": "ـت",
            "audioText": "ت",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـب",
              "ـث",
              "ـي"
            ]
          },
          {
            "id": "tha_fin",
            "grapheme": "ـث",
            "audioText": "ث",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـت",
              "ـب",
              "ـن"
            ]
          },
          {
            "id": "jeem_fin",
            "grapheme": "ـج",
            "audioText": "ج",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـح",
              "ـخ",
              "ـد"
            ]
          },
          {
            "id": "hha_fin",
            "grapheme": "ـح",
            "audioText": "ح",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـج",
              "ـخ",
              "ـه"
            ]
          },
          {
            "id": "kha_fin",
            "grapheme": "ـخ",
            "audioText": "خ",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـح",
              "ـج",
              "ـغ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Fin (...ـ) : Famille Bateau & Boucles",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 16,
        "worldId": 2,
        "title": "Fin (...ـ) : Fermetures et Queues",
        "titleAr": "فِي آخِر الكَلِمَة - المَجْمُوعَة الثَّانِيَة",
        "description": "Repère Seen, Sheen, Ṣad, Lam, Meem, Noon, Yaa en fin de mot.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#4F46E5",
          "#3730A3"
        ],
        "items": [
          {
            "id": "seen_fin",
            "grapheme": "ـس",
            "audioText": "س",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـش",
              "ـص",
              "ـز"
            ]
          },
          {
            "id": "sheen_fin",
            "grapheme": "ـش",
            "audioText": "ش",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـس",
              "ـص",
              "ـض"
            ]
          },
          {
            "id": "sad_fin",
            "grapheme": "ـص",
            "audioText": "ص",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـض",
              "ـس",
              "ـط"
            ]
          },
          {
            "id": "lam_fin",
            "grapheme": "ـل",
            "audioText": "ل",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـك",
              "ـم",
              "ـأ"
            ]
          },
          {
            "id": "meem_fin",
            "grapheme": "ـم",
            "audioText": "م",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـن",
              "ـل",
              "ـو"
            ]
          },
          {
            "id": "noon_fin",
            "grapheme": "ـن",
            "audioText": "ن",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـب",
              "ـت",
              "ـي"
            ]
          },
          {
            "id": "yaa_fin",
            "grapheme": "ـي",
            "audioText": "ي",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "ـب",
              "ـت",
              "ـن"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Fin (...ـ) : Fermetures et Queues",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 17,
        "worldId": 2,
        "title": "Les 6 Lettres Non-Attachantes (أ د ذ ر ز و)",
        "titleAr": "الحُرُوف الرَّافِضَة ( أ ، د ، ذ ، ر ، ز ، و )",
        "description": "Ces 6 lettres ne s'attachent jamais vers la gauche !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#F59E0B",
          "#B45309"
        ],
        "items": [
          {
            "id": "alif_non",
            "grapheme": "أ",
            "audioText": "أ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بـ",
              "لـ",
              "تـ"
            ]
          },
          {
            "id": "dal_non",
            "grapheme": "د",
            "audioText": "د",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ذ",
              "ر",
              "ز"
            ]
          },
          {
            "id": "dhal_non",
            "grapheme": "ذ",
            "audioText": "ذ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "د",
              "ز",
              "ر"
            ]
          },
          {
            "id": "ra_non",
            "grapheme": "ر",
            "audioText": "ر",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ز",
              "و",
              "د"
            ]
          },
          {
            "id": "zay_non",
            "grapheme": "ز",
            "audioText": "ز",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ر",
              "د",
              "و"
            ]
          },
          {
            "id": "waw_non",
            "grapheme": "و",
            "audioText": "و",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ر",
              "ز",
              "فـ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Les 6 Lettres Non-Attachantes (أ د ذ ر ز و)",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 18,
        "worldId": 2,
        "title": "Grand Défi des Positions (Début, Milieu, Fin)",
        "titleAr": "تَحَدِّي مَوَاقِع الحُرُوف الكُبْرَى",
        "description": "Distingue instantanément la position exacte d'une lettre !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#9333EA",
          "#6B21A8"
        ],
        "items": [
          {
            "id": "ba_init",
            "grapheme": "بـ",
            "audioText": "ب",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "ـبـ",
              "ـب",
              "ب"
            ]
          },
          {
            "id": "jeem_med",
            "grapheme": "ـجـ",
            "audioText": "ج",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "جـ",
              "ـج",
              "ج"
            ]
          },
          {
            "id": "seen_fin",
            "grapheme": "ـس",
            "audioText": "س",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "سـ",
              "ـسـ",
              "س"
            ]
          },
          {
            "id": "kaf_init",
            "grapheme": "كـ",
            "audioText": "ك",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "ـكـ",
              "ـك",
              "ك"
            ]
          },
          {
            "id": "ayn_med",
            "grapheme": "ـعـ",
            "audioText": "ع",
            "phonemeDesc": "Milieu de mot",
            "transliteration": "",
            "distractors": [
              "عـ",
              "ـع",
              "ع"
            ]
          },
          {
            "id": "lam_fin",
            "grapheme": "ـل",
            "audioText": "ل",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "لـ",
              "ـلـ",
              "ل"
            ]
          },
          {
            "id": "meem_init",
            "grapheme": "مـ",
            "audioText": "م",
            "phonemeDesc": "Début de mot",
            "transliteration": "",
            "distractors": [
              "ـمـ",
              "ـم",
              "م"
            ]
          },
          {
            "id": "noon_fin",
            "grapheme": "ـن",
            "audioText": "ن",
            "phonemeDesc": "Fin de mot",
            "transliteration": "",
            "distractors": [
              "نـ",
              "ـنـ",
              "ن"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Grand Challenge des Positions (Début, Milieu, Fin)",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      }
    ],
    "nameEn": "World 2: The 4 Letter Shapes",
    "descriptionEn": "Learn the 4 positions of letters: Isolated, Initial, Medial, and Final."
  },
  {
    "id": 3,
    "name": "Monde 3 : Les Voyelles Courtes (الحركات)",
    "nameAr": "العالم الثالث : الحركات القصيرة",
    "description": "Apprends les sons produits avec la Fatḥah (A), la Ḍammah (OU) et la Kasrah (I) — 1 temps vif.",
    "icon": "volume-high",
    "color": "#10B981",
    "levels": [
      {
        "id": 19,
        "worldId": 3,
        "title": "La Fatḥah (ـَ) - Sons de base",
        "titleAr": "الفَتْحَة ( ـَ ) - الحُرُوف البَسِيطَة",
        "description": "Écoute le son ouvert \"A\".",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#38BDF8",
          "#0284C7"
        ],
        "items": [
          {
            "id": "ba_fatha",
            "grapheme": "بَ",
            "audioText": "بَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بُ",
              "بِ",
              "تَ"
            ]
          },
          {
            "id": "ta_fatha",
            "grapheme": "تَ",
            "audioText": "تَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُ",
              "تِ",
              "بَ"
            ]
          },
          {
            "id": "da_fatha",
            "grapheme": "دَ",
            "audioText": "دَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُ",
              "دِ",
              "رَ"
            ]
          },
          {
            "id": "ra_fatha",
            "grapheme": "رَ",
            "audioText": "رَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رُ",
              "رِ",
              "زَ"
            ]
          },
          {
            "id": "sa_fatha",
            "grapheme": "سَ",
            "audioText": "سَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سُ",
              "سِ",
              "شَ"
            ]
          },
          {
            "id": "ma_fatha",
            "grapheme": "مَ",
            "audioText": "مَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "مُ",
              "مِ",
              "نَ"
            ]
          },
          {
            "id": "na_fatha",
            "grapheme": "نَ",
            "audioText": "نَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "نُ",
              "نِ",
              "بَ"
            ]
          },
          {
            "id": "ya_fatha",
            "grapheme": "يَ",
            "audioText": "يَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "يُ",
              "يِ",
              "تَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Fatḥah (ـَ) : Short 'A' sound",
        "descriptionEn": "Listen to the sound and catch the correct letter."
      },
      {
        "id": 20,
        "worldId": 3,
        "title": "La Fatḥah (ـَ) - Emphatiques & Gutturales",
        "titleAr": "الفَتْحَة ( ـَ ) - الحُرُوف المُفَخَّمَة وَالحَلْقِيَّة",
        "description": "Distingue les sons ouverts puissants (Ṣa, Ḍa, Ṭa, Ẓa, 'A, Gha, Qa, Ḥa).",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#059669",
          "#047857"
        ],
        "items": [
          {
            "id": "sad_fatha",
            "grapheme": "صَ",
            "audioText": "صَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سَ",
              "ضَ",
              "طَ"
            ]
          },
          {
            "id": "dad_fatha",
            "grapheme": "ضَ",
            "audioText": "ضَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "صَ",
              "دَ",
              "ظَ"
            ]
          },
          {
            "id": "ttaa_fatha",
            "grapheme": "طَ",
            "audioText": "طَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "ظَ",
              "ضَ"
            ]
          },
          {
            "id": "zha_fatha",
            "grapheme": "ظَ",
            "audioText": "ظَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "طَ",
              "ضَ",
              "ذَ"
            ]
          },
          {
            "id": "ayn_fatha",
            "grapheme": "عَ",
            "audioText": "عَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غَ",
              "حَ",
              "أَ"
            ]
          },
          {
            "id": "ghayn_fatha",
            "grapheme": "غَ",
            "audioText": "غَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "عَ",
              "خَ",
              "فَ"
            ]
          },
          {
            "id": "qaf_fatha",
            "grapheme": "قَ",
            "audioText": "قَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كَ",
              "فَ",
              "غَ"
            ]
          },
          {
            "id": "hha_fatha",
            "grapheme": "حَ",
            "audioText": "حَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "خَ",
              "جَ",
              "هَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Fatḥah (ـَ) : Short 'A' sound",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 21,
        "worldId": 3,
        "title": "La Ḍammah (ـُ) - Sons \"OU\" de base",
        "titleAr": "الضَّمَّة ( ـُ ) - الحُرُوف البَسِيطَة",
        "description": "Écoute le son arrondi \"OU\".",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#F97316",
          "#C2410C"
        ],
        "items": [
          {
            "id": "bu_damma",
            "grapheme": "بُ",
            "audioText": "بُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "بِ",
              "تُ"
            ]
          },
          {
            "id": "tu_damma",
            "grapheme": "تُ",
            "audioText": "تُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "تِ",
              "بُ"
            ]
          },
          {
            "id": "du_damma",
            "grapheme": "دُ",
            "audioText": "دُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دَ",
              "دِ",
              "رُ"
            ]
          },
          {
            "id": "ru_damma",
            "grapheme": "رُ",
            "audioText": "رُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رَ",
              "رِ",
              "زُ"
            ]
          },
          {
            "id": "su_damma",
            "grapheme": "سُ",
            "audioText": "سُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سَ",
              "سِ",
              "صُ"
            ]
          },
          {
            "id": "mu_damma",
            "grapheme": "مُ",
            "audioText": "مُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "مَ",
              "مِ",
              "نُ"
            ]
          },
          {
            "id": "nu_damma",
            "grapheme": "نُ",
            "audioText": "نُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "نَ",
              "نِ",
              "بُ"
            ]
          },
          {
            "id": "waw_damma",
            "grapheme": "وُ",
            "audioText": "وُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَ",
              "وِ",
              "رُ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Ḍammah (ـُ) : Short 'U' sound",
        "descriptionEn": "Listen to the sound and catch the correct letter."
      },
      {
        "id": 22,
        "worldId": 3,
        "title": "La Ḍammah (ـُ) - Sons \"OU\" avancés",
        "titleAr": "الضَّمَّة ( ـُ ) - حُرُوف مُتَقَدِّمَة",
        "description": "Distingue Jou, Ṣou, Ḍou, Ṭou, Kou, Lou, Qou, 'Ou.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#EA580C",
          "#9A3412"
        ],
        "items": [
          {
            "id": "ju_damma",
            "grapheme": "جُ",
            "audioText": "جُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "حُ",
              "خُ",
              "دُ"
            ]
          },
          {
            "id": "sad_damma",
            "grapheme": "صُ",
            "audioText": "صُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سُ",
              "ضُ",
              "طُ"
            ]
          },
          {
            "id": "dad_damma",
            "grapheme": "ضُ",
            "audioText": "ضُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "صُ",
              "دُ",
              "ظُ"
            ]
          },
          {
            "id": "ttaa_damma",
            "grapheme": "طُ",
            "audioText": "طُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُ",
              "ظُ",
              "ضُ"
            ]
          },
          {
            "id": "ku_damma",
            "grapheme": "كُ",
            "audioText": "كُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قُ",
              "لُ",
              "دُ"
            ]
          },
          {
            "id": "lu_damma",
            "grapheme": "لُ",
            "audioText": "لُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كُ",
              "مُ",
              "نُ"
            ]
          },
          {
            "id": "qaf_damma",
            "grapheme": "قُ",
            "audioText": "قُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كُ",
              "فُ",
              "غُ"
            ]
          },
          {
            "id": "ayn_damma",
            "grapheme": "عُ",
            "audioText": "عُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غُ",
              "حُ",
              "أُ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Ḍammah (ـُ) : Short 'U' sound",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 23,
        "worldId": 3,
        "title": "La Kasrah (ـِ) - Sons \"I\" de base",
        "titleAr": "الكَسْرَة ( ـِ ) - الحُرُوف البَسِيطَة",
        "description": "Écoute le son tiré \"I\".",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#A855F7",
          "#7E22CE"
        ],
        "items": [
          {
            "id": "bi_kasra",
            "grapheme": "بِ",
            "audioText": "بِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "بُ",
              "تِ"
            ]
          },
          {
            "id": "ti_kasra",
            "grapheme": "تِ",
            "audioText": "تِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "تُ",
              "بِ"
            ]
          },
          {
            "id": "di_kasra",
            "grapheme": "دِ",
            "audioText": "دِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دَ",
              "دُ",
              "رِ"
            ]
          },
          {
            "id": "ri_kasra",
            "grapheme": "رِ",
            "audioText": "رِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رَ",
              "رُ",
              "زِ"
            ]
          },
          {
            "id": "si_kasra",
            "grapheme": "سِ",
            "audioText": "سِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سَ",
              "سُ",
              "شِ"
            ]
          },
          {
            "id": "mi_kasra",
            "grapheme": "مِ",
            "audioText": "مِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "مَ",
              "مُ",
              "نِ"
            ]
          },
          {
            "id": "ni_kasra",
            "grapheme": "نِ",
            "audioText": "نِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "نَ",
              "نُ",
              "بِ"
            ]
          },
          {
            "id": "yaa_kasra",
            "grapheme": "يِ",
            "audioText": "يِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "يَ",
              "يُ",
              "تِ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Kasrah (ـِ) : Short 'I' sound",
        "descriptionEn": "Listen to the sound and catch the correct letter."
      },
      {
        "id": 24,
        "worldId": 3,
        "title": "La Kasrah (ـِ) - Sons \"I\" avancés",
        "titleAr": "الكَسْرَة ( ـِ ) - حُرُوف مُتَقَدِّمَة",
        "description": "Distingue Ji, Ṣi, Ṭi, 'I, Qi, Ki, Li, Fi.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#9333EA",
          "#6B21A8"
        ],
        "items": [
          {
            "id": "jeem_kasra",
            "grapheme": "جِ",
            "audioText": "جِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "حِ",
              "خِ",
              "دِ"
            ]
          },
          {
            "id": "sad_kasra",
            "grapheme": "صِ",
            "audioText": "صِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سِ",
              "ضِ",
              "طِ"
            ]
          },
          {
            "id": "ttaa_kasra",
            "grapheme": "طِ",
            "audioText": "طِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تِ",
              "ظِ",
              "ضِ"
            ]
          },
          {
            "id": "ayn_kasra",
            "grapheme": "عِ",
            "audioText": "عِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "غِ",
              "حِ",
              "إِ"
            ]
          },
          {
            "id": "qaf_kasra",
            "grapheme": "قِ",
            "audioText": "قِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِ",
              "فِ",
              "غِ"
            ]
          },
          {
            "id": "kaf_kasra",
            "grapheme": "كِ",
            "audioText": "كِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قِ",
              "لِ",
              "دِ"
            ]
          },
          {
            "id": "lam_kasra",
            "grapheme": "لِ",
            "audioText": "لِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِ",
              "مِ",
              "نِ"
            ]
          },
          {
            "id": "fa_kasra",
            "grapheme": "فِ",
            "audioText": "فِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قِ",
              "غِ",
              "بِ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Kasrah (ـِ) : Short 'I' sound",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 25,
        "worldId": 3,
        "title": "Duel des 3 Voyelles : A vs OU vs I",
        "titleAr": "المُقَارَنَةُ بَيْنَ الحَرَكَات الثَّلَاث",
        "description": "Distingue la Fatḥah, Ḍammah et Kasrah sur une même consonne !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#EC4899",
          "#BE185D"
        ],
        "items": [
          {
            "id": "ba_fatha",
            "grapheme": "بَ",
            "audioText": "بَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بُ",
              "بِ",
              "تَ"
            ]
          },
          {
            "id": "bu_damma",
            "grapheme": "بُ",
            "audioText": "بُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "بِ",
              "تُ"
            ]
          },
          {
            "id": "bi_kasra",
            "grapheme": "بِ",
            "audioText": "بِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "بُ",
              "تِ"
            ]
          },
          {
            "id": "ta_fatha",
            "grapheme": "تَ",
            "audioText": "تَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُ",
              "تِ",
              "بَ"
            ]
          },
          {
            "id": "tu_damma",
            "grapheme": "تُ",
            "audioText": "تُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "تِ",
              "بُ"
            ]
          },
          {
            "id": "ti_kasra",
            "grapheme": "تِ",
            "audioText": "تِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "تُ",
              "بِ"
            ]
          },
          {
            "id": "da_fatha",
            "grapheme": "دَ",
            "audioText": "دَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُ",
              "دِ",
              "رَ"
            ]
          },
          {
            "id": "du_damma",
            "grapheme": "دُ",
            "audioText": "دُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دَ",
              "دِ",
              "رُ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Duel des 3 Voyelles : A vs OU vs I",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 26,
        "worldId": 3,
        "title": "Grand Défi des 3 Harakāt",
        "titleAr": "تَحَدِّي الحَرَكَات الثَّلَاث الكُبْرَى",
        "description": "Distingue instantanément Fatḥah, Ḍammah et Kasrah !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#F43F5E",
          "#BE123C"
        ],
        "items": [
          {
            "id": "ka_fatha",
            "grapheme": "كَ",
            "audioText": "كَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كُ",
              "كِ",
              "قَ"
            ]
          },
          {
            "id": "ku_damma",
            "grapheme": "كُ",
            "audioText": "كُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كَ",
              "كِ",
              "قُ"
            ]
          },
          {
            "id": "ki_kasra",
            "grapheme": "كِ",
            "audioText": "كِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كَ",
              "كُ",
              "قِ"
            ]
          },
          {
            "id": "la_fatha",
            "grapheme": "لَ",
            "audioText": "لَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "لُ",
              "لِ",
              "كَ"
            ]
          },
          {
            "id": "lu_damma",
            "grapheme": "لُ",
            "audioText": "لُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "لَ",
              "لِ",
              "مُ"
            ]
          },
          {
            "id": "li_kasra",
            "grapheme": "لِ",
            "audioText": "لِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "لَ",
              "لُ",
              "بِ"
            ]
          },
          {
            "id": "sa_fatha",
            "grapheme": "سَ",
            "audioText": "سَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سُ",
              "سِ",
              "صَ"
            ]
          },
          {
            "id": "si_kasra",
            "grapheme": "سِ",
            "audioText": "سِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سَ",
              "سُ",
              "شِ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Grand Challenge des 3 Harakāt",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      }
    ],
    "nameEn": "World 3: Short Vowels (Harakāt)",
    "descriptionEn": "Master the 3 short vowel signs: Fatḥah (A), Ḍammah (U), and Kasrah (I)."
  },
  {
    "id": 4,
    "name": "Monde 4 : Les Combinaisons de 2 Voyelles",
    "nameAr": "العالم الرابع : تَرْكِيبُ الحَرَكَاتِ الثُّنَائِيَّة",
    "description": "Enchaîne avec fluidité deux lettres portant des voyelles courtes (Fatḥah, Ḍammah, Kasrah) sur les 28 lettres et les sons emphatiques !",
    "icon": "layers",
    "color": "#F59E0B",
    "levels": [
      {
        "id": 27,
        "worldId": 4,
        "title": "Série A + A (Emphatiques & Simples)",
        "titleAr": "فَتْحَة + فَتْحَة (صَدَ ، طَلَ ، غَفَ ، خَلَ)",
        "description": "Lis et assemble tes premières combinaisons ouvertes à 2 Fatḥah !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#F59E0B",
          "#B45309"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "sada",
            "word": "صَدَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "صَ",
              "دَ"
            ],
            "distractorLetters": [
              "سَ",
              "ذَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "tala",
            "word": "طَلَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "طَ",
              "لَ"
            ],
            "distractorLetters": [
              "تَ",
              "كَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "ghafa",
            "word": "غَفَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "غَ",
              "فَ"
            ],
            "distractorLetters": [
              "عَ",
              "قَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "khala",
            "word": "خَلَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "خَ",
              "لَ"
            ],
            "distractorLetters": [
              "حَ",
              "جَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "bata",
            "word": "بَتَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "بَ",
              "تَ"
            ],
            "distractorLetters": [
              "نَ",
              "دَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "maa_particle",
            "word": "مَعَ",
            "meaning": "Avec",
            "translationFr": "Avec",
            "letters": [
              "مَ",
              "عَ"
            ],
            "distractorLetters": [
              "غَ",
              "لَ"
            ],
            "emoji": "🤝",
            "translationEn": "With"
          },
          {
            "id": "laka",
            "word": "لَكَ",
            "meaning": "Pour toi",
            "translationFr": "Pour toi",
            "letters": [
              "لَ",
              "كَ"
            ],
            "distractorLetters": [
              "بَ",
              "كُ"
            ],
            "emoji": "🎁",
            "translationEn": "For you"
          }
        ],
        "titleEn": "Series A + A (Emphatic & Simple)",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 28,
        "worldId": 4,
        "title": "Série A + OU (Emphatiques & Simples)",
        "titleAr": "فَتْحَة + ضَمَّة (ضَرُ ، ظَفُ ، قَتُ ، حَسُ)",
        "description": "Passe du son 'A' au son 'OU' avec agilité sur les sons lourds et légers !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#EA580C",
          "#9A3412"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "daru_emph",
            "word": "ضَرُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "ضَ",
              "رُ"
            ],
            "distractorLetters": [
              "دَ",
              "زُ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "zhafu",
            "word": "ظَفُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "ظَ",
              "فُ"
            ],
            "distractorLetters": [
              "طَ",
              "قُ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "qatu",
            "word": "قَتُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "قَ",
              "تُ"
            ],
            "distractorLetters": [
              "كَ",
              "تَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "hasu",
            "word": "حَسُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "حَ",
              "سُ"
            ],
            "distractorLetters": [
              "خَ",
              "صُ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "babu",
            "word": "بَبُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "بَ",
              "بُ"
            ],
            "distractorLetters": [
              "تُ",
              "بِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "nabu",
            "word": "نَبُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "نَ",
              "بُ"
            ],
            "distractorLetters": [
              "بَ",
              "نُ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "tadu",
            "word": "تَدُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "تَ",
              "دُ"
            ],
            "distractorLetters": [
              "ثَ",
              "دَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          }
        ],
        "titleEn": "Series A + U (Emphatic & Simple)",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 29,
        "worldId": 4,
        "title": "Série A + I (Gorge, Emphatiques & Sifflement)",
        "titleAr": "فَتْحَة + كَسْرَة (صَحِ ، طَفِ ، غَنِ ، خَشِ)",
        "description": "Descends vers la Kasrah après la Fatḥah !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#8B5CF6",
          "#5B21B6"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "sahi",
            "word": "صَحِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "صَ",
              "حِ"
            ],
            "distractorLetters": [
              "سَ",
              "خِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "tafi",
            "word": "طَفِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "طَ",
              "فِ"
            ],
            "distractorLetters": [
              "تَ",
              "قِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "ghani",
            "word": "غَنِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "غَ",
              "نِ"
            ],
            "distractorLetters": [
              "عَ",
              "لِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "khashi",
            "word": "خَشِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "خَ",
              "شِ"
            ],
            "distractorLetters": [
              "حَ",
              "سِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "ali_short",
            "word": "عَلِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "عَ",
              "لِ"
            ],
            "distractorLetters": [
              "غَ",
              "لَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "jali",
            "word": "جَلِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "جَ",
              "لِ"
            ],
            "distractorLetters": [
              "حَ",
              "رِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "dhari",
            "word": "ذَرِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "ذَ",
              "رِ"
            ],
            "distractorLetters": [
              "دَ",
              "زِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "zami",
            "word": "زَمِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "زَ",
              "مِ"
            ],
            "distractorLetters": [
              "رَ",
              "نِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          }
        ],
        "titleEn": "Series A + I (Throat & Emphatics)",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 30,
        "worldId": 4,
        "title": "Séries OU + I & OU + A (Emphatiques & Pronoms)",
        "titleAr": "ضَمَّة + كَسْرَة / فَتْحَة (صُرِ ، ضُرِ ، طُبِ ، ظُلِ)",
        "description": "Attrape les bulles des combinaisons débutant par le son 'OU' !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#10B981",
          "#047857"
        ],
        "items": [
          {
            "id": "suri_emph",
            "grapheme": "صُرِ",
            "audioText": "صُرِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سُرِ",
              "صَرِ",
              "صُرُ"
            ]
          },
          {
            "id": "duri_emph",
            "grapheme": "ضُرِ",
            "audioText": "ضُرِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُرِ",
              "ضَرِ",
              "ضُرُ"
            ]
          },
          {
            "id": "tubi",
            "grapheme": "طُبِ",
            "audioText": "طُبِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُبِ",
              "طَبِ",
              "طُبُ"
            ]
          },
          {
            "id": "zhuli",
            "grapheme": "ظُلِ",
            "audioText": "ظُلِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ذُلِ",
              "ظَلِ",
              "طُلِ"
            ]
          },
          {
            "id": "quri",
            "grapheme": "قُرِ",
            "audioText": "قُرِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كُرِ",
              "قَرِ",
              "قُرُ"
            ]
          },
          {
            "id": "ghufi",
            "grapheme": "غُفِ",
            "audioText": "غُفِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "عُفِ",
              "غَفِ",
              "غُفُ"
            ]
          },
          {
            "id": "khuli",
            "grapheme": "خُلِ",
            "audioText": "خُلِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "حُلِ",
              "خَلِ",
              "جُلِ"
            ]
          },
          {
            "id": "humi",
            "grapheme": "حُمِ",
            "audioText": "حُمِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "خُمِ",
              "حَمِ",
              "عُمِ"
            ]
          },
          {
            "id": "thubi",
            "grapheme": "ثُبِ",
            "audioText": "ثُبِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُبِ",
              "سُبِ",
              "ثَبِ"
            ]
          },
          {
            "id": "huwa",
            "grapheme": "هُوَ",
            "audioText": "هُوَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "هِيَ",
              "هَوَ",
              "لَكَ"
            ]
          },
          {
            "id": "ruba",
            "grapheme": "رُبَ",
            "audioText": "رُبَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رَبَ",
              "رُبُ",
              "زُبَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Series U + I & U + A (Emphatics & Pronouns)",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 31,
        "worldId": 4,
        "title": "Série I + A & Défi Discrimination Emphatique",
        "titleAr": "كَسْرَة + فَتْحَة (طِبَ ، ظِمَ ، صِفَ ، ضِعَ ، قِفَ)",
        "description": "Vise la bonne cible parmi les sons subtils et emphatiques !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [
          {
            "id": "tiba",
            "grapheme": "طِبَ",
            "audioText": "طِبَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تِبَ",
              "طُبَ",
              "طَبَ"
            ]
          },
          {
            "id": "zhima",
            "grapheme": "ظِمَ",
            "audioText": "ظِمَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "ذِمَ",
              "ظُمَ",
              "طِمَ"
            ]
          },
          {
            "id": "sifa",
            "grapheme": "صِفَ",
            "audioText": "صِفَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سِفَ",
              "صُفَ",
              "صَفَ"
            ]
          },
          {
            "id": "dia",
            "grapheme": "ضِعَ",
            "audioText": "ضِعَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دِعَ",
              "ضُعَ",
              "ضَعَ"
            ]
          },
          {
            "id": "qifa",
            "grapheme": "قِفَ",
            "audioText": "قِفَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِفَ",
              "قُفَ",
              "قَفَ"
            ]
          },
          {
            "id": "ghila",
            "grapheme": "غِلَ",
            "audioText": "غِلَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "عِلَ",
              "غُلَ",
              "غَلَ"
            ]
          },
          {
            "id": "khifa",
            "grapheme": "خِفَ",
            "audioText": "خِفَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "حِفَ",
              "خُفَ",
              "خَفَ"
            ]
          },
          {
            "id": "hiya",
            "grapheme": "هِيَ",
            "audioText": "هِيَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "هُوَ",
              "هَيَ",
              "لِمَ"
            ]
          },
          {
            "id": "lima",
            "grapheme": "لِمَ",
            "audioText": "لِمَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "لَمَ",
              "لُمَ",
              "لَكَ"
            ]
          },
          {
            "id": "bika",
            "grapheme": "بِكَ",
            "audioText": "بِكَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَكَ",
              "بُكَ",
              "بِتَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Series I + A & Discrimination Challenge",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 32,
        "worldId": 4,
        "title": "Grand Atelier des 28 Lettres & Emphatiques",
        "titleAr": "الوَرْشَةُ الكُبْرَى لِتَرْكِيبِ الحُرُوف الثَّمَانِيَة وَالعِشْرِين",
        "description": "Construis les combinaisons de voyelles mélangées pour valider ton Monde 4 !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#D97706",
          "#92400E"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "sada",
            "word": "صَدَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "صَ",
              "دَ"
            ],
            "distractorLetters": [
              "سَ",
              "ضَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "daru_emph",
            "word": "ضَرُ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "ضَ",
              "رُ"
            ],
            "distractorLetters": [
              "دَ",
              "ظُ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "tafi",
            "word": "طَفِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "طَ",
              "فِ"
            ],
            "distractorLetters": [
              "تَ",
              "قِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "zhuli",
            "word": "ظُلِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "ظُ",
              "لِ"
            ],
            "distractorLetters": [
              "طُ",
              "ذِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "quri",
            "word": "قُرِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "قُ",
              "رِ"
            ],
            "distractorLetters": [
              "كُ",
              "رَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "ghani",
            "word": "غَنِ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "غَ",
              "نِ"
            ],
            "distractorLetters": [
              "عَ",
              "مِ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "khala",
            "word": "خَلَ",
            "meaning": "",
            "translationFr": "",
            "letters": [
              "خَ",
              "لَ"
            ],
            "distractorLetters": [
              "حَ",
              "جَ"
            ],
            "emoji": "🔤",
            "translationEn": ""
          },
          {
            "id": "huwa",
            "word": "هُوَ",
            "meaning": "Il",
            "translationFr": "Il",
            "letters": [
              "هُ",
              "وَ"
            ],
            "distractorLetters": [
              "هَ",
              "وِ"
            ],
            "emoji": "👦",
            "translationEn": "He"
          },
          {
            "id": "hiya",
            "word": "هِيَ",
            "meaning": "Elle",
            "translationFr": "Elle",
            "letters": [
              "هِ",
              "يَ"
            ],
            "distractorLetters": [
              "هُ",
              "يُ"
            ],
            "emoji": "👧",
            "translationEn": "She"
          }
        ],
        "titleEn": "Grand Workshop: All 28 Letters",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      }
    ],
    "nameEn": "World 4: 2-Vowel Combinations",
    "descriptionEn": "Chain two consecutive short vowels smoothly across all 28 letters and emphatic sounds."
  },
  {
    "id": 5,
    "name": "Monde 5 : Sukūn & Voyelles Longues (المَدّ)",
    "nameAr": "العالم الخامس : السُّكُون وَحُرُوفُ المَدّ",
    "description": "Maîtrise le Sukūn (arrêt net) et allonge les sons avec Madd Alif, Waw et Ya (2 temps étirés).",
    "icon": "pulse",
    "color": "#06B6D4",
    "levels": [
      {
        "id": 33,
        "worldId": 5,
        "title": "Le Sukūn (ـْ) - Syllabes simples",
        "titleAr": "السُّكُون ( ـْ ) - المَقَاطِع البَسِيطَة",
        "description": "La consonne d'arrêt net sans voyelle.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#059669",
          "#065F46"
        ],
        "items": [
          {
            "id": "ab_sukun",
            "grapheme": "أَبْ",
            "audioText": "أَبْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "أَبَ",
              "أَبُ",
              "أَتْ"
            ]
          },
          {
            "id": "at_sukun",
            "grapheme": "أَتْ",
            "audioText": "أَتْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "أَتَ",
              "أَتُ",
              "أَبْ"
            ]
          },
          {
            "id": "bar_sukun",
            "grapheme": "بَرْ",
            "audioText": "بَرْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَرِ",
              "بَرُ",
              "بَلْ"
            ]
          },
          {
            "id": "bal_sukun",
            "grapheme": "بَلْ",
            "audioText": "بَلْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَلَ",
              "بَلُ",
              "بَرْ"
            ]
          },
          {
            "id": "min_sukun",
            "grapheme": "مِنْ",
            "audioText": "مِنْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "مَنَ",
              "مُنْ",
              "عَنْ"
            ]
          },
          {
            "id": "an_sukun",
            "grapheme": "عَنْ",
            "audioText": "عَنْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "عَنَ",
              "مِنْ",
              "إِنْ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Sukūn (ـْ) : The Consonant Stop",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 34,
        "worldId": 5,
        "title": "Le Sukūn (ـْ) - Syllabes avancées",
        "titleAr": "السُّكُون ( ـْ ) - مَقَاطِع مُتَقَدِّمَة",
        "description": "Distingue Qul, Qum, Qad, Hal, Kul, Bay, Sham, Tay.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [
          {
            "id": "qul_sukun",
            "grapheme": "قُلْ",
            "audioText": "قُلْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قُلَ",
              "قِلْ",
              "كُلْ"
            ]
          },
          {
            "id": "qum_sukun",
            "grapheme": "قُمْ",
            "audioText": "قُمْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قَمْ",
              "قِلْ",
              "كُلْ"
            ]
          },
          {
            "id": "qad_sukun",
            "grapheme": "قَدْ",
            "audioText": "قَدْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "قَدَ",
              "قُدْ",
              "كَدْ"
            ]
          },
          {
            "id": "hal_sukun",
            "grapheme": "هَلْ",
            "audioText": "هَلْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "هَلَ",
              "هِلْ",
              "بَلْ"
            ]
          },
          {
            "id": "kul_sukun",
            "grapheme": "كُلْ",
            "audioText": "كُلْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كَلْ",
              "قُلْ",
              "هَلْ"
            ]
          },
          {
            "id": "bay_sukun",
            "grapheme": "بَيْ",
            "audioText": "بَيْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَاي",
              "بَيَ",
              "طَيْ"
            ]
          },
          {
            "id": "sham_sukun",
            "grapheme": "شَمْ",
            "audioText": "شَمْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "شَمَ",
              "شَمُ",
              "نَجْ"
            ]
          },
          {
            "id": "tay_sukun",
            "grapheme": "طَيْ",
            "audioText": "طَيْ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "طَيَ",
              "بَيْ",
              "حَيْ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Sukūn (ـْ) : The Consonant Stop",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 35,
        "worldId": 5,
        "title": "Madd Alif (ـَا) - Le son long \"Â\"",
        "titleAr": "مَدّ بِالأَلِف ( ـَا ) - 2 تَمْبس",
        "description": "Écoute le son long étiré avec Alif.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#6366F1",
          "#4338CA"
        ],
        "items": [
          {
            "id": "baa_long",
            "grapheme": "بَا",
            "audioText": "بَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "بُو",
              "تَا"
            ]
          },
          {
            "id": "taa_long",
            "grapheme": "تَا",
            "audioText": "تَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "تُو",
              "بَا"
            ]
          },
          {
            "id": "daa_long",
            "grapheme": "دَا",
            "audioText": "دَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دَ",
              "دُو",
              "رَا"
            ]
          },
          {
            "id": "raa_long",
            "grapheme": "رَا",
            "audioText": "رَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رَ",
              "رُو",
              "زَا"
            ]
          },
          {
            "id": "baa_long",
            "grapheme": "بَا",
            "audioText": "بَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بِي",
              "بَ",
              "تَا"
            ]
          },
          {
            "id": "daa_long",
            "grapheme": "دَا",
            "audioText": "دَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دِي",
              "دَ",
              "دُو"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Madd Alif (ـَا) : 2-Beat Long 'AA'",
        "descriptionEn": "Listen to the sound and catch the correct letter."
      },
      {
        "id": 36,
        "worldId": 5,
        "title": "Madd Waw (ـُو) - Le son long \"OUU\"",
        "titleAr": "مَدّ بِالوَاو ( ـُو ) - 2 تَمْبس",
        "description": "Prolonge la Ḍammah avec la lettre Waw.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#F59E0B",
          "#B45309"
        ],
        "items": [
          {
            "id": "boo_long",
            "grapheme": "بُو",
            "audioText": "بُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بُ",
              "بَا",
              "تُو"
            ]
          },
          {
            "id": "too_long",
            "grapheme": "تُو",
            "audioText": "تُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تُ",
              "تَا",
              "بُو"
            ]
          },
          {
            "id": "doo_long",
            "grapheme": "دُو",
            "audioText": "دُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُ",
              "دَا",
              "رُو"
            ]
          },
          {
            "id": "soo_long",
            "grapheme": "سُو",
            "audioText": "سُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سُ",
              "سَا",
              "شُو"
            ]
          },
          {
            "id": "shoo_long",
            "grapheme": "شُو",
            "audioText": "شُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "شُ",
              "شَا",
              "سُو"
            ]
          },
          {
            "id": "boo_long",
            "grapheme": "بُو",
            "audioText": "بُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بِي",
              "بُ",
              "تُو"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Madd Waw (ـُو) : 2-Beat Long 'UU'",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 37,
        "worldId": 5,
        "title": "Madd Ya (ـِي) - Le son long \"II\"",
        "titleAr": "مَدّ بِاليَاء ( ـِي ) - 2 تَمْبس",
        "description": "Prolonge la Kasrah avec la lettre Ya.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#EC4899",
          "#BE185D"
        ],
        "items": [
          {
            "id": "bee_long",
            "grapheme": "بِي",
            "audioText": "بِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بِ",
              "بَا",
              "تِي"
            ]
          },
          {
            "id": "tee_long",
            "grapheme": "تِي",
            "audioText": "تِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تِ",
              "تَا",
              "بِي"
            ]
          },
          {
            "id": "dee_long",
            "grapheme": "دِي",
            "audioText": "دِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دِ",
              "دَا",
              "رِي"
            ]
          },
          {
            "id": "see_long",
            "grapheme": "سِي",
            "audioText": "سِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سِ",
              "سَا",
              "شِي"
            ]
          },
          {
            "id": "shee_long",
            "grapheme": "شِي",
            "audioText": "شِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "شِ",
              "شَا",
              "سِي"
            ]
          },
          {
            "id": "ree_long",
            "grapheme": "رِي",
            "audioText": "رِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رِ",
              "رَا",
              "زِي"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Madd Ya (ـِي) : 2-Beat Long 'II'",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 38,
        "worldId": 5,
        "title": "Duel Court vs Long : Série A & OU",
        "titleAr": "المُقَارَنَة 1 : الفَتْحَة وَالضَّمَّة مَعَ المَدّ",
        "description": "Distingue immédiatement le son bref du son étiré !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#7C3AED",
          "#5B21B6"
        ],
        "items": [
          {
            "id": "ba_fatha",
            "grapheme": "بَ",
            "audioText": "بَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَا",
              "بُ",
              "بُو"
            ]
          },
          {
            "id": "baa_long",
            "grapheme": "بَا",
            "audioText": "بَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَ",
              "تَا",
              "بُو"
            ]
          },
          {
            "id": "ta_fatha",
            "grapheme": "تَ",
            "audioText": "تَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَا",
              "تُ",
              "تُو"
            ]
          },
          {
            "id": "taa_long",
            "grapheme": "تَا",
            "audioText": "تَا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تَ",
              "بَا",
              "تُو"
            ]
          },
          {
            "id": "du_damma",
            "grapheme": "دُ",
            "audioText": "دُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُو",
              "دَ",
              "دَا"
            ]
          },
          {
            "id": "doo_long",
            "grapheme": "دُو",
            "audioText": "دُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دُ",
              "تُو",
              "دَا"
            ]
          },
          {
            "id": "bu_damma",
            "grapheme": "بُ",
            "audioText": "بُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بُو",
              "بَ",
              "بَا"
            ]
          },
          {
            "id": "boo_long",
            "grapheme": "بُو",
            "audioText": "بُو",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بُ",
              "بَا",
              "تُو"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Duel Court vs Long : Série A & OU",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 39,
        "worldId": 5,
        "title": "Duel Court vs Long : Série I & Mixte",
        "titleAr": "المُقَارَنَة 2 : الكَسْرَة وَالمَدّ بِاليَاء",
        "description": "Distingue immédiatement le son bref et le son étiré avec Kasrah & Ya.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#06B6D4",
          "#0891B2"
        ],
        "items": [
          {
            "id": "bi_kasra",
            "grapheme": "بِ",
            "audioText": "بِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بِي",
              "بَ",
              "بُ"
            ]
          },
          {
            "id": "bee_long",
            "grapheme": "بِي",
            "audioText": "بِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بِ",
              "تِي",
              "بَا"
            ]
          },
          {
            "id": "si_kasra",
            "grapheme": "سِ",
            "audioText": "سِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سِي",
              "سَ",
              "سُ"
            ]
          },
          {
            "id": "see_long",
            "grapheme": "سِي",
            "audioText": "سِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "سِ",
              "شِي",
              "سَا"
            ]
          },
          {
            "id": "ri_kasra",
            "grapheme": "رِ",
            "audioText": "رِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رِي",
              "رَ",
              "رُ"
            ]
          },
          {
            "id": "ree_long",
            "grapheme": "رِي",
            "audioText": "رِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رِ",
              "رَا",
              "زِي"
            ]
          },
          {
            "id": "ti_kasra",
            "grapheme": "تِ",
            "audioText": "تِ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تِي",
              "تَ",
              "تُ"
            ]
          },
          {
            "id": "tee_long",
            "grapheme": "تِي",
            "audioText": "تِي",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "تِ",
              "بِي",
              "تَا"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Duel Court vs Long : Série I & Mixte",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      }
    ],
    "nameEn": "World 5: Sukūn & Long Vowels (Madd)",
    "descriptionEn": "Contrast consonant stops (Sukūn) with sustained 2-beat long vowels (Alif, Waw, Ya)."
  },
  {
    "id": 6,
    "name": "Monde 6 : Shaddah, Tanwīn & Alif-Lām",
    "nameAr": "العالم السادس : الشَّدَّة والتَّنْوِين وَأَل التَّعْرِيف",
    "description": "Maîtrise la consonne appuyée (Shaddah), les terminaisons Tanwīn (-an, -oun, -in) et l'article Alif-Lām.",
    "icon": "flash",
    "color": "#E11D48",
    "levels": [
      {
        "id": 40,
        "worldId": 6,
        "title": "La Shaddah (ـّ) : Consonne double appuyée",
        "titleAr": "الشَّدَّة ( ـّ ) - الحَرْف المُشَدَّد",
        "description": "Appuie fortement sur la consonne doublée avec voyelle finale.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#F43F5E",
          "#BE123C"
        ],
        "items": [
          {
            "id": "rabba",
            "grapheme": "رَبَّ",
            "audioText": "رَبَّ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "رَبَ",
              "رَبُ",
              "رَدَّ"
            ]
          },
          {
            "id": "madda",
            "grapheme": "مَدَّ",
            "audioText": "مَدَّ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "مَدَ",
              "مَدِ",
              "شَدَّ"
            ]
          },
          {
            "id": "allama",
            "grapheme": "عَلَّمَ",
            "audioText": "عَلَّمَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "عَلَمَ",
              "عَلِمَ",
              "قَلَّمَ"
            ]
          },
          {
            "id": "shadda",
            "grapheme": "شَدَّ",
            "audioText": "شَدَّ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "شَدَ",
              "شَدُ",
              "مَدَّ"
            ]
          },
          {
            "id": "hassa",
            "grapheme": "حَسَّ",
            "audioText": "حَسَّ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "حَسَ",
              "حَسُ",
              "مَسَّ"
            ]
          },
          {
            "id": "rabba",
            "grapheme": "رَبَّ",
            "audioText": "رَبَّ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "شَدَّ",
              "مَدَّ",
              "عَلَّمَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "The Shaddah (ـّ) : Doubled Consonant",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 41,
        "worldId": 6,
        "title": "Le Tanwīn en -an (ـً) : Terminaison ouverte",
        "titleAr": "تَنْوِينُ الفَتْحِ : صَوْتُ أَنْ",
        "description": "Écoute la terminaison avec Tanwīn Fatḥ (ـً).",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#FB7185",
          "#9F1239"
        ],
        "items": [
          {
            "id": "kitaban",
            "grapheme": "كِتَابًا",
            "audioText": "كِتَابًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِتَابٌ",
              "كِتَابٍ",
              "كِتَاب"
            ]
          },
          {
            "id": "waladan",
            "grapheme": "وَلَدًا",
            "audioText": "وَلَدًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدٌ",
              "وَلَدٍ",
              "وَلَد"
            ]
          },
          {
            "id": "baytan",
            "grapheme": "بَيْتًا",
            "audioText": "بَيْتًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتٌ",
              "بَيْتٍ",
              "بَيْت"
            ]
          },
          {
            "id": "kitaban",
            "grapheme": "كِتَابًا",
            "audioText": "كِتَابًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدًا",
              "بَيْتًا",
              "كِتَابٌ"
            ]
          },
          {
            "id": "waladan",
            "grapheme": "وَلَدًا",
            "audioText": "وَلَدًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتًا",
              "كِتَابًا",
              "وَلَدٌ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Tanwīn -an (ـً) : Open Nunation",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 42,
        "worldId": 6,
        "title": "Le Tanwīn en -oun (ـٌ) : Terminaison fermée",
        "titleAr": "تَنْوِينُ الضَّمِّ : صَوْتُ أُنْ",
        "description": "Écoute la terminaison avec Tanwīn Ḍamm (ـٌ).",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#E11D48",
          "#BE123C"
        ],
        "items": [
          {
            "id": "kitabun",
            "grapheme": "كِتَابٌ",
            "audioText": "كِتَابٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِتَابًا",
              "كِتَابٍ",
              "كِتَاب"
            ]
          },
          {
            "id": "waladun",
            "grapheme": "وَلَدٌ",
            "audioText": "وَلَدٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدًا",
              "وَلَدٍ",
              "وَلَد"
            ]
          },
          {
            "id": "baytun",
            "grapheme": "بَيْتٌ",
            "audioText": "بَيْتٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتًا",
              "بَيْتٍ",
              "بَيْت"
            ]
          },
          {
            "id": "kitabun",
            "grapheme": "كِتَابٌ",
            "audioText": "كِتَابٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدٌ",
              "بَيْتٌ",
              "كِتَابًا"
            ]
          },
          {
            "id": "waladun",
            "grapheme": "وَلَدٌ",
            "audioText": "وَلَدٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتٌ",
              "كِتَابٌ",
              "وَلَدًا"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Tanwīn -un (ـٌ) : Closed Nunation",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 43,
        "worldId": 6,
        "title": "Le Tanwīn en -in (ـٍ) & Grand Duel des 3 Tanwīns",
        "titleAr": "تَنْوِينُ الكَسْرِ وَتَحَدِّي التَّنْوِين",
        "description": "Distingue instantanément les 3 formes de Tanwīn !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#BE123C",
          "#881337"
        ],
        "items": [
          {
            "id": "kitabin",
            "grapheme": "كِتَابٍ",
            "audioText": "كِتَابٍ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِتَابًا",
              "كِتَابٌ",
              "كِتَاب"
            ]
          },
          {
            "id": "waladin",
            "grapheme": "وَلَدٍ",
            "audioText": "وَلَدٍ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدًا",
              "وَلَدٌ",
              "وَلَد"
            ]
          },
          {
            "id": "baytin",
            "grapheme": "بَيْتٍ",
            "audioText": "بَيْتٍ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتًا",
              "بَيْتٌ",
              "بَيْت"
            ]
          },
          {
            "id": "kitaban",
            "grapheme": "كِتَابًا",
            "audioText": "كِتَابًا",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كِتَابٌ",
              "كِتَابٍ",
              "كِتَاب"
            ]
          },
          {
            "id": "waladun",
            "grapheme": "وَلَدٌ",
            "audioText": "وَلَدٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "وَلَدًا",
              "وَلَدٍ",
              "وَلَد"
            ]
          },
          {
            "id": "baytin",
            "grapheme": "بَيْتٍ",
            "audioText": "بَيْتٍ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "بَيْتًا",
              "بَيْتٌ",
              "بَيْت"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Tanwīn -in (ـٍ) & The 3 Tanwīns Duel",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 44,
        "worldId": 6,
        "title": "Alif-Lām (الـ) : Lettres Lunaires (Lām prononcé)",
        "titleAr": "اللاَّمُ القَمَرِيَّة ( صَوْت \"الـ\" وَاضِح )",
        "description": "Le Lām s'entend clairement avec un Sukūn sur le Lām.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [
          {
            "id": "al_qamar",
            "grapheme": "القَمَر",
            "audioText": "القَمَرُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "الشَّمْس",
              "النَّجْم",
              "الطَّيْر"
            ]
          },
          {
            "id": "al_kitaab",
            "grapheme": "الكِتَاب",
            "audioText": "الكِتَابُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "النَّجْم",
              "الشَّمْس",
              "الطَّيْر"
            ]
          },
          {
            "id": "al_walad",
            "grapheme": "الوَلَد",
            "audioText": "الوَلَدُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "الطَّيْر",
              "الشَّمْس",
              "النَّجْم"
            ]
          },
          {
            "id": "al_qamar",
            "grapheme": "القَمَر",
            "audioText": "القَمَرُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "الكِتَاب",
              "الوَلَد",
              "الشَّمْس"
            ]
          },
          {
            "id": "al_kitaab",
            "grapheme": "الكِتَاب",
            "audioText": "الكِتَابُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "القَمَر",
              "الوَلَد",
              "النَّجْم"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Alif-Lām (الـ) : Moon Letters",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 45,
        "worldId": 6,
        "title": "Alif-Lām (الـ) : Lettres Solaires (Lām muet + Shaddah)",
        "titleAr": "اللاَّمُ الشَّمْسِيَّة ( إِدْغَام مَعَ الشَّدَّة )",
        "description": "Le Lām est muet et la consonne suivante prend une Shaddah.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#E11D48",
          "#881337"
        ],
        "items": [
          {
            "id": "ash_shams",
            "grapheme": "الشَّمْس",
            "audioText": "الشَّمْسُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "القَمَر",
              "الكِتَاب",
              "الوَلَد"
            ]
          },
          {
            "id": "an_najm",
            "grapheme": "النَّجْم",
            "audioText": "النَّجْمُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "القَمَر",
              "الكِتَاب",
              "الوَلَد"
            ]
          },
          {
            "id": "at_tayr",
            "grapheme": "الطَّيْر",
            "audioText": "الطَّيْرُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "القَمَر",
              "الكِتَاب",
              "الوَلَد"
            ]
          },
          {
            "id": "ash_shams",
            "grapheme": "الشَّمْس",
            "audioText": "الشَّمْسُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "النَّجْم",
              "الطَّيْر",
              "القَمَر"
            ]
          },
          {
            "id": "an_najm",
            "grapheme": "النَّجْم",
            "audioText": "النَّجْمُ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "الشَّمْس",
              "الطَّيْر",
              "الكِتَاب"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Alif-Lām (الـ) : Sun Letters",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      }
    ],
    "nameEn": "World 6: Shaddah, Tanwīn & Alif-Lām",
    "descriptionEn": "Double consonants (Shaddah), nunations (Tanwīn), and Solar vs Lunar letters (الـ)."
  },
  {
    "id": 7,
    "name": "Monde 7 : Le Vocabulaire & Mots",
    "nameAr": "العالم السابع : تَرْكِيبُ الكَلِمَاتِ وَالمُفْرَدَات",
    "description": "Assemble les lettres et accède à la lecture autonome et rapide de mots variés de la vie quotidienne.",
    "icon": "cube",
    "color": "#D97706",
    "levels": [
      {
        "id": 46,
        "worldId": 7,
        "title": "Verbes à 3 lettres de base",
        "titleAr": "أَفْعَال ثُلَاثِيَّة بِالفَتْحَة",
        "description": "Assemble les phonèmes pour former le mot entier.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#10B981",
          "#064E3B"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "kataba",
            "word": "كَتَبَ",
            "meaning": "Il a écrit",
            "translationFr": "Écrire",
            "letters": [
              "كَ",
              "تَ",
              "بَ"
            ],
            "distractorLetters": [
              "رَ",
              "سَ"
            ],
            "emoji": "✍️",
            "translationEn": "Write"
          },
          {
            "id": "darasa",
            "word": "دَرَسَ",
            "meaning": "Il a étudié",
            "translationFr": "Étudier",
            "letters": [
              "دَ",
              "رَ",
              "سَ"
            ],
            "distractorLetters": [
              "زَ",
              "تَ"
            ],
            "emoji": "📖",
            "translationEn": "Study"
          },
          {
            "id": "qaraa",
            "word": "قَرَأَ",
            "meaning": "Il a lu",
            "translationFr": "Lire",
            "letters": [
              "قَ",
              "رَ",
              "أَ"
            ],
            "distractorLetters": [
              "فَ",
              "كَ"
            ],
            "emoji": "📚",
            "translationEn": "Read"
          },
          {
            "id": "rasama",
            "word": "رَسَمَ",
            "meaning": "Il a dessiné",
            "translationFr": "Dessiner",
            "letters": [
              "رَ",
              "سَ",
              "مَ"
            ],
            "distractorLetters": [
              "نَ",
              "دَ"
            ],
            "emoji": "🎨",
            "translationEn": "Draw"
          }
        ],
        "titleEn": "3-Letter Base Verbs",
        "descriptionEn": "Listen and assemble the letters in the correct order."
      },
      {
        "id": 47,
        "worldId": 7,
        "title": "Verbes d'action du quotidien",
        "titleAr": "أَفْعَال يَوْمِيَّة مُتَنَوِّعَة",
        "description": "Écoute et construis les verbes d'action.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "jalasa",
            "word": "جَلَسَ",
            "meaning": "Il s'est assis",
            "translationFr": "S'asseoir",
            "letters": [
              "جَ",
              "لَ",
              "سَ"
            ],
            "distractorLetters": [
              "حَ",
              "دَ"
            ],
            "emoji": "🪑",
            "translationEn": "Sit"
          },
          {
            "id": "dhahaba",
            "word": "ذَهَبَ",
            "meaning": "Il est parti",
            "translationFr": "Partir",
            "letters": [
              "ذَ",
              "هَ",
              "بَ"
            ],
            "distractorLetters": [
              "دَ",
              "تَ"
            ],
            "emoji": "🚶",
            "translationEn": "Leave"
          },
          {
            "id": "samia",
            "word": "سَمِعَ",
            "meaning": "Il a écouté",
            "translationFr": "Écouter",
            "letters": [
              "سَ",
              "مِ",
              "عَ"
            ],
            "distractorLetters": [
              "شَ",
              "قَ"
            ],
            "emoji": "👂",
            "translationEn": "Listen"
          },
          {
            "id": "akala",
            "word": "أَكَلَ",
            "meaning": "Il a mangé",
            "translationFr": "Manger",
            "letters": [
              "أَ",
              "كَ",
              "لَ"
            ],
            "distractorLetters": [
              "نَ",
              "بَ"
            ],
            "emoji": "🍽️",
            "translationEn": "Eat"
          },
          {
            "id": "shariba",
            "word": "شَرِبَ",
            "meaning": "Il a bu",
            "translationFr": "Boire",
            "letters": [
              "شَ",
              "رِ",
              "بَ"
            ],
            "distractorLetters": [
              "سَ",
              "تَ"
            ],
            "emoji": "🥛",
            "translationEn": "Drink"
          },
          {
            "id": "fataha",
            "word": "فَتَحَ",
            "meaning": "Il a ouvert",
            "translationFr": "Ouvrir",
            "letters": [
              "فَ",
              "تَ",
              "حَ"
            ],
            "distractorLetters": [
              "قَ",
              "جَ"
            ],
            "emoji": "🚪",
            "translationEn": "Open"
          }
        ],
        "titleEn": "Daily Action Verbs",
        "descriptionEn": "Listen and assemble the letters in the correct order."
      },
      {
        "id": 48,
        "worldId": 7,
        "title": "Mots illustrés : Maison & Bureau",
        "titleAr": "كَلِمَات مُصَوَّرَة مِنَ البَيْت وَالمَكْتَب",
        "description": "Écoute le mot et retrouve sa composition exacte.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#3B82F6",
          "#1E3A8A"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "bab",
            "word": "بَاب",
            "meaning": "Porte",
            "translationFr": "Porte",
            "letters": [
              "بَا",
              "ب"
            ],
            "distractorLetters": [
              "ت",
              "د"
            ],
            "emoji": "🚪",
            "translationEn": "Door"
          },
          {
            "id": "bayt",
            "word": "بَيْت",
            "meaning": "Maison",
            "translationFr": "Maison",
            "letters": [
              "بَ",
              "يْ",
              "ت"
            ],
            "distractorLetters": [
              "ن",
              "ك"
            ],
            "emoji": "🏠",
            "translationEn": "House"
          },
          {
            "id": "kursiy",
            "word": "كُرْسِيّ",
            "meaning": "Chaise",
            "translationFr": "Chaise",
            "letters": [
              "كُ",
              "رْ",
              "سِ",
              "يّ"
            ],
            "distractorLetters": [
              "م",
              "ل"
            ],
            "emoji": "🪑",
            "translationEn": "Chair"
          },
          {
            "id": "maktab",
            "word": "مَكْتَب",
            "meaning": "Bureau",
            "translationFr": "Bureau",
            "letters": [
              "مَ",
              "كْ",
              "تَ",
              "ب"
            ],
            "distractorLetters": [
              "ن",
              "د"
            ],
            "emoji": "🖥️",
            "translationEn": "Desk"
          },
          {
            "id": "qalam",
            "word": "قَلَم",
            "meaning": "Stylo",
            "translationFr": "Stylo",
            "letters": [
              "قَ",
              "لَ",
              "م"
            ],
            "distractorLetters": [
              "ك",
              "ن"
            ],
            "emoji": "✏️",
            "translationEn": "Pen"
          }
        ],
        "titleEn": "Illustrated Words: House & Office",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 49,
        "worldId": 7,
        "title": "Les Animaux du Monde",
        "titleAr": "حَدِيقَةُ الحَيَوَانَات",
        "description": "Découvre et écris les noms des animaux.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#059669",
          "#047857"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "asad",
            "word": "أَسَد",
            "meaning": "Lion",
            "translationFr": "Lion",
            "letters": [
              "أَ",
              "سَ",
              "د"
            ],
            "distractorLetters": [
              "ذ",
              "ر"
            ],
            "emoji": "🦁",
            "translationEn": "Lion"
          },
          {
            "id": "jamal",
            "word": "جَمَل",
            "meaning": "Chameau",
            "translationFr": "Chameau",
            "letters": [
              "جَ",
              "مَ",
              "ل"
            ],
            "distractorLetters": [
              "ح",
              "ن"
            ],
            "emoji": "🐪",
            "translationEn": "Camel"
          },
          {
            "id": "feel",
            "word": "فِيل",
            "meaning": "Éléphant",
            "translationFr": "Éléphant",
            "letters": [
              "فِي",
              "ل"
            ],
            "distractorLetters": [
              "ق",
              "ب"
            ],
            "emoji": "🐘",
            "translationEn": "Elephant"
          },
          {
            "id": "tayr",
            "word": "طَيْر",
            "meaning": "Oiseau",
            "translationFr": "Oiseau",
            "letters": [
              "طَ",
              "يْ",
              "ر"
            ],
            "distractorLetters": [
              "ت",
              "ز"
            ],
            "emoji": "🐦",
            "translationEn": "Bird"
          },
          {
            "id": "qitt",
            "word": "قِطّ",
            "meaning": "Chat",
            "translationFr": "Chat",
            "letters": [
              "قِ",
              "طّ"
            ],
            "distractorLetters": [
              "ك",
              "ت"
            ],
            "emoji": "🐱",
            "translationEn": "Cat"
          },
          {
            "id": "kalb",
            "word": "كَلْب",
            "meaning": "Chien",
            "translationFr": "Chien",
            "letters": [
              "كَ",
              "لْ",
              "ب"
            ],
            "distractorLetters": [
              "ق",
              "د"
            ],
            "emoji": "🐶",
            "translationEn": "Dog"
          }
        ],
        "titleEn": "Animals of the World",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 50,
        "worldId": 7,
        "title": "La Nature & les Éléments",
        "titleAr": "الطَّبِيعَةُ وَعَنَاصِرُ الكَوْن",
        "description": "Écris les mots du ciel, de l'eau et des végétaux.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#8B5CF6",
          "#5B21B6"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "shams",
            "word": "شَمْس",
            "meaning": "Soleil",
            "translationFr": "Soleil",
            "letters": [
              "شَ",
              "مْ",
              "س"
            ],
            "distractorLetters": [
              "ص",
              "ز"
            ],
            "emoji": "☀️",
            "translationEn": "Sun"
          },
          {
            "id": "qamar",
            "word": "قَمَر",
            "meaning": "Lune",
            "translationFr": "Lune",
            "letters": [
              "قَ",
              "مَ",
              "ر"
            ],
            "distractorLetters": [
              "غ",
              "ل"
            ],
            "emoji": "🌙",
            "translationEn": "Moon"
          },
          {
            "id": "najm",
            "word": "نَجْم",
            "meaning": "Étoile",
            "translationFr": "Étoile",
            "letters": [
              "نَ",
              "جْ",
              "م"
            ],
            "distractorLetters": [
              "ح",
              "ت"
            ],
            "emoji": "⭐",
            "translationEn": "Star"
          },
          {
            "id": "bahr",
            "word": "بَحْر",
            "meaning": "Mer",
            "translationFr": "Mer",
            "letters": [
              "بَ",
              "حْ",
              "ر"
            ],
            "distractorLetters": [
              "ج",
              "ز"
            ],
            "emoji": "🌊",
            "translationEn": "Sea"
          },
          {
            "id": "samaa",
            "word": "سَمَاء",
            "meaning": "Ciel",
            "translationFr": "Ciel",
            "letters": [
              "سَ",
              "مَا",
              "ء"
            ],
            "distractorLetters": [
              "ش",
              "د"
            ],
            "emoji": "☁️",
            "translationEn": "Sky"
          },
          {
            "id": "shajara",
            "word": "شَجَرَة",
            "meaning": "Arbre",
            "translationFr": "Arbre",
            "letters": [
              "شَ",
              "جَ",
              "رَ",
              "ة"
            ],
            "distractorLetters": [
              "س",
              "د"
            ],
            "emoji": "🌳",
            "translationEn": "Tree"
          }
        ],
        "titleEn": "Nature & Elements",
        "descriptionEn": "Listen and assemble the letters in the correct order."
      },
      {
        "id": 51,
        "worldId": 7,
        "title": "La Famille & les Personnes",
        "titleAr": "العَائِلَةُ وَالأَقَارِب",
        "description": "Reconnais les membres de la famille et les personnes.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#EC4899",
          "#9D174D"
        ],
        "items": [
          {
            "id": "ab",
            "grapheme": "أَب",
            "audioText": "أَبٌ",
            "phonemeDesc": "Père",
            "transliteration": "",
            "distractors": [
              "أُمّ",
              "أَخ",
              "أُخْت"
            ],
            "phonemeDescEn": "Father"
          },
          {
            "id": "umm",
            "grapheme": "أُمّ",
            "audioText": "أُمٌّ",
            "phonemeDesc": "Mère",
            "transliteration": "",
            "distractors": [
              "أَب",
              "بِنْت",
              "وَلَد"
            ],
            "phonemeDescEn": "Mother"
          },
          {
            "id": "akh",
            "grapheme": "أَخ",
            "audioText": "أَخٌ",
            "phonemeDesc": "Frère",
            "transliteration": "",
            "distractors": [
              "أُخْت",
              "أَب",
              "مُعَلِّم"
            ],
            "phonemeDescEn": "Brother"
          },
          {
            "id": "ukht",
            "grapheme": "أُخْت",
            "audioText": "أُخْتٌ",
            "phonemeDesc": "Sœur",
            "transliteration": "",
            "distractors": [
              "أَخ",
              "أُمّ",
              "بِنْت"
            ]
          },
          {
            "id": "walad",
            "grapheme": "وَلَد",
            "audioText": "وَلَدٌ",
            "phonemeDesc": "Garçon",
            "transliteration": "",
            "distractors": [
              "بِنْت",
              "طِفْل",
              "مُعَلِّم"
            ]
          },
          {
            "id": "bint",
            "grapheme": "بِنْت",
            "audioText": "بِنْتٌ",
            "phonemeDesc": "Fille",
            "transliteration": "",
            "distractors": [
              "وَلَد",
              "أُخْت",
              "أُمّ"
            ]
          },
          {
            "id": "muallim",
            "grapheme": "مُعَلِّم",
            "audioText": "مُعَلِّمٌ",
            "phonemeDesc": "Enseignant",
            "transliteration": "",
            "distractors": [
              "طِفْل",
              "أَب",
              "وَلَد"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Family & People",
        "descriptionEn": "Recognize the correct Arabic phrase and meaning."
      },
      {
        "id": 52,
        "worldId": 7,
        "title": "Les Aliments & Boissons",
        "titleAr": "الأَطْعِمَةُ وَالمَشْرُوبَات",
        "description": "Assemble les délices du quotidien.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#EA580C",
          "#C2410C"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "maa",
            "word": "مَاء",
            "meaning": "Eau",
            "translationFr": "Eau",
            "letters": [
              "مَا",
              "ء"
            ],
            "distractorLetters": [
              "ن",
              "ب"
            ],
            "emoji": "💧",
            "translationEn": "Water"
          },
          {
            "id": "haleeb",
            "word": "حَلِيب",
            "meaning": "Lait",
            "translationFr": "Lait",
            "letters": [
              "حَ",
              "لِي",
              "ب"
            ],
            "distractorLetters": [
              "ج",
              "ت"
            ],
            "emoji": "🥛",
            "translationEn": "Milk"
          },
          {
            "id": "khubz",
            "word": "خُبْز",
            "meaning": "Pain",
            "translationFr": "Pain",
            "letters": [
              "خُ",
              "بْ",
              "ز"
            ],
            "distractorLetters": [
              "ح",
              "ر"
            ],
            "emoji": "🍞",
            "translationEn": "Pain / Bread"
          },
          {
            "id": "tamr",
            "word": "تَمْر",
            "meaning": "Dattes",
            "translationFr": "Dattes",
            "letters": [
              "تَ",
              "مْ",
              "ر"
            ],
            "distractorLetters": [
              "ث",
              "ز"
            ],
            "emoji": "🌴",
            "translationEn": "Dates"
          },
          {
            "id": "inab",
            "word": "عِنَب",
            "meaning": "Raisin",
            "translationFr": "Raisin",
            "letters": [
              "عِ",
              "نَ",
              "ب"
            ],
            "distractorLetters": [
              "غ",
              "ت"
            ],
            "emoji": "🍇",
            "translationEn": "Grapes"
          },
          {
            "id": "tuffah",
            "word": "تُفَّاح",
            "meaning": "Pomme",
            "translationFr": "Pomme",
            "letters": [
              "تُ",
              "فَّا",
              "ح"
            ],
            "distractorLetters": [
              "ب",
              "ج"
            ],
            "emoji": "🍎",
            "translationEn": "Apple"
          }
        ],
        "titleEn": "Food & Drinks",
        "descriptionEn": "Listen and assemble the letters in the correct order."
      },
      {
        "id": 53,
        "worldId": 7,
        "title": "Mots complexes : Madd, Sukūn & Shaddah",
        "titleAr": "كَلِمَاتٌ مُرَكَّبَة مَعَ المَدِّ وَالشَّدَّة",
        "description": "Assemble des mots riches avec plusieurs règles combinées.",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#7C3AED",
          "#4C1D95"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "madrasa",
            "word": "مَدْرَسَة",
            "meaning": "École",
            "translationFr": "École",
            "letters": [
              "مَ",
              "دْ",
              "رَ",
              "سَ",
              "ة"
            ],
            "distractorLetters": [
              "ت",
              "ن"
            ],
            "emoji": "🏫",
            "translationEn": "School"
          },
          {
            "id": "hadeeqa",
            "word": "حَدِيقَة",
            "meaning": "Jardin",
            "translationFr": "Jardin",
            "letters": [
              "حَ",
              "دِي",
              "قَ",
              "ة"
            ],
            "distractorLetters": [
              "خ",
              "ت"
            ],
            "emoji": "🌸",
            "translationEn": "Garden"
          },
          {
            "id": "ousfoor",
            "word": "عُصْفُور",
            "meaning": "Petit oiseau",
            "translationFr": "Oiseau",
            "letters": [
              "عُ",
              "صْ",
              "فُو",
              "ر"
            ],
            "distractorLetters": [
              "غ",
              "س"
            ],
            "emoji": "🐦",
            "translationEn": "Bird"
          },
          {
            "id": "rumman",
            "word": "رُمَّان",
            "meaning": "Grenade",
            "translationFr": "Grenade",
            "letters": [
              "رُ",
              "مَّا",
              "ن"
            ],
            "distractorLetters": [
              "ز",
              "ل"
            ],
            "emoji": "🫐",
            "translationEn": "Pomegranate"
          }
        ],
        "titleEn": "Complex Words: Madd, Sukūn & Shaddah",
        "descriptionEn": "Listen and assemble the letters in the correct order."
      },
      {
        "id": 54,
        "worldId": 7,
        "title": "Défi Écoute & Orthographe de Mots",
        "titleAr": "تَحَدِّي فَرْزِ الكَلِمَاتِ السَّرِيع",
        "description": "Écoute le mot prononcé et fais éclater la bonne bulle !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#0D9488",
          "#115E59"
        ],
        "items": [
          {
            "id": "kitab",
            "grapheme": "كِتَاب",
            "audioText": "كِتَابٌ",
            "phonemeDesc": "Livre",
            "transliteration": "",
            "distractors": [
              "قَلَم",
              "بَاب",
              "بَيْت"
            ],
            "phonemeDescEn": "Book"
          },
          {
            "id": "qalam",
            "grapheme": "قَلَم",
            "audioText": "قَلَمٌ",
            "phonemeDesc": "Stylo",
            "transliteration": "",
            "distractors": [
              "كِتَاب",
              "كُرْسِيّ",
              "مَكْتَب"
            ],
            "phonemeDescEn": "Pen"
          },
          {
            "id": "kursiy",
            "grapheme": "كُرْسِيّ",
            "audioText": "كُرْسِيٌّ",
            "phonemeDesc": "Chaise",
            "transliteration": "",
            "distractors": [
              "مَكْتَب",
              "بَاب",
              "بَيْت"
            ],
            "phonemeDescEn": "Chair"
          },
          {
            "id": "maktab",
            "grapheme": "مَكْتَب",
            "audioText": "مَكْتَبٌ",
            "phonemeDesc": "Bureau",
            "transliteration": "",
            "distractors": [
              "كُرْسِيّ",
              "قَلَم",
              "كِتَاب"
            ],
            "phonemeDescEn": "Desk"
          },
          {
            "id": "madrasa",
            "grapheme": "مَدْرَسَة",
            "audioText": "مَدْرَسَةٌ",
            "phonemeDesc": "École",
            "transliteration": "",
            "distractors": [
              "حَدِيقَة",
              "بَيْت",
              "شَجَرَة"
            ],
            "phonemeDescEn": "School"
          },
          {
            "id": "hadeeqa",
            "grapheme": "حَدِيقَة",
            "audioText": "حَدِيقَةٌ",
            "phonemeDesc": "Jardin",
            "transliteration": "",
            "distractors": [
              "مَدْرَسَة",
              "زَهْرَة",
              "شَجَرَة"
            ],
            "phonemeDescEn": "Garden"
          }
        ],
        "wordItems": [],
        "titleEn": "Défi Écoute & Orthographe de Mots",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 55,
        "worldId": 7,
        "title": "Grand Défi de Lecture Rapide de Vocabulaire",
        "titleAr": "تَحَدِّي القِرَاءَة السَّرِيعَة لِلْمُفْرَدَات",
        "description": "Le grand test de reconnaissance instantanée de tout le vocabulaire !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#D97706",
          "#92400E"
        ],
        "items": [
          {
            "id": "kataba",
            "grapheme": "كَتَبَ",
            "audioText": "كَتَبَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "دَرَسَ",
              "قَرَأَ",
              "رَسَمَ"
            ]
          },
          {
            "id": "darasa",
            "grapheme": "دَرَسَ",
            "audioText": "دَرَسَ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "كَتَبَ",
              "جَلَسَ",
              "ذَهَبَ"
            ]
          },
          {
            "id": "asad",
            "grapheme": "أَسَد",
            "audioText": "أَسَدٌ",
            "phonemeDesc": "",
            "transliteration": "",
            "distractors": [
              "جَمَل",
              "فِيل",
              "طَيْر"
            ]
          },
          {
            "id": "feel",
            "grapheme": "فِيل",
            "audioText": "فِيلٌ",
            "phonemeDesc": "Feel",
            "transliteration": "",
            "distractors": [
              "أَسَد",
              "جَمَل",
              "قِطّ"
            ]
          },
          {
            "id": "shams",
            "grapheme": "شَمْس",
            "audioText": "شَمْسٌ",
            "phonemeDesc": "Shams",
            "transliteration": "",
            "distractors": [
              "قَمَر",
              "نَجْم",
              "سَمَاء"
            ]
          },
          {
            "id": "bahr",
            "grapheme": "بَحْر",
            "audioText": "بَحْرٌ",
            "phonemeDesc": "Baḥr",
            "transliteration": "",
            "distractors": [
              "نَهْر",
              "سَمَاء",
              "مَاء"
            ]
          },
          {
            "id": "tuffah",
            "grapheme": "تُفَّاح",
            "audioText": "تُفَّاحٌ",
            "phonemeDesc": "Tuffāḥ",
            "transliteration": "",
            "distractors": [
              "عِنَب",
              "تَمْر",
              "خُبْز"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Grand Challenge de Lecture Rapide de Vocabulaire",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      }
    ],
    "nameEn": "World 7: Vocabulary & Everyday Words",
    "descriptionEn": "Read and assemble everyday nouns, action verbs, and illustrated vocabulary."
  },
  {
    "id": 8,
    "name": "Monde 8 : Phrases & Textes Courts",
    "nameAr": "العالم الثامن : قِرَاءَةُ الجُمَلِ وَالنُّصُوصِ القَصِيرَة",
    "description": "Lis avec fluidité et comprends de vraies phrases arabes, des dialogues du quotidien et de petites histoires.",
    "icon": "reader",
    "color": "#E11D48",
    "levels": [
      {
        "id": 56,
        "worldId": 8,
        "title": "Phrases Nominales 1 : Sujet & Description",
        "titleAr": "الجُمَلُ الاسْمِيَّةُ البَسِيطَة",
        "description": "Lis des phrases à 2 mots décrivant des objets et la nature.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#F43F5E",
          "#BE123C"
        ],
        "items": [
          {
            "id": "albayt_kabeer",
            "grapheme": "البَيْتُ كَبِيرٌ",
            "audioText": "البَيْتُ كَبِيرٌ",
            "phonemeDesc": "La maison est grande",
            "transliteration": "",
            "distractors": [
              "المَاءُ بَارِدٌ",
              "الكِتَابُ مُفِيدٌ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ],
            "phonemeDescEn": "The house is big"
          },
          {
            "id": "almaa_baarid",
            "grapheme": "المَاءُ بَارِدٌ",
            "audioText": "المَاءُ بَارِدٌ",
            "phonemeDesc": "L'eau est fraîche",
            "transliteration": "",
            "distractors": [
              "البَيْتُ كَبِيرٌ",
              "القَمَرُ مُنِيرٌ",
              "الكِتَابُ مُفِيدٌ"
            ],
            "phonemeDescEn": "The water is cold"
          },
          {
            "id": "alkitaab_mufeed",
            "grapheme": "الكِتَابُ مُفِيدٌ",
            "audioText": "الكِتَابُ مُفِيدٌ",
            "phonemeDesc": "Le livre est utile",
            "transliteration": "",
            "distractors": [
              "البَيْتُ كَبِيرٌ",
              "المَاءُ بَارِدٌ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ],
            "phonemeDescEn": "The book is useful"
          },
          {
            "id": "ashshams_mushriqa",
            "grapheme": "الشَّمْسُ مُشْرِقَةٌ",
            "audioText": "الشَّمْسُ مُشْرِقَةٌ",
            "phonemeDesc": "Le soleil brille",
            "transliteration": "",
            "distractors": [
              "القَمَرُ مُنِيرٌ",
              "المَاءُ بَارِدٌ",
              "البَيْتُ كَبِيرٌ"
            ],
            "phonemeDescEn": "The sun is shining"
          },
          {
            "id": "alqamar_muneer",
            "grapheme": "القَمَرُ مُنِيرٌ",
            "audioText": "القَمَرُ مُنِيرٌ",
            "phonemeDesc": "La lune est lumineuse",
            "transliteration": "",
            "distractors": [
              "الشَّمْسُ مُشْرِقَةٌ",
              "الكِتَابُ مُفِيدٌ",
              "المَاءُ بَارِدٌ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Nominal Sentences 1: Subject & Description",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 57,
        "worldId": 8,
        "title": "Phrases Nominales 2 : Qualités & États",
        "titleAr": "أَوْصَافُ النَّاسِ وَالأَشْيَاء",
        "description": "Distingue les descriptions et caractéristiques.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#8B5CF6",
          "#6D28D9"
        ],
        "items": [
          {
            "id": "alwalad_nasheet",
            "grapheme": "الوَلَدُ نَشِيطٌ",
            "audioText": "الوَلَدُ نَشِيطٌ",
            "phonemeDesc": "Le garçon est énergique",
            "transliteration": "",
            "distractors": [
              "البِنْتُ ذَكِيَّةٌ",
              "القَلَمُ جَدِيدٌ",
              "البَابُ مَفْتُوحٌ"
            ],
            "phonemeDescEn": "The boy is energetic"
          },
          {
            "id": "albint_dhakiyya",
            "grapheme": "البِنْتُ ذَكِيَّةٌ",
            "audioText": "البِنْتُ ذَكِيَّةٌ",
            "phonemeDesc": "La fille est intelligente",
            "transliteration": "",
            "distractors": [
              "الوَلَدُ نَشِيطٌ",
              "الزَّهْرَةُ جَمِيلَةٌ",
              "القَلَمُ جَدِيدٌ"
            ],
            "phonemeDescEn": "The girl is smart"
          },
          {
            "id": "alqalam_jadeed",
            "grapheme": "القَلَمُ جَدِيدٌ",
            "audioText": "القَلَمُ جَدِيدٌ",
            "phonemeDesc": "Le stylo est neuf",
            "transliteration": "",
            "distractors": [
              "البَابُ مَفْتُوحٌ",
              "الوَلَدُ نَشِيطٌ",
              "البِنْتُ ذَكِيَّةٌ"
            ],
            "phonemeDescEn": "The pen is new"
          },
          {
            "id": "albaab_maftooh",
            "grapheme": "البَابُ مَفْتُوحٌ",
            "audioText": "البَابُ مَفْتُوحٌ",
            "phonemeDesc": "La porte est ouverte",
            "transliteration": "",
            "distractors": [
              "القَلَمُ جَدِيدٌ",
              "الزَّهْرَةُ جَمِيلَةٌ",
              "الوَلَدُ نَشِيطٌ"
            ]
          },
          {
            "id": "azzahra_jameela",
            "grapheme": "الزَّهْرَةُ جَمِيلَةٌ",
            "audioText": "الزَّهْرَةُ جَمِيلَةٌ",
            "phonemeDesc": "La fleur est belle",
            "transliteration": "",
            "distractors": [
              "البِنْتُ ذَكِيَّةٌ",
              "البَابُ مَفْتُوحٌ",
              "القَلَمُ جَدِيدٌ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Nominal Sentences 2: Qualities & States",
        "descriptionEn": "Listen carefully and distinguish the subtle sound differences."
      },
      {
        "id": 58,
        "worldId": 8,
        "title": "Phrases Verbales 1 : Verbe & Sujet",
        "titleAr": "الجُمَلُ الفِعْلِيَّةُ البَسِيطَة",
        "description": "Lis l'action réalisée par le sujet.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [
          {
            "id": "kataba_alwalad",
            "grapheme": "كَتَبَ الوَلَدُ",
            "audioText": "كَتَبَ الوَلَدُ",
            "phonemeDesc": "L'enfant a écrit",
            "transliteration": "",
            "distractors": [
              "قَرَأَ الطَّالِبُ",
              "جَلَسَ الأَبُ",
              "أَكَلَ الطِّفْلُ"
            ],
            "phonemeDescEn": "The child wrote"
          },
          {
            "id": "qaraa_attaalib",
            "grapheme": "قَرَأَ الطَّالِبُ",
            "audioText": "قَرَأَ الطَّالِبُ",
            "phonemeDesc": "L'élève a lu",
            "transliteration": "",
            "distractors": [
              "كَتَبَ الوَلَدُ",
              "شَرِبَ الوَلَدُ",
              "نَامَ الطِّفْلُ"
            ],
            "phonemeDescEn": "The student read"
          },
          {
            "id": "jalasa_alab",
            "grapheme": "جَلَسَ الأَبُ",
            "audioText": "جَلَسَ الأَبُ",
            "phonemeDesc": "Le père s'est assis",
            "transliteration": "",
            "distractors": [
              "كَتَبَ الوَلَدُ",
              "قَرَأَ الطَّالِبُ",
              "أَكَلَ الطِّفْلُ"
            ],
            "phonemeDescEn": "The father sat down"
          },
          {
            "id": "akala_attifl",
            "grapheme": "أَكَلَ الطِّفْلُ",
            "audioText": "أَكَلَ الطِّفْلُ",
            "phonemeDesc": "Le petit a mangé",
            "transliteration": "",
            "distractors": [
              "شَرِبَ الوَلَدُ",
              "جَلَسَ الأَبُ",
              "نَامَ الطِّفْلُ"
            ]
          },
          {
            "id": "shariba_alwalad",
            "grapheme": "شَرِبَ الوَلَدُ",
            "audioText": "شَرِبَ الوَلَدُ",
            "phonemeDesc": "Le garçon a bu",
            "transliteration": "",
            "distractors": [
              "أَكَلَ الطِّفْلُ",
              "كَتَبَ الوَلَدُ",
              "قَرَأَ الطَّالِبُ"
            ]
          },
          {
            "id": "naama_attifl",
            "grapheme": "نَامَ الطِّفْلُ",
            "audioText": "نَامَ الطِّفْلُ",
            "phonemeDesc": "Le bébé a dormi",
            "transliteration": "",
            "distractors": [
              "جَلَسَ الأَبُ",
              "شَرِبَ الوَلَدُ",
              "أَكَلَ الطِّفْلُ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Verbal Sentences 1: Verb & Subject",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 59,
        "worldId": 8,
        "title": "Phrases Verbales 2 : Actions & Mouvements",
        "titleAr": "أَفْعَالُ الحَرَكَةِ وَالانْتِقَال",
        "description": "Comprends les mouvements et déplacements.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#10B981",
          "#047857"
        ],
        "items": [
          {
            "id": "dhahaba_alwalad",
            "grapheme": "ذَهَبَ الوَلَدُ",
            "audioText": "ذَهَبَ الوَلَدُ",
            "phonemeDesc": "Le garçon est parti",
            "transliteration": "",
            "distractors": [
              "رَجَعَ الأَبُ",
              "خَرَجَ المُعَلِّمُ",
              "دَخَلَ الطَّالِبُ"
            ],
            "phonemeDescEn": "The boy left"
          },
          {
            "id": "rajaa_alab",
            "grapheme": "رَجَعَ الأَبُ",
            "audioText": "رَجَعَ الأَبُ",
            "phonemeDesc": "Le père est revenu",
            "transliteration": "",
            "distractors": [
              "ذَهَبَ الوَلَدُ",
              "خَرَجَ المُعَلِّمُ",
              "طَارَ العُصْفُورُ"
            ],
            "phonemeDescEn": "The father returned"
          },
          {
            "id": "kharaja_almuallim",
            "grapheme": "خَرَجَ المُعَلِّمُ",
            "audioText": "خَرَجَ المُعَلِّمُ",
            "phonemeDesc": "Le maître est sorti",
            "transliteration": "",
            "distractors": [
              "دَخَلَ الطَّالِبُ",
              "ذَهَبَ الوَلَدُ",
              "رَجَعَ الأَبُ"
            ],
            "phonemeDescEn": "The teacher went out"
          },
          {
            "id": "dakhala_attaalib",
            "grapheme": "دَخَلَ الطَّالِبُ",
            "audioText": "دَخَلَ الطَّالِبُ",
            "phonemeDesc": "L'élève est entré",
            "transliteration": "",
            "distractors": [
              "خَرَجَ المُعَلِّمُ",
              "طَارَ العُصْفُورُ",
              "ذَهَبَ الوَلَدُ"
            ]
          },
          {
            "id": "taara_alousfoor",
            "grapheme": "طَارَ العُصْفُورُ",
            "audioText": "طَارَ العُصْفُورُ",
            "phonemeDesc": "L'oiseau s'est envolé",
            "transliteration": "",
            "distractors": [
              "دَخَلَ الطَّالِبُ",
              "رَجَعَ الأَبُ",
              "خَرَجَ المُعَلِّمُ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Verbal Sentences 2: Actions & Movements",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      },
      {
        "id": 60,
        "worldId": 8,
        "title": "Phrases Complètes 1 : Action sur un Objet",
        "titleAr": "الفِعْلُ وَالفَاعِلُ وَالمَفْعُولُ بِه",
        "description": "Lis des phrases à 3 éléments (Sujet + Verbe + Objet).",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#D97706",
          "#B45309"
        ],
        "items": [
          {
            "id": "qaraa_alwalad_alkitaab",
            "grapheme": "قَرَأَ الوَلَدُ الكِتَابَ",
            "audioText": "قَرَأَ الوَلَدُ الكِتَابَ",
            "phonemeDesc": "L'enfant a lu le livre",
            "transliteration": "",
            "distractors": [
              "كَتَبَ الطَّالِبُ الدَّرْسَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ",
              "أَكَلَ الوَلَدُ التَّمْرَ"
            ],
            "phonemeDescEn": "The child read the book"
          },
          {
            "id": "kataba_attaalib_addars",
            "grapheme": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "audioText": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "phonemeDesc": "L'élève a écrit la leçon",
            "transliteration": "",
            "distractors": [
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "فَتَحَ الأَبُ البَابَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ"
            ],
            "phonemeDescEn": "The student wrote the lesson"
          },
          {
            "id": "shariba_attifl_alhaleeb",
            "grapheme": "شَرِبَ الطِّفْلُ الحَلِيبَ",
            "audioText": "شَرِبَ الطِّفْلُ الحَلِيبَ",
            "phonemeDesc": "L'enfant a bu le lait",
            "transliteration": "",
            "distractors": [
              "أَكَلَ الوَلَدُ التَّمْرَ",
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ],
            "phonemeDescEn": "The child drank the milk"
          },
          {
            "id": "akala_alwalad_attamr",
            "grapheme": "أَكَلَ الوَلَدُ التَّمْرَ",
            "audioText": "أَكَلَ الوَلَدُ التَّمْرَ",
            "phonemeDesc": "Le garçon a mangé la datte",
            "transliteration": "",
            "distractors": [
              "شَرِبَ الطِّفْلُ الحَلِيبَ",
              "فَتَحَ الأَبُ البَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Complete Sentences 1: Action on an Object",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 61,
        "worldId": 8,
        "title": "Phrases Complètes 2 : Gestes du Quotidien",
        "titleAr": "أَعْمَالُ اليَوْمِ وَالحَيَاة",
        "description": "Lis des actions concrètes de la vie de tous les jours.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#9333EA",
          "#6B21A8"
        ],
        "items": [
          {
            "id": "fataha_alab_albaab",
            "grapheme": "فَتَحَ الأَبُ البَابَ",
            "audioText": "فَتَحَ الأَبُ البَابَ",
            "phonemeDesc": "Le père a ouvert la porte",
            "transliteration": "",
            "distractors": [
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ],
            "phonemeDescEn": "The father opened the door"
          },
          {
            "id": "rasama_alwalad_ashshajara",
            "grapheme": "رَسَمَ الوَلَدُ الشَّجَرَةَ",
            "audioText": "رَسَمَ الوَلَدُ الشَّجَرَةَ",
            "phonemeDesc": "L'enfant a dessiné l'arbre",
            "transliteration": "",
            "distractors": [
              "فَتَحَ الأَبُ البَابَ",
              "أَكَلَ الوَلَدُ التَّمْرَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ"
            ],
            "phonemeDescEn": "The child drew the tree"
          },
          {
            "id": "qaraa_alwalad_alkitaab",
            "grapheme": "قَرَأَ الوَلَدُ الكِتَابَ",
            "audioText": "قَرَأَ الوَلَدُ الكِتَابَ",
            "phonemeDesc": "L'enfant a lu le livre",
            "transliteration": "",
            "distractors": [
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "فَتَحَ الأَبُ البَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ],
            "phonemeDescEn": "The child read the book"
          },
          {
            "id": "kataba_attaalib_addars",
            "grapheme": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "audioText": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "phonemeDesc": "L'élève a écrit la leçon",
            "transliteration": "",
            "distractors": [
              "فَتَحَ الأَبُ البَابَ",
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "أَكَلَ الوَلَدُ التَّمْرَ"
            ],
            "phonemeDescEn": "The student wrote the lesson"
          }
        ],
        "wordItems": [],
        "titleEn": "Complete Sentences 2: Daily Life Actions",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 62,
        "worldId": 8,
        "title": "Politesse & Expressions Usuelles",
        "titleAr": "التَّحِيَّاتُ وَآدَابُ الحِوَار",
        "description": "Reconnais les formules de politesse et de salutation arabes.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#059669",
          "#065F46"
        ],
        "items": [
          {
            "id": "assalamu_alaykum",
            "grapheme": "السَّلَامُ عَلَيْكُمْ",
            "audioText": "السَّلَامُ عَلَيْكُمْ",
            "phonemeDesc": "Que la paix soit sur vous",
            "transliteration": "",
            "distractors": [
              "أَهْلًا وَسَهْلًا",
              "شُكْرًا جَزِيلًا",
              "صَبَاحُ الخَيْرِ"
            ],
            "phonemeDescEn": "Peace be upon you"
          },
          {
            "id": "ahlan_wa_sahlan",
            "grapheme": "أَهْلًا وَسَهْلًا",
            "audioText": "أَهْلًا وَسَهْلًا",
            "phonemeDesc": "Bienvenue",
            "transliteration": "",
            "distractors": [
              "السَّلَامُ عَلَيْكُمْ",
              "مَسَاءُ الخَيْرِ",
              "شُكْرًا جَزِيلًا"
            ],
            "phonemeDescEn": "Welcome"
          },
          {
            "id": "shukran_jazeelan",
            "grapheme": "شُكْرًا جَزِيلًا",
            "audioText": "شُكْرًا جَزِيلًا",
            "phonemeDesc": "Merci beaucoup",
            "transliteration": "",
            "distractors": [
              "صَبَاحُ الخَيْرِ",
              "أَهْلًا وَسَهْلًا",
              "السَّلَامُ عَلَيْكُمْ"
            ],
            "phonemeDescEn": "Thank you very much"
          },
          {
            "id": "sabahu_alkhayr",
            "grapheme": "صَبَاحُ الخَيْرِ",
            "audioText": "صَبَاحُ الخَيْرِ",
            "phonemeDesc": "Bonjour",
            "transliteration": "",
            "distractors": [
              "مَسَاءُ الخَيْرِ",
              "شُكْرًا جَزِيلًا",
              "أَهْلًا وَسَهْلًا"
            ]
          },
          {
            "id": "masau_alkhayr",
            "grapheme": "مَسَاءُ الخَيْرِ",
            "audioText": "مَسَاءُ الخَيْرِ",
            "phonemeDesc": "Bonsoir",
            "transliteration": "",
            "distractors": [
              "صَبَاحُ الخَيْرِ",
              "السَّلَامُ عَلَيْكُمْ",
              "شُكْرًا جَزِيلًا"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Politeness & Common Expressions",
        "descriptionEn": "Recognize the correct Arabic phrase and meaning."
      },
      {
        "id": 63,
        "worldId": 8,
        "title": "Phrases avec Prépositions (في, إلى, على, فوق)",
        "titleAr": "حُرُوفُ الجَرِّ وَتَرْكِيبُ المَعَانِي",
        "description": "Lis des phrases indiquant des lieux et des positions précises.",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#075985"
        ],
        "items": [
          {
            "id": "dhahaba_alwalad_ilal_madrasa",
            "grapheme": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "audioText": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "phonemeDesc": "L'enfant est allé à l'école",
            "transliteration": "",
            "distractors": [
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "الكِتَابُ فِي الحَقِيبَةِ",
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ"
            ],
            "phonemeDescEn": "The child went to school"
          },
          {
            "id": "jalasa_alab_alal_kursiyy",
            "grapheme": "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
            "audioText": "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
            "phonemeDesc": "Le père s'est assis sur la chaise",
            "transliteration": "",
            "distractors": [
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "الكِتَابُ فِي الحَقِيبَةِ",
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ"
            ],
            "phonemeDescEn": "The father sat on the chair"
          },
          {
            "id": "alkitaab_fil_haqeeba",
            "grapheme": "الكِتَابُ فِي الحَقِيبَةِ",
            "audioText": "الكِتَابُ فِي الحَقِيبَةِ",
            "phonemeDesc": "Le livre est dans le cartable",
            "transliteration": "",
            "distractors": [
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ"
            ],
            "phonemeDescEn": "The book is in the schoolbag"
          },
          {
            "id": "alousfoor_fawqa_ashshajara",
            "grapheme": "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
            "audioText": "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
            "phonemeDesc": "L'oiseau est sur l'arbre",
            "transliteration": "",
            "distractors": [
              "الكِتَابُ فِي الحَقِيبَةِ",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ"
            ]
          }
        ],
        "wordItems": [],
        "titleEn": "Sentences with Prepositions (fee, ilā, 'alā)",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 64,
        "worldId": 8,
        "title": "Mini-Histoires & Compréhension",
        "titleAr": "قِصَصٌ قَصِيرَةٌ وَفَهْمُ المَعْنَى",
        "description": "Lis de courtes histoires enrichies d'adjectifs.",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#C026D3",
          "#701A75"
        ],
        "items": [
          {
            "id": "qaraa_ahmad_kitaaban_mufeedan",
            "grapheme": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "audioText": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "phonemeDesc": "Ahmad a lu un livre instructif",
            "transliteration": "",
            "distractors": [
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ"
            ],
            "phonemeDescEn": "Ahmad read an instructive book"
          },
          {
            "id": "dhahabat_fatima_ilal_hadeeqa",
            "grapheme": "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
            "audioText": "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
            "phonemeDesc": "Fatima est allée au jardin",
            "transliteration": "",
            "distractors": [
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "الكِتَابُ فِي الحَقِيبَةِ"
            ],
            "phonemeDescEn": "Fatima went to the garden"
          },
          {
            "id": "akala_alwalad_tuffahatan",
            "grapheme": "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
            "audioText": "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
            "phonemeDesc": "Le garçon a mangé une délicieuse pomme",
            "transliteration": "",
            "distractors": [
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ"
            ],
            "phonemeDescEn": "The boy ate a delicious apple"
          }
        ],
        "wordItems": [],
        "titleEn": "Short Stories & Comprehension",
        "descriptionEn": "Listen and read the complete sentence with accuracy."
      },
      {
        "id": 65,
        "worldId": 8,
        "title": "🏆 Grand Championnat de Lecture Fluide",
        "titleAr": "بُطُولَةُ القِرَاءَةِ الطَّلِقَةِ الكُبْرَى",
        "description": "Le test suprême de lecture et de compréhension de la langue arabe !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#E11D48",
          "#881337"
        ],
        "items": [
          {
            "id": "qaraa_alwalad_alkitaab",
            "grapheme": "قَرَأَ الوَلَدُ الكِتَابَ",
            "audioText": "قَرَأَ الوَلَدُ الكِتَابَ",
            "phonemeDesc": "L'enfant a lu le livre",
            "transliteration": "",
            "distractors": [
              "كَتَبَ الطَّالِبُ الدَّرْسَ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ],
            "phonemeDescEn": "The child read the book"
          },
          {
            "id": "dhahaba_alwalad_ilal_madrasa",
            "grapheme": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "audioText": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "phonemeDesc": "L'enfant est allé à l'école",
            "transliteration": "",
            "distractors": [
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "البَيْتُ كَبِيرٌ"
            ],
            "phonemeDescEn": "The child went to school"
          },
          {
            "id": "ashshams_mushriqa",
            "grapheme": "الشَّمْسُ مُشْرِقَةٌ",
            "audioText": "الشَّمْسُ مُشْرِقَةٌ",
            "phonemeDesc": "Le soleil brille",
            "transliteration": "",
            "distractors": [
              "القَمَرُ مُنِيرٌ",
              "المَاءُ بَارِدٌ",
              "الكِتَابُ مُفِيدٌ"
            ],
            "phonemeDescEn": "The sun is shining"
          },
          {
            "id": "assalamu_alaykum",
            "grapheme": "السَّلَامُ عَلَيْكُمْ",
            "audioText": "السَّلَامُ عَلَيْكُمْ",
            "phonemeDesc": "Que la paix soit sur vous",
            "transliteration": "",
            "distractors": [
              "أَهْلًا وَسَهْلًا",
              "شُكْرًا جَزِيلًا",
              "صَبَاحُ الخَيْرِ"
            ],
            "phonemeDescEn": "Peace be upon you"
          },
          {
            "id": "qaraa_ahmad_kitaaban_mufeedan",
            "grapheme": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "audioText": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "phonemeDesc": "Ahmad a lu un livre instructif",
            "transliteration": "",
            "distractors": [
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ],
            "phonemeDescEn": "Ahmad read an instructive book"
          }
        ],
        "wordItems": [],
        "titleEn": "🏆 Grand Championship de Lecture Fluide",
        "descriptionEn": "Listen attentively and select the corresponding letter or sign."
      }
    ],
    "nameEn": "World 8: Short Sentences & Fluency",
    "descriptionEn": "Read nominal and verbal sentences with prepositions and fluent reading."
  }
];
