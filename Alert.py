import os
from winotify import Notification, audio
from os import getcwd

icon_path = r"C:\Users\Mohit\OneDrive\Documents\AI_Project\BOT\logo.png"

def Alert(text):
    toast = Notification(
    app_id="🟢 J.A.R.V.I.S.",
    title=text,
    # msg=text,
    duration="long",
    icon=icon_path,
    )

    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="https://www.google.com")

    toast.show()



