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
        "description": "Écoute le son phonétique et attrape la bonne lettre.",
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
            "phonemeDesc": "Alif",
            "transliteration": "a",
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
            "phonemeDesc": "Ba",
            "transliteration": "ba",
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
            "phonemeDesc": "Ta",
            "transliteration": "ta",
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
            "phonemeDesc": "Tha",
            "transliteration": "tha",
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
            "phonemeDesc": "Alif",
            "transliteration": "a",
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
            "phonemeDesc": "Ba",
            "transliteration": "ba",
            "distractors": [
              "ث",
              "أ",
              "ت"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Jeem (Ja)",
            "transliteration": "ja",
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
            "phonemeDesc": "Ḥa (gorge)",
            "transliteration": "ḥa",
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
            "phonemeDesc": "Kha",
            "transliteration": "kha",
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
            "phonemeDesc": "Dal (Da)",
            "transliteration": "da",
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
            "phonemeDesc": "Jeem",
            "transliteration": "ja",
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
            "phonemeDesc": "Ḥa",
            "transliteration": "ḥa",
            "distractors": [
              "د",
              "ج",
              "خ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 3,
        "worldId": 1,
        "title": "Groupe 3 : ذ, ر, ز, س",
        "titleAr": "ذ ، ر ، ز ، س",
        "description": "Écoute bien les sons Dha, Ra, Za et Sa.",
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
            "phonemeDesc": "Dhal (Dha)",
            "transliteration": "dha",
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
            "phonemeDesc": "Ra",
            "transliteration": "ra",
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
            "phonemeDesc": "Zay (Za)",
            "transliteration": "za",
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
            "phonemeDesc": "Seen (Sa)",
            "transliteration": "sa",
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
            "phonemeDesc": "Ra",
            "transliteration": "ra",
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
            "phonemeDesc": "Za",
            "transliteration": "za",
            "distractors": [
              "س",
              "ر",
              "ذ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Sheen (Sha)",
            "transliteration": "sha",
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
            "phonemeDesc": "Ṣad (emphatique)",
            "transliteration": "ṣa",
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
            "phonemeDesc": "Ḍad (emphatique)",
            "transliteration": "ḍa",
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
            "phonemeDesc": "Ṭa (emphatique)",
            "transliteration": "ṭa",
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
            "phonemeDesc": "Sha",
            "transliteration": "sha",
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
            "phonemeDesc": "Ṣad",
            "transliteration": "ṣa",
            "distractors": [
              "ض",
              "ش",
              "ط"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ẓa",
            "transliteration": "ẓa",
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
            "phonemeDesc": "ʿAyn (gorge)",
            "transliteration": "ʿa",
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
            "phonemeDesc": "Ghayn",
            "transliteration": "gha",
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
            "phonemeDesc": "Fa",
            "transliteration": "fa",
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
            "phonemeDesc": "Ayn",
            "transliteration": "ʿa",
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
            "phonemeDesc": "Ghayn",
            "transliteration": "gha",
            "distractors": [
              "ع",
              "ظ",
              "ف"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Qaf (gorge)",
            "transliteration": "qa",
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
            "phonemeDesc": "Kaf",
            "transliteration": "ka",
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
            "phonemeDesc": "Lam",
            "transliteration": "la",
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
            "phonemeDesc": "Meem",
            "transliteration": "ma",
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
            "phonemeDesc": "Qaf",
            "transliteration": "qa",
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
            "phonemeDesc": "Kaf",
            "transliteration": "ka",
            "distractors": [
              "م",
              "ق",
              "ل"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Noon",
            "transliteration": "na",
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
            "phonemeDesc": "Haa (douce)",
            "transliteration": "ha",
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
            "phonemeDesc": "Waw",
            "transliteration": "wa",
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
            "phonemeDesc": "Yaa",
            "transliteration": "ya",
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
            "phonemeDesc": "Noon",
            "transliteration": "na",
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
            "phonemeDesc": "Yaa",
            "transliteration": "ya",
            "distractors": [
              "هـ",
              "ن",
              "و"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ba (1 point bas)",
            "transliteration": "ba",
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
            "phonemeDesc": "Ta (2 points haut)",
            "transliteration": "ta",
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
            "phonemeDesc": "Tha (3 points haut)",
            "transliteration": "tha",
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
            "phonemeDesc": "Noon (1 point haut)",
            "transliteration": "na",
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
            "phonemeDesc": "Yaa (2 points bas)",
            "transliteration": "ya",
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
            "phonemeDesc": "Tha",
            "transliteration": "tha",
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
            "phonemeDesc": "Ba",
            "transliteration": "ba",
            "distractors": [
              "ي",
              "ث",
              "ت"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ḥa (gorge)",
            "transliteration": "ḥa",
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
            "phonemeDesc": "Kha",
            "transliteration": "kha",
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
            "phonemeDesc": "Ṣad (épais)",
            "transliteration": "ṣa",
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
            "phonemeDesc": "Ṭa (épais)",
            "transliteration": "ṭa",
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
            "phonemeDesc": "ʿAyn (gorge)",
            "transliteration": "ʿa",
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
            "phonemeDesc": "Qaf (gorge)",
            "transliteration": "qa",
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
            "phonemeDesc": "Ghayn",
            "transliteration": "gha",
            "distractors": [
              "ع",
              "خ",
              "ق"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Alif",
            "transliteration": "a",
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
            "phonemeDesc": "Jeem",
            "transliteration": "j",
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
            "phonemeDesc": "Sad",
            "transliteration": "ṣ",
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
            "phonemeDesc": "Ttaa",
            "transliteration": "ṭ",
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
            "phonemeDesc": "Ayn",
            "transliteration": "ʿ",
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
            "phonemeDesc": "Qaf",
            "transliteration": "q",
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
            "phonemeDesc": "Kaf",
            "transliteration": "k",
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
            "phonemeDesc": "Meem",
            "transliteration": "m",
            "distractors": [
              "ن",
              "ل",
              "و"
            ]
          }
        ],
        "wordItems": []
      }
    ]
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
            "phonemeDesc": "Ba début",
            "transliteration": "b-",
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
            "phonemeDesc": "Ta début",
            "transliteration": "t-",
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
            "phonemeDesc": "Tha début",
            "transliteration": "th-",
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
            "phonemeDesc": "Jeem début",
            "transliteration": "j-",
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
            "phonemeDesc": "Ḥa début",
            "transliteration": "ḥ-",
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
            "phonemeDesc": "Kha début",
            "transliteration": "kh-",
            "distractors": [
              "حـ",
              "جـ",
              "غـ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Seen début",
            "transliteration": "s-",
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
            "phonemeDesc": "Sheen début",
            "transliteration": "sh-",
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
            "phonemeDesc": "Ṣad début",
            "transliteration": "ṣ-",
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
            "phonemeDesc": "Ayn début",
            "transliteration": "ʿ-",
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
            "phonemeDesc": "Kaf début",
            "transliteration": "k-",
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
            "phonemeDesc": "Lam début",
            "transliteration": "l-",
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
            "phonemeDesc": "Meem début",
            "transliteration": "m-",
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
            "phonemeDesc": "Noon début",
            "transliteration": "n-",
            "distractors": [
              "بـ",
              "تـ",
              "يـ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ba milieu",
            "transliteration": "-b-",
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
            "phonemeDesc": "Ta milieu",
            "transliteration": "-t-",
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
            "phonemeDesc": "Tha milieu",
            "transliteration": "-th-",
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
            "phonemeDesc": "Jeem milieu",
            "transliteration": "-j-",
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
            "phonemeDesc": "Ḥa milieu",
            "transliteration": "-ḥ-",
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
            "phonemeDesc": "Kha milieu",
            "transliteration": "-kh-",
            "distractors": [
              "ـحـ",
              "ـغـ",
              "ـجـ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Seen milieu",
            "transliteration": "-s-",
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
            "phonemeDesc": "Sheen milieu",
            "transliteration": "-sh-",
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
            "phonemeDesc": "Ṣad milieu",
            "transliteration": "-ṣ-",
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
            "phonemeDesc": "Ayn milieu",
            "transliteration": "-ʿ-",
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
            "phonemeDesc": "Kaf milieu",
            "transliteration": "-k-",
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
            "phonemeDesc": "Lam milieu",
            "transliteration": "-l-",
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
            "phonemeDesc": "Meem milieu",
            "transliteration": "-m-",
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
            "phonemeDesc": "Yaa milieu",
            "transliteration": "-y-",
            "distractors": [
              "ـبـ",
              "ـتـ",
              "ـنـ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ba fin",
            "transliteration": "-b",
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
            "phonemeDesc": "Ta fin",
            "transliteration": "-t",
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
            "phonemeDesc": "Tha fin",
            "transliteration": "-th",
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
            "phonemeDesc": "Jeem fin",
            "transliteration": "-j",
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
            "phonemeDesc": "Ḥa fin",
            "transliteration": "-ḥ",
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
            "phonemeDesc": "Kha fin",
            "transliteration": "-kh",
            "distractors": [
              "ـح",
              "ـج",
              "ـغ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Seen fin",
            "transliteration": "-s",
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
            "phonemeDesc": "Sheen fin",
            "transliteration": "-sh",
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
            "phonemeDesc": "Ṣad fin",
            "transliteration": "-ṣ",
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
            "phonemeDesc": "Lam fin",
            "transliteration": "-l",
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
            "phonemeDesc": "Meem fin",
            "transliteration": "-m",
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
            "phonemeDesc": "Noon fin",
            "transliteration": "-n",
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
            "phonemeDesc": "Yaa fin",
            "transliteration": "-y",
            "distractors": [
              "ـب",
              "ـت",
              "ـن"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Alif",
            "transliteration": "a",
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
            "phonemeDesc": "Dal",
            "transliteration": "d",
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
            "phonemeDesc": "Dhal",
            "transliteration": "dh",
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
            "phonemeDesc": "Ra",
            "transliteration": "r",
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
            "phonemeDesc": "Zay",
            "transliteration": "z",
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
            "phonemeDesc": "Waw",
            "transliteration": "w",
            "distractors": [
              "ر",
              "ز",
              "فـ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Au début",
            "transliteration": "b-",
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
            "phonemeDesc": "Au milieu",
            "transliteration": "-j-",
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
            "phonemeDesc": "À la fin",
            "transliteration": "-s",
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
            "phonemeDesc": "Au début",
            "transliteration": "k-",
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
            "phonemeDesc": "Au milieu",
            "transliteration": "-ʿ-",
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
            "phonemeDesc": "À la fin",
            "transliteration": "-l",
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
            "phonemeDesc": "Au début",
            "transliteration": "m-",
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
            "phonemeDesc": "À la fin",
            "transliteration": "-n",
            "distractors": [
              "نـ",
              "ـنـ",
              "ن"
            ]
          }
        ],
        "wordItems": []
      }
    ]
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
        "description": "Écoute le son ouvert \"A\" (bref, 1 temps).",
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
            "phonemeDesc": "Ba",
            "transliteration": "ba",
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
            "phonemeDesc": "Ta",
            "transliteration": "ta",
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
            "phonemeDesc": "Da",
            "transliteration": "da",
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
            "phonemeDesc": "Ra",
            "transliteration": "ra",
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
            "phonemeDesc": "Sa",
            "transliteration": "sa",
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
            "phonemeDesc": "Ma",
            "transliteration": "ma",
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
            "phonemeDesc": "Na",
            "transliteration": "na",
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
            "phonemeDesc": "Ya",
            "transliteration": "ya",
            "distractors": [
              "يُ",
              "يِ",
              "تَ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ṣa",
            "transliteration": "ṣa",
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
            "phonemeDesc": "Ḍa",
            "transliteration": "ḍa",
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
            "phonemeDesc": "Ṭa",
            "transliteration": "ṭa",
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
            "phonemeDesc": "Ẓa",
            "transliteration": "ẓa",
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
            "phonemeDesc": "ʿA",
            "transliteration": "ʿa",
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
            "phonemeDesc": "Gha",
            "transliteration": "gha",
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
            "phonemeDesc": "Qa",
            "transliteration": "qa",
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
            "phonemeDesc": "Ḥa",
            "transliteration": "ḥa",
            "distractors": [
              "خَ",
              "جَ",
              "هَ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 21,
        "worldId": 3,
        "title": "La Ḍammah (ـُ) - Sons \"OU\" de base",
        "titleAr": "الضَّمَّة ( ـُ ) - الحُرُوف البَسِيطَة",
        "description": "Écoute le son arrondi \"OU\" (bref, 1 temps).",
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
            "phonemeDesc": "Bou",
            "transliteration": "bu",
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
            "phonemeDesc": "Tou",
            "transliteration": "tu",
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
            "phonemeDesc": "Dou",
            "transliteration": "du",
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
            "phonemeDesc": "Rou",
            "transliteration": "ru",
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
            "phonemeDesc": "Sou",
            "transliteration": "su",
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
            "phonemeDesc": "Mou",
            "transliteration": "mu",
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
            "phonemeDesc": "Nou",
            "transliteration": "nu",
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
            "phonemeDesc": "Wou",
            "transliteration": "wu",
            "distractors": [
              "وَ",
              "وِ",
              "رُ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Djou",
            "transliteration": "ju",
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
            "phonemeDesc": "Ṣou",
            "transliteration": "ṣu",
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
            "phonemeDesc": "Ḍou",
            "transliteration": "ḍu",
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
            "phonemeDesc": "Ṭou",
            "transliteration": "ṭu",
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
            "phonemeDesc": "Kou",
            "transliteration": "ku",
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
            "phonemeDesc": "Lou",
            "transliteration": "lu",
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
            "phonemeDesc": "Qou",
            "transliteration": "qu",
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
            "phonemeDesc": "ʿOu",
            "transliteration": "ʿu",
            "distractors": [
              "غُ",
              "حُ",
              "أُ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 23,
        "worldId": 3,
        "title": "La Kasrah (ـِ) - Sons \"I\" de base",
        "titleAr": "الكَسْرَة ( ـِ ) - الحُرُوف البَسِيطَة",
        "description": "Écoute le son tiré \"I\" (bref, 1 temps).",
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
            "phonemeDesc": "Bi",
            "transliteration": "bi",
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
            "phonemeDesc": "Ti",
            "transliteration": "ti",
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
            "phonemeDesc": "Di",
            "transliteration": "di",
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
            "phonemeDesc": "Ri",
            "transliteration": "ri",
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
            "phonemeDesc": "Si",
            "transliteration": "si",
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
            "phonemeDesc": "Mi",
            "transliteration": "mi",
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
            "phonemeDesc": "Ni",
            "transliteration": "ni",
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
            "phonemeDesc": "Yi",
            "transliteration": "yi",
            "distractors": [
              "يَ",
              "يُ",
              "تِ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Dji",
            "transliteration": "ji",
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
            "phonemeDesc": "Ṣi",
            "transliteration": "ṣi",
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
            "phonemeDesc": "Ṭi",
            "transliteration": "ṭi",
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
            "phonemeDesc": "ʿI",
            "transliteration": "ʿi",
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
            "phonemeDesc": "Qi",
            "transliteration": "qi",
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
            "phonemeDesc": "Ki",
            "transliteration": "ki",
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
            "phonemeDesc": "Li",
            "transliteration": "li",
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
            "phonemeDesc": "Fi",
            "transliteration": "fi",
            "distractors": [
              "قِ",
              "غِ",
              "بِ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ba (A)",
            "transliteration": "ba",
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
            "phonemeDesc": "Bou (OU)",
            "transliteration": "bu",
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
            "phonemeDesc": "Bi (I)",
            "transliteration": "bi",
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
            "phonemeDesc": "Ta (A)",
            "transliteration": "ta",
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
            "phonemeDesc": "Tou (OU)",
            "transliteration": "tu",
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
            "phonemeDesc": "Ti (I)",
            "transliteration": "ti",
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
            "phonemeDesc": "Da (A)",
            "transliteration": "da",
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
            "phonemeDesc": "Dou (OU)",
            "transliteration": "du",
            "distractors": [
              "دَ",
              "دِ",
              "رُ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ka",
            "transliteration": "ka",
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
            "phonemeDesc": "Kou",
            "transliteration": "ku",
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
            "phonemeDesc": "Ki",
            "transliteration": "ki",
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
            "phonemeDesc": "La",
            "transliteration": "la",
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
            "phonemeDesc": "Lou",
            "transliteration": "lu",
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
            "phonemeDesc": "Li",
            "transliteration": "li",
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
            "phonemeDesc": "Sa",
            "transliteration": "sa",
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
            "phonemeDesc": "Si",
            "transliteration": "si",
            "distractors": [
              "سَ",
              "سُ",
              "شِ"
            ]
          }
        ],
        "wordItems": []
      }
    ]
  },
  {
    "id": 4,
    "name": "Monde 4 : Les Combinaisons de 2 Voyelles",
    "nameAr": "العالم الرابع : تَرْكِيبُ الحَرَكَاتِ الثُّنَائِيَّة",
    "description": "Enchaîne avec fluidité deux lettres portant des voyelles courtes (Fatḥah, Ḍammah, Kasrah) !",
    "icon": "layers",
    "color": "#F59E0B",
    "levels": [
      {
        "id": 27,
        "worldId": 4,
        "title": "Série A + A (Fatḥah - Fatḥah)",
        "titleAr": "فَتْحَة + فَتْحَة (بَتَ ، دَرَ ، كَتَ)",
        "description": "Lis et assemble tes premières combinaisons à 2 Fatḥah !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#F59E0B",
          "#B45309"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "bata",
            "word": "بَتَ",
            "meaning": "Ba-Ta",
            "translationFr": "Ba-Ta",
            "letters": [
              "بَ",
              "تَ"
            ],
            "distractorLetters": [
              "نَ",
              "دَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "dara",
            "word": "دَرَ",
            "meaning": "Da-Ra",
            "translationFr": "Da-Ra",
            "letters": [
              "دَ",
              "رَ"
            ],
            "distractorLetters": [
              "زَ",
              "ذَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "kata",
            "word": "كَتَ",
            "meaning": "Ka-Ta",
            "translationFr": "Ka-Ta",
            "letters": [
              "كَ",
              "تَ"
            ],
            "distractorLetters": [
              "قَ",
              "بَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "sama",
            "word": "سَمَ",
            "meaning": "Sa-Ma",
            "translationFr": "Sa-Ma",
            "letters": [
              "سَ",
              "مَ"
            ],
            "distractorLetters": [
              "شَ",
              "نَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "rasa",
            "word": "رَسَ",
            "meaning": "Ra-Sa",
            "translationFr": "Ra-Sa",
            "letters": [
              "رَ",
              "سَ"
            ],
            "distractorLetters": [
              "دَ",
              "صَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "maa_particle",
            "word": "مَعَ",
            "meaning": "Avec (Ma'a)",
            "translationFr": "Avec",
            "letters": [
              "مَ",
              "عَ"
            ],
            "distractorLetters": [
              "غَ",
              "لَ"
            ],
            "emoji": "🤝"
          },
          {
            "id": "laka",
            "word": "لَكَ",
            "meaning": "Pour toi (La-Ka)",
            "translationFr": "Pour toi",
            "letters": [
              "لَ",
              "كَ"
            ],
            "distractorLetters": [
              "بَ",
              "كُ"
            ],
            "emoji": "🎁"
          }
        ]
      },
      {
        "id": 28,
        "worldId": 4,
        "title": "Série A + OU (Fatḥah - Ḍammah)",
        "titleAr": "فَتْحَة + ضَمَّة (بَبُ ، كَتُ ، دَرُ)",
        "description": "Passe du son 'A' au son 'OU' avec agilité !",
        "gameType": "wordBuilder",
        "requiredStars": 0,
        "bgColor": [
          "#EA580C",
          "#9A3412"
        ],
        "items": [],
        "wordItems": [
          {
            "id": "babu",
            "word": "بَبُ",
            "meaning": "Ba-Bou",
            "translationFr": "Ba-Bou",
            "letters": [
              "بَ",
              "بُ"
            ],
            "distractorLetters": [
              "تُ",
              "بِ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "katu",
            "word": "كَتُ",
            "meaning": "Ka-Tou",
            "translationFr": "Ka-Tou",
            "letters": [
              "كَ",
              "تُ"
            ],
            "distractorLetters": [
              "قَ",
              "تَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "daru",
            "word": "دَرُ",
            "meaning": "Da-Rou",
            "translationFr": "Da-Rou",
            "letters": [
              "دَ",
              "رُ"
            ],
            "distractorLetters": [
              "ذَ",
              "رَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "samu",
            "word": "سَمُ",
            "meaning": "Sa-Mou",
            "translationFr": "Sa-Mou",
            "letters": [
              "سَ",
              "مُ"
            ],
            "distractorLetters": [
              "شَ",
              "مَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "qatu",
            "word": "قَتُ",
            "meaning": "Qa-Tou",
            "translationFr": "Qa-Tou",
            "letters": [
              "قَ",
              "تُ"
            ],
            "distractorLetters": [
              "كُ",
              "تَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "nabu",
            "word": "نَبُ",
            "meaning": "Na-Bou",
            "translationFr": "Na-Bou",
            "letters": [
              "نَ",
              "بُ"
            ],
            "distractorLetters": [
              "بَ",
              "نُ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "tadu",
            "word": "تَدُ",
            "meaning": "Ta-Dou",
            "translationFr": "Ta-Dou",
            "letters": [
              "تَ",
              "دُ"
            ],
            "distractorLetters": [
              "ثَ",
              "دَ"
            ],
            "emoji": "🔤"
          }
        ]
      },
      {
        "id": 29,
        "worldId": 4,
        "title": "Série A + I (Fatḥah - Kasrah)",
        "titleAr": "فَتْحَة + كَسْرَة (بَرِ ، دَرِ ، سَمِ)",
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
            "id": "bari",
            "word": "بَرِ",
            "meaning": "Ba-Ri",
            "translationFr": "Ba-Ri",
            "letters": [
              "بَ",
              "رِ"
            ],
            "distractorLetters": [
              "تِ",
              "بُ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "dari",
            "word": "دَرِ",
            "meaning": "Da-Ri",
            "translationFr": "Da-Ri",
            "letters": [
              "دَ",
              "رِ"
            ],
            "distractorLetters": [
              "رَ",
              "دِ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "sami_short",
            "word": "سَمِ",
            "meaning": "Sa-Mi",
            "translationFr": "Sa-Mi",
            "letters": [
              "سَ",
              "مِ"
            ],
            "distractorLetters": [
              "سُ",
              "مَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "kati",
            "word": "كَتِ",
            "meaning": "Ka-Ti",
            "translationFr": "Ka-Ti",
            "letters": [
              "كَ",
              "تِ"
            ],
            "distractorLetters": [
              "كُ",
              "تَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "shari_short",
            "word": "شَرِ",
            "meaning": "Cha-Ri",
            "translationFr": "Cha-Ri",
            "letters": [
              "شَ",
              "رِ"
            ],
            "distractorLetters": [
              "سَ",
              "رُ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "ali_short",
            "word": "عَلِ",
            "meaning": "ʿA-Li",
            "translationFr": "ʿA-Li",
            "letters": [
              "عَ",
              "لِ"
            ],
            "distractorLetters": [
              "غَ",
              "لَ"
            ],
            "emoji": "🔤"
          }
        ]
      },
      {
        "id": 30,
        "worldId": 4,
        "title": "Séries OU + I & OU + A",
        "titleAr": "ضَمَّة + كَسْرَة / فَتْحَة (كُتِ ، قُرِ ، هُوَ)",
        "description": "Attrape les bulles des combinaisons débutant par le son 'OU' !",
        "gameType": "bubble",
        "requiredStars": 0,
        "bgColor": [
          "#10B981",
          "#047857"
        ],
        "items": [
          {
            "id": "kuti",
            "grapheme": "كُتِ",
            "audioText": "كُتِ",
            "phonemeDesc": "Kou-Ti",
            "transliteration": "kuti",
            "distractors": [
              "كَتَ",
              "كَتُ",
              "قُتِ"
            ]
          },
          {
            "id": "quri",
            "grapheme": "قُرِ",
            "audioText": "قُرِ",
            "phonemeDesc": "Qou-Ri",
            "transliteration": "quri",
            "distractors": [
              "قَرِ",
              "قُرُ",
              "كُرِ"
            ]
          },
          {
            "id": "sumi",
            "grapheme": "سُمِ",
            "audioText": "سُمِ",
            "phonemeDesc": "Sou-Mi",
            "transliteration": "sumi",
            "distractors": [
              "سَمِ",
              "سُمُ",
              "شُمِ"
            ]
          },
          {
            "id": "duri",
            "grapheme": "دُرِ",
            "audioText": "دُرِ",
            "phonemeDesc": "Dou-Ri",
            "transliteration": "duri",
            "distractors": [
              "دَرِ",
              "دُرُ",
              "ذُرِ"
            ]
          },
          {
            "id": "huwa",
            "grapheme": "هُوَ",
            "audioText": "هُوَ",
            "phonemeDesc": "Il (Hou-Wa)",
            "transliteration": "huwa",
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
            "phonemeDesc": "Rou-Ba",
            "transliteration": "ruba",
            "distractors": [
              "رَبَ",
              "رُبُ",
              "زُبَ"
            ]
          },
          {
            "id": "kuta",
            "grapheme": "كُتَ",
            "audioText": "كُتَ",
            "phonemeDesc": "Kou-Ta",
            "transliteration": "kuta",
            "distractors": [
              "كَتَ",
              "كُتِ",
              "قُتَ"
            ]
          },
          {
            "id": "dura",
            "grapheme": "دُرَ",
            "audioText": "دُرَ",
            "phonemeDesc": "Dou-Ra",
            "transliteration": "dura",
            "distractors": [
              "دَرَ",
              "دُرِ",
              "ذُرَ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 31,
        "worldId": 4,
        "title": "Série I + A & Défi Vitesse Mixte",
        "titleAr": "كَسْرَة + فَتْحَة وَالتَّحَدِّي المُمَيَّز",
        "description": "Vise la bonne cible parmi les différentes combinaisons de voyelles !",
        "gameType": "target",
        "requiredStars": 0,
        "bgColor": [
          "#0284C7",
          "#0369A1"
        ],
        "items": [
          {
            "id": "hiya",
            "grapheme": "هِيَ",
            "audioText": "هِيَ",
            "phonemeDesc": "Elle (Hi-Ya)",
            "transliteration": "hiya",
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
            "phonemeDesc": "Pourquoi (Li-Ma)",
            "transliteration": "lima",
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
            "phonemeDesc": "Par toi (Bi-Ka)",
            "transliteration": "bika",
            "distractors": [
              "بَكَ",
              "بُكَ",
              "بِتَ"
            ]
          },
          {
            "id": "bita",
            "grapheme": "بِتَ",
            "audioText": "بِتَ",
            "phonemeDesc": "Bi-Ta",
            "transliteration": "bita",
            "distractors": [
              "بَتَ",
              "بِكَ",
              "تِبَ"
            ]
          },
          {
            "id": "babu",
            "grapheme": "بَبُ",
            "audioText": "بَبُ",
            "phonemeDesc": "Ba-Bou",
            "transliteration": "babu",
            "distractors": [
              "بَتُ",
              "بُبَ",
              "بَبَ"
            ]
          },
          {
            "id": "katu",
            "grapheme": "كَتُ",
            "audioText": "كَتُ",
            "phonemeDesc": "Ka-Tou",
            "transliteration": "katu",
            "distractors": [
              "كَتَ",
              "كُتِ",
              "قَتُ"
            ]
          },
          {
            "id": "bari",
            "grapheme": "بَرِ",
            "audioText": "بَرِ",
            "phonemeDesc": "Ba-Ri",
            "transliteration": "bari",
            "distractors": [
              "بُرِ",
              "بَرُ",
              "دَرِ"
            ]
          },
          {
            "id": "kuti",
            "grapheme": "كُتِ",
            "audioText": "كُتِ",
            "phonemeDesc": "Kou-Ti",
            "transliteration": "kuti",
            "distractors": [
              "كَتِ",
              "كُتَ",
              "قُتِ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 32,
        "worldId": 4,
        "title": "Grand Atelier des 2 Voyelles",
        "titleAr": "الوَرْشَةُ الكُبْرَى لِتَرْكِيبِ الصَّوْتَيْن",
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
            "id": "bata",
            "word": "بَتَ",
            "meaning": "Ba-Ta",
            "translationFr": "Ba-Ta",
            "letters": [
              "بَ",
              "تَ"
            ],
            "distractorLetters": [
              "تُ",
              "بِ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "babu",
            "word": "بَبُ",
            "meaning": "Ba-Bou",
            "translationFr": "Ba-Bou",
            "letters": [
              "بَ",
              "بُ"
            ],
            "distractorLetters": [
              "بَ",
              "تُ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "katu",
            "word": "كَتُ",
            "meaning": "Ka-Tou",
            "translationFr": "Ka-Tou",
            "letters": [
              "كَ",
              "تُ"
            ],
            "distractorLetters": [
              "كُ",
              "تَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "bari",
            "word": "بَرِ",
            "meaning": "Ba-Ri",
            "translationFr": "Ba-Ri",
            "letters": [
              "بَ",
              "رِ"
            ],
            "distractorLetters": [
              "بُ",
              "رَ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "kuti",
            "word": "كُتِ",
            "meaning": "Kou-Ti",
            "translationFr": "Kou-Ti",
            "letters": [
              "كُ",
              "تِ"
            ],
            "distractorLetters": [
              "كَ",
              "تُ"
            ],
            "emoji": "🔤"
          },
          {
            "id": "huwa",
            "word": "هُوَ",
            "meaning": "Il (Hou-Wa)",
            "translationFr": "Il",
            "letters": [
              "هُ",
              "وَ"
            ],
            "distractorLetters": [
              "هَ",
              "وِ"
            ],
            "emoji": "👦"
          },
          {
            "id": "hiya",
            "word": "هِيَ",
            "meaning": "Elle (Hi-Ya)",
            "translationFr": "Elle",
            "letters": [
              "هِ",
              "يَ"
            ],
            "distractorLetters": [
              "هُ",
              "يُ"
            ],
            "emoji": "👧"
          },
          {
            "id": "bika",
            "word": "بِكَ",
            "meaning": "Par toi (Bi-Ka)",
            "translationFr": "Par toi",
            "letters": [
              "بِ",
              "كَ"
            ],
            "distractorLetters": [
              "بَ",
              "كُ"
            ],
            "emoji": "👉"
          }
        ]
      }
    ]
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
            "phonemeDesc": "Ab",
            "transliteration": "ab",
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
            "phonemeDesc": "At",
            "transliteration": "at",
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
            "phonemeDesc": "Bar",
            "transliteration": "bar",
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
            "phonemeDesc": "Bal",
            "transliteration": "bal",
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
            "phonemeDesc": "Min",
            "transliteration": "min",
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
            "phonemeDesc": "'An",
            "transliteration": "ʿan",
            "distractors": [
              "عَنَ",
              "مِنْ",
              "إِنْ"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Qul",
            "transliteration": "qul",
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
            "phonemeDesc": "Qoum",
            "transliteration": "qum",
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
            "phonemeDesc": "Qad",
            "transliteration": "qad",
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
            "phonemeDesc": "Hal",
            "transliteration": "hal",
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
            "phonemeDesc": "Kul",
            "transliteration": "kul",
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
            "phonemeDesc": "Bay",
            "transliteration": "bay",
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
            "phonemeDesc": "Sham",
            "transliteration": "sham",
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
            "phonemeDesc": "Tay",
            "transliteration": "tay",
            "distractors": [
              "طَيَ",
              "بَيْ",
              "حَيْ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 35,
        "worldId": 5,
        "title": "Madd Alif (ـَا) - Le son long \"Â\"",
        "titleAr": "مَدّ بِالأَلِف ( ـَا ) - 2 تَمْبس",
        "description": "Écoute le son long étiré avec Alif (2 temps bien tenus).",
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
            "phonemeDesc": "Bââ",
            "transliteration": "bā",
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
            "phonemeDesc": "Tââ",
            "transliteration": "tā",
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
            "phonemeDesc": "Dââ",
            "transliteration": "dā",
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
            "phonemeDesc": "Rââ",
            "transliteration": "rā",
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
            "phonemeDesc": "Bââ",
            "transliteration": "bā",
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
            "phonemeDesc": "Dââ",
            "transliteration": "dā",
            "distractors": [
              "دِي",
              "دَ",
              "دُو"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 36,
        "worldId": 5,
        "title": "Madd Waw (ـُو) - Le son long \"OUU\"",
        "titleAr": "مَدّ بِالوَاو ( ـُو ) - 2 تَمْبس",
        "description": "Prolonge la Ḍammah avec la lettre Waw (2 temps).",
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
            "phonemeDesc": "Bouu",
            "transliteration": "bū",
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
            "phonemeDesc": "Touu",
            "transliteration": "tū",
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
            "phonemeDesc": "Douu",
            "transliteration": "dū",
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
            "phonemeDesc": "Souu",
            "transliteration": "sū",
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
            "phonemeDesc": "Shouu",
            "transliteration": "shū",
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
            "phonemeDesc": "Bouu",
            "transliteration": "bū",
            "distractors": [
              "بِي",
              "بُ",
              "تُو"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 37,
        "worldId": 5,
        "title": "Madd Ya (ـِي) - Le son long \"II\"",
        "titleAr": "مَدّ بِاليَاء ( ـِي ) - 2 تَمْبس",
        "description": "Prolonge la Kasrah avec la lettre Ya (2 temps).",
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
            "phonemeDesc": "Biii",
            "transliteration": "bī",
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
            "phonemeDesc": "Tiii",
            "transliteration": "tī",
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
            "phonemeDesc": "Diii",
            "transliteration": "dī",
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
            "phonemeDesc": "Siii",
            "transliteration": "sī",
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
            "phonemeDesc": "Shiii",
            "transliteration": "shī",
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
            "phonemeDesc": "Riii",
            "transliteration": "rī",
            "distractors": [
              "رِ",
              "رَا",
              "زِي"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 38,
        "worldId": 5,
        "title": "Duel Court vs Long : Série A & OU",
        "titleAr": "المُقَارَنَة 1 : الفَتْحَة وَالضَّمَّة مَعَ المَدّ",
        "description": "Distingue immédiatement le son bref (1t) du son étiré (2t) !",
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
            "phonemeDesc": "Ba (court, 1t)",
            "transliteration": "ba",
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
            "phonemeDesc": "Bââ (long, 2t)",
            "transliteration": "bā",
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
            "phonemeDesc": "Ta (court, 1t)",
            "transliteration": "ta",
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
            "phonemeDesc": "Tââ (long, 2t)",
            "transliteration": "tā",
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
            "phonemeDesc": "Dou (court, 1t)",
            "transliteration": "du",
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
            "phonemeDesc": "Douuu (long, 2t)",
            "transliteration": "dū",
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
            "phonemeDesc": "Bou (court, 1t)",
            "transliteration": "bu",
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
            "phonemeDesc": "Bouuu (long, 2t)",
            "transliteration": "bū",
            "distractors": [
              "بُ",
              "بَا",
              "تُو"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 39,
        "worldId": 5,
        "title": "Duel Court vs Long : Série I & Mixte",
        "titleAr": "المُقَارَنَة 2 : الكَسْرَة وَالمَدّ بِاليَاء",
        "description": "Distingue immédiatement le son bref (1t) et le son étiré (2t) avec Kasrah & Ya.",
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
            "phonemeDesc": "Bi (court, 1t)",
            "transliteration": "bi",
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
            "phonemeDesc": "Biii (long, 2t)",
            "transliteration": "bī",
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
            "phonemeDesc": "Si (court, 1t)",
            "transliteration": "si",
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
            "phonemeDesc": "Siiii (long, 2t)",
            "transliteration": "sī",
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
            "phonemeDesc": "Ri (court, 1t)",
            "transliteration": "ri",
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
            "phonemeDesc": "Riii (long, 2t)",
            "transliteration": "rī",
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
            "phonemeDesc": "Ti (court, 1t)",
            "transliteration": "ti",
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
            "phonemeDesc": "Tiii (long, 2t)",
            "transliteration": "tī",
            "distractors": [
              "تِ",
              "بِي",
              "تَا"
            ]
          }
        ],
        "wordItems": []
      }
    ]
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
            "phonemeDesc": "Rabba (appuyé sur le B)",
            "transliteration": "rabba",
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
            "phonemeDesc": "Madda (appuyé sur le D)",
            "transliteration": "madda",
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
            "phonemeDesc": "'Allama (appuyé sur le L)",
            "transliteration": "ʿallama",
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
            "phonemeDesc": "Shadda (appuyé sur le D)",
            "transliteration": "shadda",
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
            "phonemeDesc": "Ḥassa (appuyé sur le S)",
            "transliteration": "ḥassa",
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
            "phonemeDesc": "Rabba",
            "transliteration": "rabba",
            "distractors": [
              "شَدَّ",
              "مَدَّ",
              "عَلَّمَ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 41,
        "worldId": 6,
        "title": "Le Tanwīn en -an (ـً) : Terminaison ouverte",
        "titleAr": "تَنْوِينُ الفَتْحِ : صَوْتُ أَنْ",
        "description": "Écoute la terminaison nasalisée en \"-an\".",
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
            "phonemeDesc": "Kitāban (-an)",
            "transliteration": "kitāban",
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
            "phonemeDesc": "Waladan (-an)",
            "transliteration": "waladan",
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
            "phonemeDesc": "Baytan (-an)",
            "transliteration": "baytan",
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
            "phonemeDesc": "Kitāban",
            "transliteration": "kitāban",
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
            "phonemeDesc": "Waladan",
            "transliteration": "waladan",
            "distractors": [
              "بَيْتًا",
              "كِتَابًا",
              "وَلَدٌ"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 42,
        "worldId": 6,
        "title": "Le Tanwīn en -oun (ـٌ) : Terminaison fermée",
        "titleAr": "تَنْوِينُ الضَّمِّ : صَوْتُ أُنْ",
        "description": "Écoute la terminaison nasalisée en \"-oun\".",
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
            "phonemeDesc": "Kitābun (-oun)",
            "transliteration": "kitābun",
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
            "phonemeDesc": "Waladun (-oun)",
            "transliteration": "waladun",
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
            "phonemeDesc": "Baytun (-oun)",
            "transliteration": "baytun",
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
            "phonemeDesc": "Kitābun",
            "transliteration": "kitābun",
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
            "phonemeDesc": "Waladun",
            "transliteration": "waladun",
            "distractors": [
              "بَيْتٌ",
              "كِتَابٌ",
              "وَلَدًا"
            ]
          }
        ],
        "wordItems": []
      },
      {
        "id": 43,
        "worldId": 6,
        "title": "Le Tanwīn en -in (ـٍ) & Grand Duel des 3 Tanwīns",
        "titleAr": "تَنْوِينُ الكَسْرِ وَتَحَدِّي التَّنْوِين",
        "description": "Distingue instantanément -an, -oun et -in !",
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
            "phonemeDesc": "Kitābin (-in)",
            "transliteration": "kitābin",
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
            "phonemeDesc": "Waladin (-in)",
            "transliteration": "waladin",
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
            "phonemeDesc": "Baytin (-in)",
            "transliteration": "baytin",
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
            "phonemeDesc": "Kitāban (-an)",
            "transliteration": "kitāban",
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
            "phonemeDesc": "Waladun (-oun)",
            "transliteration": "waladun",
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
            "phonemeDesc": "Baytin (-in)",
            "transliteration": "baytin",
            "distractors": [
              "بَيْتًا",
              "بَيْتٌ",
              "بَيْت"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Al-Qamar (Lām clair)",
            "transliteration": "al-qamaru",
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
            "phonemeDesc": "Al-Kitāb (Lām clair)",
            "transliteration": "al-kitābu",
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
            "phonemeDesc": "Al-Walad (Lām clair)",
            "transliteration": "al-waladu",
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
            "phonemeDesc": "Al-Qamar",
            "transliteration": "al-qamaru",
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
            "phonemeDesc": "Al-Kitāb",
            "transliteration": "al-kitābu",
            "distractors": [
              "القَمَر",
              "الوَلَد",
              "النَّجْم"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Ash-Shams (Lām assimilé)",
            "transliteration": "ash-shamsu",
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
            "phonemeDesc": "An-Najm (Lām assimilé)",
            "transliteration": "an-najmu",
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
            "phonemeDesc": "At-Tayr (Lām assimilé)",
            "transliteration": "at-tayru",
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
            "phonemeDesc": "Ash-Shams",
            "transliteration": "ash-shamsu",
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
            "phonemeDesc": "An-Najm",
            "transliteration": "an-najmu",
            "distractors": [
              "الشَّمْس",
              "الطَّيْر",
              "الكِتَاب"
            ]
          }
        ],
        "wordItems": []
      }
    ]
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
            "emoji": "✍️"
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
            "emoji": "📖"
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
            "emoji": "📚"
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
            "emoji": "🎨"
          }
        ]
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
            "emoji": "🪑"
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
            "emoji": "🚶"
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
            "emoji": "👂"
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
            "emoji": "🍽️"
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
            "emoji": "🥛"
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
            "emoji": "🚪"
          }
        ]
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
            "emoji": "🚪"
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
            "emoji": "🏠"
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
            "emoji": "🪑"
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
            "emoji": "🖥️"
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
            "emoji": "✏️"
          }
        ]
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
            "emoji": "🦁"
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
            "emoji": "🐪"
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
            "emoji": "🐘"
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
            "emoji": "🐦"
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
            "emoji": "🐱"
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
            "emoji": "🐶"
          }
        ]
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
            "emoji": "☀️"
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
            "emoji": "🌙"
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
            "emoji": "⭐"
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
            "emoji": "🌊"
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
            "emoji": "☁️"
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
            "emoji": "🌳"
          }
        ]
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
            "transliteration": "abun",
            "distractors": [
              "أُمّ",
              "أَخ",
              "أُخْت"
            ]
          },
          {
            "id": "umm",
            "grapheme": "أُمّ",
            "audioText": "أُمٌّ",
            "phonemeDesc": "Mère",
            "transliteration": "ummun",
            "distractors": [
              "أَب",
              "بِنْت",
              "وَلَد"
            ]
          },
          {
            "id": "akh",
            "grapheme": "أَخ",
            "audioText": "أَخٌ",
            "phonemeDesc": "Frère",
            "transliteration": "akhun",
            "distractors": [
              "أُخْت",
              "أَب",
              "مُعَلِّم"
            ]
          },
          {
            "id": "ukht",
            "grapheme": "أُخْت",
            "audioText": "أُخْتٌ",
            "phonemeDesc": "Sœur",
            "transliteration": "ukhtun",
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
            "transliteration": "waladun",
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
            "transliteration": "bintun",
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
            "transliteration": "mu'allimun",
            "distractors": [
              "طِفْل",
              "أَب",
              "وَلَد"
            ]
          }
        ],
        "wordItems": []
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
            "emoji": "💧"
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
            "emoji": "🥛"
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
            "emoji": "🍞"
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
            "emoji": "🌴"
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
            "emoji": "🍇"
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
            "emoji": "🍎"
          }
        ]
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
            "emoji": "🏫"
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
            "emoji": "🌸"
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
            "emoji": "🐦"
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
            "emoji": "🫐"
          }
        ]
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
            "transliteration": "kitābun",
            "distractors": [
              "قَلَم",
              "بَاب",
              "بَيْت"
            ]
          },
          {
            "id": "qalam",
            "grapheme": "قَلَم",
            "audioText": "قَلَمٌ",
            "phonemeDesc": "Stylo",
            "transliteration": "qalamun",
            "distractors": [
              "كِتَاب",
              "كُرْسِيّ",
              "مَكْتَب"
            ]
          },
          {
            "id": "kursiy",
            "grapheme": "كُرْسِيّ",
            "audioText": "كُرْسِيٌّ",
            "phonemeDesc": "Chaise",
            "transliteration": "kursiyyun",
            "distractors": [
              "مَكْتَب",
              "بَاب",
              "بَيْت"
            ]
          },
          {
            "id": "maktab",
            "grapheme": "مَكْتَب",
            "audioText": "مَكْتَبٌ",
            "phonemeDesc": "Bureau",
            "transliteration": "maktabun",
            "distractors": [
              "كُرْسِيّ",
              "قَلَم",
              "كِتَاب"
            ]
          },
          {
            "id": "madrasa",
            "grapheme": "مَدْرَسَة",
            "audioText": "مَدْرَسَةٌ",
            "phonemeDesc": "École",
            "transliteration": "madrasatun",
            "distractors": [
              "حَدِيقَة",
              "بَيْت",
              "شَجَرَة"
            ]
          },
          {
            "id": "hadeeqa",
            "grapheme": "حَدِيقَة",
            "audioText": "حَدِيقَةٌ",
            "phonemeDesc": "Jardin",
            "transliteration": "ḥadeeqatun",
            "distractors": [
              "مَدْرَسَة",
              "زَهْرَة",
              "شَجَرَة"
            ]
          }
        ],
        "wordItems": []
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
            "phonemeDesc": "Kataba",
            "transliteration": "kataba",
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
            "phonemeDesc": "Darasa",
            "transliteration": "darasa",
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
            "phonemeDesc": "Asad",
            "transliteration": "asadun",
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
            "transliteration": "feelun",
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
            "transliteration": "shamsun",
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
            "transliteration": "baḥrun",
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
            "transliteration": "tuffāḥun",
            "distractors": [
              "عِنَب",
              "تَمْر",
              "خُبْز"
            ]
          }
        ],
        "wordItems": []
      }
    ]
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
            "transliteration": "al-baytu kabeerun",
            "distractors": [
              "المَاءُ بَارِدٌ",
              "الكِتَابُ مُفِيدٌ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ]
          },
          {
            "id": "almaa_baarid",
            "grapheme": "المَاءُ بَارِدٌ",
            "audioText": "المَاءُ بَارِدٌ",
            "phonemeDesc": "L'eau est fraîche",
            "transliteration": "al-mā'u bāridun",
            "distractors": [
              "البَيْتُ كَبِيرٌ",
              "القَمَرُ مُنِيرٌ",
              "الكِتَابُ مُفِيدٌ"
            ]
          },
          {
            "id": "alkitaab_mufeed",
            "grapheme": "الكِتَابُ مُفِيدٌ",
            "audioText": "الكِتَابُ مُفِيدٌ",
            "phonemeDesc": "Le livre est utile",
            "transliteration": "al-kitābu mufeedun",
            "distractors": [
              "البَيْتُ كَبِيرٌ",
              "المَاءُ بَارِدٌ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ]
          },
          {
            "id": "ashshams_mushriqa",
            "grapheme": "الشَّمْسُ مُشْرِقَةٌ",
            "audioText": "الشَّمْسُ مُشْرِقَةٌ",
            "phonemeDesc": "Le soleil brille",
            "transliteration": "ash-shamsu mushriqatun",
            "distractors": [
              "القَمَرُ مُنِيرٌ",
              "المَاءُ بَارِدٌ",
              "البَيْتُ كَبِيرٌ"
            ]
          },
          {
            "id": "alqamar_muneer",
            "grapheme": "القَمَرُ مُنِيرٌ",
            "audioText": "القَمَرُ مُنِيرٌ",
            "phonemeDesc": "La lune est lumineuse",
            "transliteration": "al-qamaru muneerun",
            "distractors": [
              "الشَّمْسُ مُشْرِقَةٌ",
              "الكِتَابُ مُفِيدٌ",
              "المَاءُ بَارِدٌ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "al-waladu nasheetun",
            "distractors": [
              "البِنْتُ ذَكِيَّةٌ",
              "القَلَمُ جَدِيدٌ",
              "البَابُ مَفْتُوحٌ"
            ]
          },
          {
            "id": "albint_dhakiyya",
            "grapheme": "البِنْتُ ذَكِيَّةٌ",
            "audioText": "البِنْتُ ذَكِيَّةٌ",
            "phonemeDesc": "La fille est intelligente",
            "transliteration": "al-bintu dhakiyyatun",
            "distractors": [
              "الوَلَدُ نَشِيطٌ",
              "الزَّهْرَةُ جَمِيلَةٌ",
              "القَلَمُ جَدِيدٌ"
            ]
          },
          {
            "id": "alqalam_jadeed",
            "grapheme": "القَلَمُ جَدِيدٌ",
            "audioText": "القَلَمُ جَدِيدٌ",
            "phonemeDesc": "Le stylo est neuf",
            "transliteration": "al-qalamu jadeedun",
            "distractors": [
              "البَابُ مَفْتُوحٌ",
              "الوَلَدُ نَشِيطٌ",
              "البِنْتُ ذَكِيَّةٌ"
            ]
          },
          {
            "id": "albaab_maftooh",
            "grapheme": "البَابُ مَفْتُوحٌ",
            "audioText": "البَابُ مَفْتُوحٌ",
            "phonemeDesc": "La porte est ouverte",
            "transliteration": "al-bābu maftooḥun",
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
            "transliteration": "az-zahratu jameelatun",
            "distractors": [
              "البِنْتُ ذَكِيَّةٌ",
              "البَابُ مَفْتُوحٌ",
              "القَلَمُ جَدِيدٌ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "kataba al-waladu",
            "distractors": [
              "قَرَأَ الطَّالِبُ",
              "جَلَسَ الأَبُ",
              "أَكَلَ الطِّفْلُ"
            ]
          },
          {
            "id": "qaraa_attaalib",
            "grapheme": "قَرَأَ الطَّالِبُ",
            "audioText": "قَرَأَ الطَّالِبُ",
            "phonemeDesc": "L'élève a lu",
            "transliteration": "qara'a aṭ-ṭālibu",
            "distractors": [
              "كَتَبَ الوَلَدُ",
              "شَرِبَ الوَلَدُ",
              "نَامَ الطِّفْلُ"
            ]
          },
          {
            "id": "jalasa_alab",
            "grapheme": "جَلَسَ الأَبُ",
            "audioText": "جَلَسَ الأَبُ",
            "phonemeDesc": "Le père s'est assis",
            "transliteration": "jalasa al-abu",
            "distractors": [
              "كَتَبَ الوَلَدُ",
              "قَرَأَ الطَّالِبُ",
              "أَكَلَ الطِّفْلُ"
            ]
          },
          {
            "id": "akala_attifl",
            "grapheme": "أَكَلَ الطِّفْلُ",
            "audioText": "أَكَلَ الطِّفْلُ",
            "phonemeDesc": "Le petit a mangé",
            "transliteration": "akala aṭ-ṭiflu",
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
            "transliteration": "shariba al-waladu",
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
            "transliteration": "nāma aṭ-ṭiflu",
            "distractors": [
              "جَلَسَ الأَبُ",
              "شَرِبَ الوَلَدُ",
              "أَكَلَ الطِّفْلُ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "dhahaba al-waladu",
            "distractors": [
              "رَجَعَ الأَبُ",
              "خَرَجَ المُعَلِّمُ",
              "دَخَلَ الطَّالِبُ"
            ]
          },
          {
            "id": "rajaa_alab",
            "grapheme": "رَجَعَ الأَبُ",
            "audioText": "رَجَعَ الأَبُ",
            "phonemeDesc": "Le père est revenu",
            "transliteration": "raja'a al-abu",
            "distractors": [
              "ذَهَبَ الوَلَدُ",
              "خَرَجَ المُعَلِّمُ",
              "طَارَ العُصْفُورُ"
            ]
          },
          {
            "id": "kharaja_almuallim",
            "grapheme": "خَرَجَ المُعَلِّمُ",
            "audioText": "خَرَجَ المُعَلِّمُ",
            "phonemeDesc": "Le maître est sorti",
            "transliteration": "kharaja al-mu'allimu",
            "distractors": [
              "دَخَلَ الطَّالِبُ",
              "ذَهَبَ الوَلَدُ",
              "رَجَعَ الأَبُ"
            ]
          },
          {
            "id": "dakhala_attaalib",
            "grapheme": "دَخَلَ الطَّالِبُ",
            "audioText": "دَخَلَ الطَّالِبُ",
            "phonemeDesc": "L'élève est entré",
            "transliteration": "dakhala aṭ-ṭālibu",
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
            "transliteration": "ṭāra al-'uṣfooru",
            "distractors": [
              "دَخَلَ الطَّالِبُ",
              "رَجَعَ الأَبُ",
              "خَرَجَ المُعَلِّمُ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "qara'a al-waladu al-kitāba",
            "distractors": [
              "كَتَبَ الطَّالِبُ الدَّرْسَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ",
              "أَكَلَ الوَلَدُ التَّمْرَ"
            ]
          },
          {
            "id": "kataba_attaalib_addars",
            "grapheme": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "audioText": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "phonemeDesc": "L'élève a écrit la leçon",
            "transliteration": "kataba aṭ-ṭālibu ad-darsa",
            "distractors": [
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "فَتَحَ الأَبُ البَابَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ"
            ]
          },
          {
            "id": "shariba_attifl_alhaleeb",
            "grapheme": "شَرِبَ الطِّفْلُ الحَلِيبَ",
            "audioText": "شَرِبَ الطِّفْلُ الحَلِيبَ",
            "phonemeDesc": "L'enfant a bu le lait",
            "transliteration": "shariba aṭ-ṭiflu al-ḥaleeba",
            "distractors": [
              "أَكَلَ الوَلَدُ التَّمْرَ",
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          },
          {
            "id": "akala_alwalad_attamr",
            "grapheme": "أَكَلَ الوَلَدُ التَّمْرَ",
            "audioText": "أَكَلَ الوَلَدُ التَّمْرَ",
            "phonemeDesc": "Le garçon a mangé la datte",
            "transliteration": "akala al-waladu at-tamra",
            "distractors": [
              "شَرِبَ الطِّفْلُ الحَلِيبَ",
              "فَتَحَ الأَبُ البَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "fataḥa al-abu al-bāba",
            "distractors": [
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "قَرَأَ الوَلَدُ الكِتَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          },
          {
            "id": "rasama_alwalad_ashshajara",
            "grapheme": "رَسَمَ الوَلَدُ الشَّجَرَةَ",
            "audioText": "رَسَمَ الوَلَدُ الشَّجَرَةَ",
            "phonemeDesc": "L'enfant a dessiné l'arbre",
            "transliteration": "rasama al-waladu ash-shajarata",
            "distractors": [
              "فَتَحَ الأَبُ البَابَ",
              "أَكَلَ الوَلَدُ التَّمْرَ",
              "شَرِبَ الطِّفْلُ الحَلِيبَ"
            ]
          },
          {
            "id": "qaraa_alwalad_alkitaab",
            "grapheme": "قَرَأَ الوَلَدُ الكِتَابَ",
            "audioText": "قَرَأَ الوَلَدُ الكِتَابَ",
            "phonemeDesc": "L'enfant a lu le livre",
            "transliteration": "qara'a al-waladu al-kitāba",
            "distractors": [
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "فَتَحَ الأَبُ البَابَ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          },
          {
            "id": "kataba_attaalib_addars",
            "grapheme": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "audioText": "كَتَبَ الطَّالِبُ الدَّرْسَ",
            "phonemeDesc": "L'élève a écrit la leçon",
            "transliteration": "kataba aṭ-ṭālibu ad-darsa",
            "distractors": [
              "فَتَحَ الأَبُ البَابَ",
              "رَسَمَ الوَلَدُ الشَّجَرَةَ",
              "أَكَلَ الوَلَدُ التَّمْرَ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "as-salāmu 'alaykum",
            "distractors": [
              "أَهْلًا وَسَهْلًا",
              "شُكْرًا جَزِيلًا",
              "صَبَاحُ الخَيْرِ"
            ]
          },
          {
            "id": "ahlan_wa_sahlan",
            "grapheme": "أَهْلًا وَسَهْلًا",
            "audioText": "أَهْلًا وَسَهْلًا",
            "phonemeDesc": "Bienvenue",
            "transliteration": "ahlan wa sahlan",
            "distractors": [
              "السَّلَامُ عَلَيْكُمْ",
              "مَسَاءُ الخَيْرِ",
              "شُكْرًا جَزِيلًا"
            ]
          },
          {
            "id": "shukran_jazeelan",
            "grapheme": "شُكْرًا جَزِيلًا",
            "audioText": "شُكْرًا جَزِيلًا",
            "phonemeDesc": "Merci beaucoup",
            "transliteration": "shukran jazeelan",
            "distractors": [
              "صَبَاحُ الخَيْرِ",
              "أَهْلًا وَسَهْلًا",
              "السَّلَامُ عَلَيْكُمْ"
            ]
          },
          {
            "id": "sabahu_alkhayr",
            "grapheme": "صَبَاحُ الخَيْرِ",
            "audioText": "صَبَاحُ الخَيْرِ",
            "phonemeDesc": "Bonjour",
            "transliteration": "ṣabāḥu al-khayri",
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
            "transliteration": "masā'u al-khayri",
            "distractors": [
              "صَبَاحُ الخَيْرِ",
              "السَّلَامُ عَلَيْكُمْ",
              "شُكْرًا جَزِيلًا"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "dhahaba al-waladu ilā al-madrasati",
            "distractors": [
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "الكِتَابُ فِي الحَقِيبَةِ",
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ"
            ]
          },
          {
            "id": "jalasa_alab_alal_kursiyy",
            "grapheme": "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
            "audioText": "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
            "phonemeDesc": "Le père s'est assis sur la chaise",
            "transliteration": "jalasa al-abu 'alā al-kursiyyi",
            "distractors": [
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "الكِتَابُ فِي الحَقِيبَةِ",
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ"
            ]
          },
          {
            "id": "alkitaab_fil_haqeeba",
            "grapheme": "الكِتَابُ فِي الحَقِيبَةِ",
            "audioText": "الكِتَابُ فِي الحَقِيبَةِ",
            "phonemeDesc": "Le livre est dans le cartable",
            "transliteration": "al-kitābu fee al-ḥaqeebati",
            "distractors": [
              "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ"
            ]
          },
          {
            "id": "alousfoor_fawqa_ashshajara",
            "grapheme": "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
            "audioText": "العُصْفُورُ فَوْقَ الشَّجَرَةِ",
            "phonemeDesc": "L'oiseau est sur l'arbre",
            "transliteration": "al-'uṣfooru fawqa ash-shajarati",
            "distractors": [
              "الكِتَابُ فِي الحَقِيبَةِ",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "qara'a aḥmadu kitāban mufeedan",
            "distractors": [
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ"
            ]
          },
          {
            "id": "dhahabat_fatima_ilal_hadeeqa",
            "grapheme": "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
            "audioText": "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
            "phonemeDesc": "Fatima est allée au jardin",
            "transliteration": "dhahabat fāṭimatu ilā al-ḥadeeqati",
            "distractors": [
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "الكِتَابُ فِي الحَقِيبَةِ"
            ]
          },
          {
            "id": "akala_alwalad_tuffahatan",
            "grapheme": "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
            "audioText": "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
            "phonemeDesc": "Le garçon a mangé une délicieuse pomme",
            "transliteration": "akala al-waladu tuffāḥatan ladheedhatan",
            "distractors": [
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ"
            ]
          }
        ],
        "wordItems": []
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
            "transliteration": "qara'a al-waladu al-kitāba",
            "distractors": [
              "كَتَبَ الطَّالِبُ الدَّرْسَ",
              "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
              "الشَّمْسُ مُشْرِقَةٌ"
            ]
          },
          {
            "id": "dhahaba_alwalad_ilal_madrasa",
            "grapheme": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "audioText": "ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ",
            "phonemeDesc": "L'enfant est allé à l'école",
            "transliteration": "dhahaba al-waladu ilā al-madrasati",
            "distractors": [
              "جَلَسَ الأَبُ عَلَى الكُرْسِيِّ",
              "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
              "البَيْتُ كَبِيرٌ"
            ]
          },
          {
            "id": "ashshams_mushriqa",
            "grapheme": "الشَّمْسُ مُشْرِقَةٌ",
            "audioText": "الشَّمْسُ مُشْرِقَةٌ",
            "phonemeDesc": "Le soleil brille",
            "transliteration": "ash-shamsu mushriqatun",
            "distractors": [
              "القَمَرُ مُنِيرٌ",
              "المَاءُ بَارِدٌ",
              "الكِتَابُ مُفِيدٌ"
            ]
          },
          {
            "id": "assalamu_alaykum",
            "grapheme": "السَّلَامُ عَلَيْكُمْ",
            "audioText": "السَّلَامُ عَلَيْكُمْ",
            "phonemeDesc": "Que la paix soit sur vous",
            "transliteration": "as-salāmu 'alaykum",
            "distractors": [
              "أَهْلًا وَسَهْلًا",
              "شُكْرًا جَزِيلًا",
              "صَبَاحُ الخَيْرِ"
            ]
          },
          {
            "id": "qaraa_ahmad_kitaaban_mufeedan",
            "grapheme": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "audioText": "قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا",
            "phonemeDesc": "Ahmad a lu un livre instructif",
            "transliteration": "qara'a aḥmadu kitāban mufeedan",
            "distractors": [
              "أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً",
              "ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ",
              "كَتَبَ الطَّالِبُ الدَّرْسَ"
            ]
          }
        ],
        "wordItems": []
      }
    ]
  }
];
