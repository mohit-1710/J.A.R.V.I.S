import pyautogui

def scroll_up():
    pyautogui.press('up', presses=5)

def scroll_down():
    pyautogui.press('down', presses=5)

def scroll_to_top():
    pyautogui.hotkey('home')

def scroll_to_bottom():
    pyautogui.hotkey('end')


def control_scrolling(text):
    text = text.lower()

    if "scroll up" in text or "move up" in text:
        scroll_up()
    elif "scroll down" in text or "move down" in text:
        scroll_down()
    elif "scroll to top" in text or "go to top" in text:
        scroll_to_top()
    elif "scroll to bottom" in text or "go to bottom" in text:
        scroll_to_bottom()
    else:
        pass

