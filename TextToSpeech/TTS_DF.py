import asyncio
import threading
import os
import edge_tts
import pygame
import time 

voice = "en-IE-EmilyNeural"
BUFFER_SIZE = 1024


def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            os.remove(file_path)
            break
        except FileNotFoundError:
            break
        except Exception as e:
            print(f"Error deleting file: {e}")
            attempts += 1
            time.sleep(1) 



async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, voice)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()

    except Exception as e:
        print(e)

    finally:
        remove_file(output_file)


def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()

        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        pygame.quit()

    except Exception as e:
        print(e)


def speak(Text, output_file=None):
    try:
        if output_file is None:
            output_file = f"{os.getcwd()}/speech.mp3"
        asyncio.run(amain(Text, output_file))

    except Exception as e:
        print(e)



