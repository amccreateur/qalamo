import asyncio
import edge_tts
import subprocess
import os

kasra_pure_syllables = [
    ("alif_kasra", "إِي"),
    ("ba_kasra", "بِي"),
    ("ta_kasra", "تِي"),
    ("tha_kasra", "ثِي"),
    ("jeem_kasra", "جِي"),
    ("hha_kasra", "حِي"),
    ("kha_kasra", "خِي"),
    ("dal_kasra", "دِي"),
    ("dhal_kasra", "ذِي"),
    ("ra_kasra", "رِي"),
    ("zay_kasra", "زِي"),
    ("seen_kasra", "سِي"),
    ("sheen_kasra", "شِي"),
    ("sad_kasra", "صِي"),
    ("dad_kasra", "ضِي"),
    ("ttaa_kasra", "طِي"),
    ("zha_kasra", "ظِي"),
    ("ayn_kasra", "عِي"),
    ("ghayn_kasra", "غِي"),
    ("fa_kasra", "فِي"),
    ("qaf_kasra", "قِي"),
    ("kaf_kasra", "كِي"),
    ("lam_kasra", "لِي"),
    ("meem_kasra", "مِي"),
    ("noon_kasra", "نِي"),
    ("haa_kasra", "هِي"),
    ("waw_kasra", "وِي"),
    ("yaa_kasra", "يِي"),
]

aliases = {
    "bi_kasra": "ba_kasra",
    "ti_kasra": "ta_kasra",
    "thi_kasra": "tha_kasra",
    "ji_kasra": "jeem_kasra",
    "hi_kasra": "hha_kasra",
    "khi_kasra": "kha_kasra",
    "di_kasra": "dal_kasra",
    "dhi_kasra": "dhal_kasra",
    "ri_kasra": "ra_kasra",
    "zi_kasra": "zay_kasra",
    "si_kasra": "seen_kasra",
    "shi_kasra": "sheen_kasra",
    "ki_kasra": "kaf_kasra",
    "li_kasra": "lam_kasra",
    "mi_kasra": "meem_kasra",
    "ni_kasra": "noon_kasra",
}

async def generate_pure_kasra():
    voice = "ar-SA-HamedNeural"
    print("Generating pure Kasrah syllables...")
    for key, text in kasra_pure_syllables:
        raw = f"raw_{key}.mp3"
        dest = f"assets/audio/generated/{key}.mp3"
        tts = edge_tts.Communicate(text, voice, rate="-5%")
        await tts.save(raw)
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
            dest
        ], capture_output=True)
        if os.path.exists(raw):
            os.remove(raw)
        print(f"Generated {dest}")

    for alias, target in aliases.items():
        src = f"assets/audio/generated/{target}.mp3"
        dst = f"assets/audio/generated/{alias}.mp3"
        if os.path.exists(src):
            subprocess.run(["ffmpeg", "-y", "-i", src, "-c", "copy", dst], capture_output=True)

if __name__ == "__main__":
    asyncio.run(generate_pure_kasra())
