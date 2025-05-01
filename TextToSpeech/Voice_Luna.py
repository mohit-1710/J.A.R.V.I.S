import subprocess
import threading
import os
from playsound import playsound
import tempfile


def speak(text: str, voice: str = "en-IE-EmilyNeural") -> None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            output_file = tmpfile.name

        command = f'edge-tts --voice {voice} --text "{text}" --write-media {output_file}'
        
        subprocess.run(command, shell=True, check=True)

        threading.Thread(target=playsound, args=(output_file,)).start()

    except Exception as e:
        print(e)
