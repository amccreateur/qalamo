import asyncio
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# In Arabic grammar / Tajweed: Tanwin is explicitly a Nun Sakinah.
# To force the TTS engine to articulate the "-un", "-an", "-in" 100% audibly without pausal sukun,
# we feed the phonetic spelling to the synthesizer while keeping the correct Tanwin spelling in the app.
tanwin_items = [
    ('kitabun.mp3', 'كِتَابُنْ', 'ar-SA-HamedNeural'),
    ('kitaban.mp3', 'كِتَابَنْ', 'ar-SA-HamedNeural'),
    ('kitabin.mp3', 'كِتَابِنْ', 'ar-SA-HamedNeural'),
    ('waladun.mp3', 'وَلَدُنْ', 'ar-SA-HamedNeural'),
    ('waladan.mp3', 'وَلَدَنْ', 'ar-SA-HamedNeural'),
    ('waladin.mp3', 'وَلَدِنْ', 'ar-SA-HamedNeural'),
    ('baytun.mp3', 'بَيْتُنْ', 'ar-SA-HamedNeural'),
    ('baytan.mp3', 'بَيْتَنْ', 'ar-SA-HamedNeural'),
    ('baytin.mp3', 'بَيْتِنْ', 'ar-SA-HamedNeural'),
    ('kitab.mp3', 'كِتَابْ', 'ar-SA-HamedNeural'),
    ('walad.mp3', 'وَلَدْ', 'ar-SA-HamedNeural'),
    ('bayt.mp3', 'بَيْتْ', 'ar-SA-HamedNeural'),
]

async def main():
    for fn, text, voice in tanwin_items:
        raw_path = f'raw_{fn}'
        final_path = os.path.join('assets/audio/generated', fn)
        
        # 1. Generate crystal clear Tanwin
        comm = edge_tts.Communicate(text, voice, rate='-10%')
        await comm.save(raw_path)
        
        # 2. Trim leading silence for instant 0ms playback
        cmd = [
            'ffmpeg', '-y', '-i', raw_path,
            '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-35dB',
            final_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        if os.path.exists(raw_path):
            os.remove(raw_path)
        print(f'Done: {fn} -> {text}')

if __name__ == '__main__':
    asyncio.run(main())
