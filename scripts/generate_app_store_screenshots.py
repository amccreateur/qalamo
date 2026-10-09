import os
from PIL import Image, ImageDraw, ImageFont

BASE_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app_store_screenshots")
DIR_EN = os.path.join(BASE_OUTPUT_DIR, "en")
DIR_FR = os.path.join(BASE_OUTPUT_DIR, "fr")

os.makedirs(DIR_EN, exist_ok=True)
os.makedirs(DIR_FR, exist_ok=True)

FONTS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts")
AMIRI_BOLD = os.path.join(FONTS_DIR, "Amiri-Bold.ttf")
AMIRI_REGULAR = os.path.join(FONTS_DIR, "Amiri-Regular.ttf")

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def generate_iphone_medium(out_dir, index, badge, title, subtitle, main_arabic, arabic_subtitle, choices, btn_label, bg_start, bg_end):
    # Exactly 1179 x 2556 px (iPhone Dynamic Island Moyen: 6.1" / 6.3")
    W, H = 1179, 2556
    img = create_gradient(W, H, bg_start, bg_end)
    draw = ImageDraw.Draw(img)

    try:
        f_title = ImageFont.truetype(AMIRI_BOLD, 68)
        f_sub = ImageFont.truetype(AMIRI_REGULAR, 42)
        f_arabic_large = ImageFont.truetype(AMIRI_BOLD, 130)
        f_arabic_sub = ImageFont.truetype(AMIRI_REGULAR, 48)
        f_badge = ImageFont.truetype(AMIRI_BOLD, 32)
        f_button = ImageFont.truetype(AMIRI_BOLD, 44)
    except Exception:
        f_title = ImageFont.load_default()
        f_sub = ImageFont.load_default()
        f_arabic_large = ImageFont.load_default()
        f_arabic_sub = ImageFont.load_default()
        f_badge = ImageFont.load_default()
        f_button = ImageFont.load_default()

    # Dynamic Island Mock (Top)
    di_w, di_h = 300, 75
    di_x = (W - di_w) // 2
    di_y = 30
    draw_rounded_rect(draw, (di_x, di_y, di_x + di_w, di_y + di_h), 38, fill=(0, 0, 0))

    # Badge Pill
    badge_bbox = draw.textbbox((0, 0), badge, font=f_badge)
    bw = badge_bbox[2] - badge_bbox[0] + 50
    bh = 58
    bx = (W - bw) // 2
    by = 150
    draw_rounded_rect(draw, (bx, by, bx + bw, by + bh), 29, fill=(255, 255, 255, 40), outline=(255, 255, 255), width=2)
    draw.text((bx + 25, by + 10), badge, font=f_badge, fill=(255, 255, 255))
    header_y = 250

    # Header Texts
    t_bbox = draw.textbbox((0, 0), title, font=f_title)
    draw.text(((W - (t_bbox[2] - t_bbox[0])) // 2, header_y), title, font=f_title, fill=(255, 255, 255))

    s_bbox = draw.textbbox((0, 0), subtitle, font=f_sub)
    draw.text(((W - (s_bbox[2] - s_bbox[0])) // 2, header_y + 85), subtitle, font=f_sub, fill=(224, 242, 254))

    # Main Card
    card_x1, card_y1 = 70, header_y + 180
    card_x2, card_y2 = W - 70, H - 110
    draw_rounded_rect(draw, (card_x1, card_y1, card_x2, card_y2), 50, fill=(255, 255, 255))

    inner_draw = ImageDraw.Draw(img)
    draw_rounded_rect(inner_draw, (card_x1 + 25, card_y1 + 25, card_x2 - 25, card_y1 + 115), 20, fill=(241, 245, 249))
    lesson_tag = f"Interactive Lesson • Level {index}" if "en" in out_dir else f"Leçon interactive • Niveau {index}"
    inner_draw.text((card_x1 + 50, card_y1 + 45), lesson_tag, font=f_badge, fill=(71, 85, 105))

    # Central Arabic Box
    box_y1 = card_y1 + 150
    box_y2 = box_y1 + 450
    draw_rounded_rect(inner_draw, (card_x1 + 35, box_y1, card_x2 - 35, box_y2), 32, fill=(238, 242, 255), outline=(199, 210, 254), width=3)
    
    a_bbox = inner_draw.textbbox((0, 0), main_arabic, font=f_arabic_large)
    aw = a_bbox[2] - a_bbox[0]
    inner_draw.text(((W - aw) // 2, box_y1 + 80), main_arabic, font=f_arabic_large, fill=(30, 58, 138))

    as_bbox = inner_draw.textbbox((0, 0), arabic_subtitle, font=f_arabic_sub)
    asw = as_bbox[2] - as_bbox[0]
    inner_draw.text(((W - asw) // 2, box_y1 + 330), arabic_subtitle, font=f_arabic_sub, fill=(79, 70, 229))

    # 4 interactive choices
    grid_y = box_y2 + 45
    tile_w = (card_x2 - card_x1 - 100) // 2
    tile_h = 220

    for i, (c_ar, c_label) in enumerate(choices):
        row = i // 2
        col = i % 2
        tx1 = card_x1 + 35 + col * (tile_w + 30)
        ty1 = grid_y + row * (tile_h + 25)
        tx2 = tx1 + tile_w
        ty2 = ty1 + tile_h

        is_correct = (i == 0)
        bg_tile = (220, 252, 231) if is_correct else (248, 250, 252)
        border_tile = (34, 197, 94) if is_correct else (226, 232, 240)

        draw_rounded_rect(inner_draw, (tx1, ty1, tx2, ty2), 24, fill=bg_tile, outline=border_tile, width=3 if is_correct else 2)
        
        t_ar_bbox = inner_draw.textbbox((0, 0), c_ar, font=f_sub)
        inner_draw.text(((tx1 + tx2 - (t_ar_bbox[2] - t_ar_bbox[0])) // 2, ty1 + 35), c_ar, font=f_sub, fill=(15, 23, 42))

        t_fr_bbox = inner_draw.textbbox((0, 0), c_label, font=f_badge)
        inner_draw.text(((tx1 + tx2 - (t_fr_bbox[2] - t_fr_bbox[0])) // 2, ty1 + 130), c_label, font=f_badge, fill=(71, 85, 105))

    # Bottom Audio Button
    btn_y1 = grid_y + 2 * (tile_h + 25) + 35
    btn_y2 = btn_y1 + 120
    draw_rounded_rect(inner_draw, (card_x1 + 35, btn_y1, card_x2 - 35, btn_y2), 28, fill=(37, 99, 235))
    btn_bbox = inner_draw.textbbox((0, 0), btn_label, font=f_button)
    inner_draw.text(((W - (btn_bbox[2] - btn_bbox[0])) // 2, btn_y1 + 30), btn_label, font=f_button, fill=(255, 255, 255))

    out_path = os.path.join(out_dir, f"iphone_medium_screenshot_{index}.png")
    img.save(out_path, "PNG", quality=95)
    return out_path


def generate_ipad(out_dir, index, badge, title, subtitle, main_arabic, arabic_subtitle, choices, btn_label, bg_start, bg_end):
    # Exactly 2048 x 2732 px (iPad 13")
    W, H = 2048, 2732
    img = create_gradient(W, H, bg_start, bg_end)
    draw = ImageDraw.Draw(img)

    try:
        f_title = ImageFont.truetype(AMIRI_BOLD, 100)
        f_sub = ImageFont.truetype(AMIRI_REGULAR, 60)
        f_arabic_large = ImageFont.truetype(AMIRI_BOLD, 220)
        f_arabic_sub = ImageFont.truetype(AMIRI_REGULAR, 68)
        f_badge = ImageFont.truetype(AMIRI_BOLD, 48)
        f_button = ImageFont.truetype(AMIRI_BOLD, 64)
    except Exception:
        f_title = ImageFont.load_default()
        f_sub = ImageFont.load_default()
        f_arabic_large = ImageFont.load_default()
        f_arabic_sub = ImageFont.load_default()
        f_badge = ImageFont.load_default()
        f_button = ImageFont.load_default()

    badge_bbox = draw.textbbox((0, 0), badge, font=f_badge)
    bw = badge_bbox[2] - badge_bbox[0] + 80
    bh = 80
    bx = (W - bw) // 2
    by = 120
    draw_rounded_rect(draw, (bx, by, bx + bw, by + bh), 40, fill=(255, 255, 255, 40), outline=(255, 255, 255), width=3)
    draw.text((bx + 40, by + 12), badge, font=f_badge, fill=(255, 255, 255))

    header_y = 250
    t_bbox = draw.textbbox((0, 0), title, font=f_title)
    draw.text(((W - (t_bbox[2] - t_bbox[0])) // 2, header_y), title, font=f_title, fill=(255, 255, 255))

    s_bbox = draw.textbbox((0, 0), subtitle, font=f_sub)
    draw.text(((W - (s_bbox[2] - s_bbox[0])) // 2, header_y + 130), subtitle, font=f_sub, fill=(224, 242, 254))

    card_x1, card_y1 = 120, header_y + 260
    card_x2, card_y2 = W - 120, H - 140
    draw_rounded_rect(draw, (card_x1, card_y1, card_x2, card_y2), 64, fill=(255, 255, 255))

    inner_draw = ImageDraw.Draw(img)

    box_y1 = card_y1 + 80
    box_y2 = box_y1 + 650
    draw_rounded_rect(inner_draw, (card_x1 + 80, box_y1, card_x2 - 80, box_y2), 48, fill=(238, 242, 255), outline=(199, 210, 254), width=4)

    a_bbox = inner_draw.textbbox((0, 0), main_arabic, font=f_arabic_large)
    inner_draw.text(((W - (a_bbox[2] - a_bbox[0])) // 2, box_y1 + 120), main_arabic, font=f_arabic_large, fill=(30, 58, 138))

    as_bbox = inner_draw.textbbox((0, 0), arabic_subtitle, font=f_arabic_sub)
    inner_draw.text(((W - (as_bbox[2] - as_bbox[0])) // 2, box_y1 + 480), arabic_subtitle, font=f_arabic_sub, fill=(79, 70, 229))

    grid_y = box_y2 + 70
    tile_w = (card_x2 - card_x1 - 240) // 2
    tile_h = 320

    for i, (c_ar, c_label) in enumerate(choices):
        row = i // 2
        col = i % 2
        tx1 = card_x1 + 80 + col * (tile_w + 80)
        ty1 = grid_y + row * (tile_h + 40)
        tx2 = tx1 + tile_w
        ty2 = ty1 + tile_h

        is_correct = (i == 0)
        bg_tile = (220, 252, 231) if is_correct else (248, 250, 252)
        border_tile = (34, 197, 94) if is_correct else (226, 232, 240)

        draw_rounded_rect(inner_draw, (tx1, ty1, tx2, ty2), 36, fill=bg_tile, outline=border_tile, width=4 if is_correct else 2)

        t_ar_bbox = inner_draw.textbbox((0, 0), c_ar, font=f_sub)
        inner_draw.text(((tx1 + tx2 - (t_ar_bbox[2] - t_ar_bbox[0])) // 2, ty1 + 60), c_ar, font=f_sub, fill=(15, 23, 42))

        t_fr_bbox = inner_draw.textbbox((0, 0), c_label, font=f_badge)
        inner_draw.text(((tx1 + tx2 - (t_fr_bbox[2] - t_fr_bbox[0])) // 2, ty1 + 190), c_label, font=f_badge, fill=(71, 85, 105))

    btn_y1 = grid_y + 2 * (tile_h + 40) + 50
    btn_y2 = btn_y1 + 160
    draw_rounded_rect(inner_draw, (card_x1 + 80, btn_y1, card_x2 - 80, btn_y2), 40, fill=(37, 99, 235))
    btn_bbox = inner_draw.textbbox((0, 0), btn_label, font=f_button)
    inner_draw.text(((W - (btn_bbox[2] - btn_bbox[0])) // 2, btn_y1 + 45), btn_label, font=f_button, fill=(255, 255, 255))

    out_path = os.path.join(out_dir, f"ipad_13_screenshot_{index}.png")
    img.save(out_path, "PNG", quality=95)
    return out_path


# --- GENERATE EN (1179 x 2556 for iPhone & 2048 x 2732 for iPad) ---
generate_iphone_medium(
    DIR_EN, 1, "QALAMO • LEARN ARABIC",
    "Learn Arabic Step by Step", "Letters, vowels & authentic pronunciation",
    "بَ • بِ • بُ", "Letter Ba with short vowels",
    [("بَ", "Ba (Fatha)"), ("بِ", "Bi (Kasrah)"), ("بُ", "Bu (Damma)"), ("بْ", "B' (Sukun)")],
    "🔊 Listen to exact pronunciation", (30, 58, 138), (59, 130, 246)
)
generate_iphone_medium(
    DIR_EN, 2, "MINI-GAMES & AUDIO",
    "Mini-Games & Audio Practice", "Train your ear and build full words",
    "كَتَبَ", "Word assembly & reading",
    [("كَتَبَ", "Ka-ta-ba"), ("قَلَمٌ", "Qa-la-mun"), ("نُورٌ", "Nu-run"), ("جَنَّةٌ", "Jan-na-tun")],
    "🔊 Test your listening skills", (15, 118, 110), (14, 165, 233)
)
generate_iphone_medium(
    DIR_EN, 3, "NOURANIA METHOD",
    "Rules & Sound Explorer", "Tanween, Sukun, Shaddah & Grammar",
    "حَرْفُ جَرٍّ", "Prepositions & majroor endings",
    [("حَرْفُ جَرٍّ", "Preposition"), ("اسْمٌ مَجْرُورٌ", "Ism Majrur"), ("مَدٌّ طَوِيلٌ", "Long Vowel"), ("تَنْوِينٌ", "Tanween (-un, -an, -in)")],
    "🔊 Explore every sound variation", (67, 56, 202), (147, 51, 234)
)

generate_ipad(
    DIR_EN, 1, "QALAMO • LEARN ARABIC ON IPAD",
    "Learn Arabic Step by Step", "The complete interactive alphabet for all ages",
    "أَ • إِ • أُ", "Alphabet & Core Vowel Variations",
    [("أَ • إِ • أُ", "Alif & Vowels"), ("بَ • بِ • بُ", "Ba & Forms"), ("تَ • تِ • تُ", "Ta & Variations"), ("ثَ • ثِ • ثُ", "Tha & Sounds")],
    "🔊 Listen & Repeat native pronunciation", (30, 58, 138), (59, 130, 246)
)
generate_ipad(
    DIR_EN, 2, "INTERACTIVE GAMES & HQ AUDIO",
    "Fun Mini-Games & Quick Practice", "Daily interactive lessons to read with ease",
    "كَتَبَ • قَرَأَ", "Fluent reading & word building",
    [("كَتَبَ", "Ka-ta-ba (To write)"), ("قَرَأَ", "Qa-ra-'a (To read)"), ("عَلِمَ", "'A-li-ma (To know)"), ("سَمِعَ", "Sa-mi-'a (To hear)")],
    "🔊 Listen & Practice listening fluency", (15, 118, 110), (14, 165, 233)
)
generate_ipad(
    DIR_EN, 3, "FULL PEDAGOGICAL CURRICULUM",
    "Complete Arabic Curriculum", "Nourania Method, Tanween, Shaddah & Grammar",
    "حَرْفُ جَرٍّ + اسْمٌ", "Grammar rules & Arabic reading fluency",
    [("حَرْفُ جَرٍّ + اسْمٌ", "Grammar rule"), ("اسْمٌ مَجْرُورٌ بِالكَسْرَةِ", "Majrur (Kasrah)"), ("تَنْوِينُ الضَّمِّ / الكَسْرِ", "Full Tanween"), ("الشَّدَّةُ مَعَ الحَرَكَاتِ", "Shaddah & vowels")],
    "🔊 Master all reading & tajweed rules", (67, 56, 202), (147, 51, 234)
)

# --- GENERATE FR (1179 x 2556 for iPhone & 2048 x 2732 for iPad) ---
generate_iphone_medium(
    DIR_FR, 1, "QALAMO • APPRENDRE L'ARABE",
    "Apprenez l'Arabe Pas à Pas", "Lettres, voyelles et prononciation exacte",
    "بَ • بِ • بُ", "Lettre Bā avec voyelles courtes",
    [("بَ", "Ba (Fatha)"), ("بِ", "Bi (Kasrah)"), ("بُ", "Bou (Damma)"), ("بْ", "B' (Soukoun)")],
    "🔊 Écouter la prononciation exacte", (30, 58, 138), (59, 130, 246)
)
generate_iphone_medium(
    DIR_FR, 2, "MINI-JEUX & AUDIO",
    "Mini-Jeux & Pratique Audio", "Entraînez votre oreille et votre lecture",
    "كَتَبَ", "Assemblage & lecture de mots",
    [("كَتَبَ", "Ka-ta-ba"), ("قَلَمٌ", "Qa-la-moun"), ("نُورٌ", "Nou-roun"), ("جَنَّةٌ", "Jan-na-toun")],
    "🔊 Testez votre écoute", (15, 118, 110), (14, 165, 233)
)
generate_iphone_medium(
    DIR_FR, 3, "MÉTHODE NOURANIA",
    "Règles & Explorateur de Sons", "Tanwîn, Soukoun, Chaddah et Grammaire",
    "حَرْفُ جَرٍّ", "Prépositions et terminaisons majroûr",
    [("حَرْفُ جَرٍّ", "Préposition"), ("اسْمٌ مَجْرُورٌ", "Ism Majrūr"), ("مَدٌّ طَوِيلٌ", "Voyelle longue"), ("تَنْوِينٌ", "Tanwîn (-oun, -an, -in)")],
    "🔊 Explorez toutes les variations", (67, 56, 202), (147, 51, 234)
)

generate_ipad(
    DIR_FR, 1, "QALAMO • SUR IPAD",
    "Apprenez l'Arabe Pas à Pas", "L'alphabet arabe interactif pour petits et grands",
    "أَ • إِ • أُ", "Alphabet & Déclinaisons fondamentales",
    [("أَ • إِ • أُ", "Alif & Voyelles"), ("بَ • بِ • بُ", "Bā & Déclinaisons"), ("تَ • تِ • تُ", "Tā & Formes"), ("ثَ • ثِ • ثُ", "Thā & Sons")],
    "🔊 Écouter et Répéter le son authentique", (30, 58, 138), (59, 130, 246)
)
generate_ipad(
    DIR_FR, 2, "MINI-JEUX & AUDIO HQ",
    "Mini-Jeux Stimulants & Audio HQ", "Des exercices interactifs pour progresser chaque jour",
    "كَتَبَ • قَرَأَ", "Lecture fluide et compréhension",
    [("كَتَبَ", "Ka-ta-ba (Écrire)"), ("قَرَأَ", "Qa-ra-'a (Lire)"), ("عَلِمَ", "'A-li-ma (Savoir)"), ("سَمِعَ", "Sa-mi-'a (Écouter)")],
    "🔊 Pratiquer l'écoute et l'accent", (15, 118, 110), (14, 165, 233)
)
generate_ipad(
    DIR_FR, 3, "PROGRAMME PÉDAGOGIQUE",
    "Programme Pédagogique Complet", "Méthode Nourania, Tanwîn, Chaddah et Grammaire",
    "حَرْفُ جَرٍّ + اسْمٌ", "Règles de lecture et grammaire arabe",
    [("حَرْفُ جَرٍّ + اسْمٌ", "Règle de grammaire"), ("اسْمٌ مَجْرُورٌ بِالكَسْرَةِ", "Majrūr (Kasrah)"), ("تَنْوِينُ الضَّمِّ / الكَسْرِ", "Tanwîn complet"), ("الشَّدَّةُ مَعَ الحَرَكَاتِ", "Chaddah & combinaisons")],
    "🔊 Maîtriser toutes les règles", (67, 56, 202), (147, 51, 234)
)

print("ALL SCREENSHOTS RESIZED & GENERATED FOR EXACT APPLE RESOLUTIONS (1179x2556 & 2048x2732)!")
