import pyautogui
import time
from Automation.App_Open import open_App
import os

def play_music_from_spotify(song_name):
    try:
        open_App("spotify")
        time.sleep(5)
    except Exception as e:
        print(f"Error opening Spotify: {e}")
        return  # Exit the function if the app cannot be opened

    try:
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.1)
        pyautogui.write(song_name)
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(5)
    except Exception as e:
        print(f"Error searching for the song: {e}")
        return  # Exit the function if inputting the song name fails

    try:
        for _ in range(2):
            pyautogui.press("tab")
            time.sleep(0.1)
    except Exception as e:
        print(f"Error navigating with tab: {e}")

    play_button_path = os.path.join(os.path.dirname(__file__), "play_button.png")

    found = False
    max_attempts = 10
    attempts = 0

    while not found and attempts < max_attempts:
        try:
            play_button = pyautogui.locateOnScreen(play_button_path, confidence=0.6)
            if play_button is not None:
                play_button_center = pyautogui.center(play_button)
                pyautogui.click(play_button_center)
                found = True
            else:
                pyautogui.press("tab")
                time.sleep(0.5)
                attempts += 1
        except Exception as e:
            print(f"Error locating or clicking the play button: {e}")
            attempts += 1  # Still count the attempt if an error occurs

    if found:
        print("Music should now be playing.")
    else:
        print("Failed to find the play button after several attempts.")


