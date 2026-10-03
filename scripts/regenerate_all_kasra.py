import asyncio
import edge_tts
import subprocess
import os

kasra_definitions = [
    ("alif_kasra", "إِ"),
    ("ba_kasra", "بِ"),
    ("ta_kasra", "تِ"),
    ("tha_kasra", "ثِ"),
    ("jeem_kasra", "جِ"),
    ("hha_kasra", "حِ"),
    ("kha_kasra", "خِ"),
    ("dal_kasra", "دِ"),
    ("dhal_kasra", "ذِ"),
    ("ra_kasra", "رِ"),
    ("zay_kasra", "زِ"),
    ("seen_kasra", "سِ"),
    ("sheen_kasra", "شِ"),
    ("sad_kasra", "صِ"),
    ("dad_kasra", "ضِ"),
    ("ttaa_kasra", "طِ"),
    ("zha_kasra", "ظِ"),
    ("ayn_kasra", "عِ"),
    ("ghayn_kasra", "غِ"),
    ("fa_kasra", "فِ"),
    ("qaf_kasra", "قِ"),
    ("kaf_kasra", "كِ"),
    ("lam_kasra", "لِ"),
    ("meem_kasra", "مِ"),
    ("noon_kasra", "نِ"),
    ("haa_kasra", "هِ"),
    ("waw_kasra", "وِ"),
    ("yaa_kasra", "يِ"),
]

# Additional aliases in audioMap
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

async def regenerate_all_kasra():
    voice = "ar-SA-HamedNeural"
    print("Regenerating all 28 Kasrah audio clips with HamedNeural...")
    
    for key, text in kasra_definitions:
        raw = f"raw_{key}.mp3"
        dest = f"assets/audio/generated/{key}.mp3"
        tts = edge_tts.Communicate(text, voice, rate="-10%")
        await tts.save(raw)
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
            dest
        ], capture_output=True)
        if os.path.exists(raw):
            os.remove(raw)
        print(f"Generated {dest} ({os.path.getsize(dest)} bytes)")

    # Copy aliases
    for alias, target in aliases.items():
        src = f"assets/audio/generated/{target}.mp3"
        dst = f"assets/audio/generated/{alias}.mp3"
        if os.path.exists(src):
            subprocess.run(["ffmpeg", "-y", "-i", src, "-c", "copy", dst], capture_output=True)
            print(f"Copied alias {dst}")

if __name__ == "__main__":
    asyncio.run(regenerate_all_kasra())
