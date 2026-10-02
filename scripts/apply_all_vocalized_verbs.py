import asyncio
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# Using the exact proven formula (Hamed with vocalic continuation marker)
# so that the final Fathah is 100% articulated without pausal Sukun.
verbs_list = [
    # Monde 6 : Verbes 3 lettres & action
    ('kataba.mp3', 'كَتَبَا', 'ar-SA-HamedNeural'),
    ('darasa.mp3', 'دَرَسَا', 'ar-SA-HamedNeural'),
    ('qaraa.mp3', 'قَرَأَ', 'ar-SA-HamedNeural'),
    ('rasama.mp3', 'رَسَمَا', 'ar-SA-HamedNeural'),
    ('jalasa.mp3', 'جَلَسَا', 'ar-SA-HamedNeural'),
    ('dhahaba.mp3', 'ذَهَبَا', 'ar-SA-HamedNeural'),
    ('samia.mp3', 'سَمِعَا', 'ar-SA-HamedNeural'),
    ('akala.mp3', 'أَكَلَا', 'ar-SA-HamedNeural'),
    ('shariba.mp3', 'شَرِبَا', 'ar-SA-HamedNeural'),
    ('fataha.mp3', 'فَتَحَا', 'ar-SA-HamedNeural'),
    ('kharaja.mp3', 'خَرَجَا', 'ar-SA-HamedNeural'),
    ('dakhala.mp3', 'دَخَلَا', 'ar-SA-HamedNeural'),
    ('naama.mp3', 'نَامَا', 'ar-SA-HamedNeural'),
    ('rajaa.mp3', 'رَجَعَا', 'ar-SA-HamedNeural'),
    ('taara.mp3', 'طَارَا', 'ar-SA-HamedNeural'),

    # Monde 5 : Verbes Shaddah
    ('rabba.mp3', 'رَبَّا', 'ar-SA-HamedNeural'),
    ('madda.mp3', 'مَدَّا', 'ar-SA-HamedNeural'),
    ('allama.mp3', 'عَلَّمَا', 'ar-SA-HamedNeural'),
    ('shadda.mp3', 'شَدَّا', 'ar-SA-HamedNeural'),
    ('hassa.mp3', 'حَسَّا', 'ar-SA-HamedNeural'),
]

async def main():
    for fn, text, voice in verbs_list:
        raw_path = f'raw_vb_{fn}'
        final_path = os.path.join('assets/audio/generated', fn)

        comm = edge_tts.Communicate(text, voice, rate='-10%')
        await comm.save(raw_path)

        # Trim leading silence for instant 0ms audio playback
        cmd = [
            'ffmpeg', '-y', '-i', raw_path,
            '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-35dB',
            final_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        if os.path.exists(raw_path):
            os.remove(raw_path)

        print(f'Generated vocalized verb: {final_path} from "{text}" ({voice})')

if __name__ == '__main__':
    asyncio.run(main())
