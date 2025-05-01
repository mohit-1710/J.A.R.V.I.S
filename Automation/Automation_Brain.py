from Automation.Web_Open import openweb
from Automation.App_Open import open_App
import pyautogui as gui
from Automation.play_Music_YT import play_music_on_youtube
from Automation.play_Music_Spotify import play_music_from_spotify
from TextToSpeech import Fast_DF_TTS
from Automation.Battery import check_Percentage, check_Plug
from Automation.Shortcuts import close,Search,search_google,play_stop,shutdown_device,sleep_device,restart_device,desktop_change_next,desktop_change_previous
from Automation.tab_automation import tab_command
from Automation.Youtube_play_back import  control_media_player
from Automation.Scroll_System import control_scrolling
import time


def clear_file():
    with open("input.txt", "w") as file:
            file.truncate(0)
            
def play_music(platform_func):
    Fast_DF_TTS.speak("Which song do you want to play, sir?")
    clear_file()
    output_text = ""
    
    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().strip().lower()
        
        if input_text != output_text:
            output_text = input_text
            if output_text:
                platform_func(output_text)
                break


    
def Open_Brain(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website named", "").strip()
        openweb(text)

    else:
        text = text.replace("open", "").strip()
        text = text.replace("app", "").strip()
        open_App(text)

def perform_device_action(task):
    task_function_map = {
        "shutdown": shutdown_device,
        "restart": restart_device,
        "sleep": sleep_device
    }

    correct_password = f"{task} device my friend"

    Fast_DF_TTS.speak(f"Please say the password, sir. I will {task} the computer.")
    clear_file()
    output_text = ""

    while True:
        with open("input.txt", "r") as file:
            input_text = file.read().strip().lower()

        if input_text != output_text:  # Detect new input
            output_text = input_text
            if output_text:  # Only process non-empty input
                if output_text == correct_password:
                    Fast_DF_TTS.speak(f"Password accepted. Performing {task}.")
                    task_function_map[task]()
                    break
                else:
                    Fast_DF_TTS.speak("Incorrect password. Do you want to try again? Please say 'yes' or 'no'.")
                    clear_file()

                    while True:
                        with open("input.txt", "r") as retry_file:
                            retry_input = retry_file.read().strip().lower()

                        if retry_input:  # Wait for non-empty response
                            if retry_input == "no":
                                Fast_DF_TTS.speak("Operation cancelled.")
                                clear_file()
                                return  # Exit the function
                            elif retry_input == "yes":
                                Fast_DF_TTS.speak("Please say the password again.")
                                clear_file()
                                break  # Exit the retry loop
                            else:
                                Fast_DF_TTS.speak("Invalid response. Please say 'yes' or 'no'.")
                                clear_file()
                            

def Auto_main_brain(text):
    try:
        if text.startswith("open"):
            Open_Brain(text)
        
        elif text.startswith("close window"):
            close(text)
        
        elif "youtube" in text or "play music" in text or "play youtube music" in text:
            play_music(play_music_on_youtube)
        
        elif "spotify" in text or "play some music" in text or "play some music on spotify" in text:
            play_music(play_music_from_spotify)
        
        elif "check battery" in text or "check battery level" in text or "current battery percentage" in text:
            check_Percentage()
        elif "play" in text or "stop" in text or "pause" in text:
            play_stop()

        elif text.startswith("search"):
            text = text.replace("search", "")
            text = text.strip()
            Search(text)

        elif "search in google" in text:
            text = text.replace("search in google","")
            text = text.strip()
            search_google(text)
        
        elif (
            "shutdown" in text or 
            "shutdown my device" in text or 
            "shut my device down" in text or 
            "power off the computer" in text or 
            "turn off the computer" in text or 
            "turn off my pc" in text or 
            "power off my pc" in text
        ):
            perform_device_action("shutdown")
        
        elif (
            "restart" in text or 
            "restart my device" in text or 
            "reboot the computer" in text or 
            "reboot my pc" in text or 
            "restart my pc" in text
        ):
            perform_device_action("restart")
        
        elif (
            "sleep" in text or 
            "sleep my device" in text or 
            "put my device to sleep" in text or 
            "put the computer to sleep" in text or 
            "go to sleep mode" in text or 
            "put my pc in sleep mode" in text
        ):
            perform_device_action("sleep")

        elif "next desktop" in text or "move to next desktop" in text or "change to next desktop" in text :
            desktop_change_next()
        
        elif "previous desktop" in text or "move to previous desktop" in text or "change to last desktop" in text :
            desktop_change_previous()

        else:
            tab_command(text)
            control_media_player(text)
            control_scrolling(text)

    except Exception as e:
        print(f"An error occurred: {e}")


        