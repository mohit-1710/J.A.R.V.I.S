import pyautogui as gui
import pywhatkit
import time

def close():
    gui.hotkey("alt", "f4")


def Search(text):
    gui.hotkey("/")
    time.sleep(0.3)
    gui.hotkey("ctrl","a","backspace")
    gui.write(text)
    gui.hotkey("enter")

def search_google(text):
    pywhatkit.search(text)

def play_stop():
    gui.press("space")
    
def shutdown_device():
    gui.hotkey("win","x")
    time.sleep(0.3)
    gui.hotkey("u","u")

def restart_device():
    gui.hotkey("win","x")
    time.sleep(0.3)
    gui.hotkey("u","r")


def sleep_device():
    gui.hotkey("win","x")
    time.sleep(0.3)
    gui.hotkey("u","s")


def desktop_change_next():
    gui.hotkey("ctrl","win","right")
    
def desktop_change_previous():
    gui.hotkey("ctrl","win","left")

