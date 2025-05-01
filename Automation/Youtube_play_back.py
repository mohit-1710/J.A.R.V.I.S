import pyautogui

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_forward():
    pyautogui.press('right')

def seek_backward():
    pyautogui.press('left')

def seek_forward_10s():
    pyautogui.press('l')

def seek_backward_10s():
    pyautogui.press('j')

def seek_backward_frame():
    pyautogui.press(',')

def seek_forward_frame():
    pyautogui.press('.')

def seek_to_beginning():
    pyautogui.press('home')

def seek_to_end():
    pyautogui.press('end')

def seek_to_previous_chapter():
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    pyautogui.hotkey('shift', 'p')



def control_media_player(text):
    if "increase volume" in text or "volume up" in text or "increase the volume" in text:
        volume_up()
    elif "decrease volume" in text or "volume down" in text or "lower the volume" in text:
        volume_down()
    elif "seek forward" in text or "forward" in text:
        seek_forward()
    elif "seek backward" in text or "rewind" in text:
        seek_backward()
    elif "seek forward 10 seconds" in text or "forward 10 seconds" in text or "jump forward 10 seconds" in text or "10 seconds forward" in text:
        seek_forward_10s()
    elif "seek backward 10 seconds" in text or "back 10 seconds" in text or "rewind 10 seconds" in text:
        seek_backward_10s()
    elif "seek backward frame" in text or "previous frame" in text:
        seek_backward_frame()
    elif "seek forward frame" in text or "next frame" in text:
        seek_forward_frame()
    elif "seek to beginning" in text or "go to start" in text:
        seek_to_beginning()
    elif "seek to end" in text or "go to end" in text:
        seek_to_end()
    elif "previous chapter" in text or "seek to previous chapter" in text:
        seek_to_previous_chapter()
    elif "next chapter" in text or "seek to next chapter" in text:
        seek_to_next_chapter()
    elif "decrease playback speed" in text or "slow down" in text:
        decrease_playback_speed()
    elif "increase playback speed" in text or "speed up" in text:
        increase_playback_speed()
    elif "next video" in text or "move to next video" in text:
        move_to_next_video()
    elif "previous video" in text or "move to previous video" in text:
        move_to_previous_video()
    else:
        pass


