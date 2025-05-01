import psutil
import time
import threading
from TextToSpeech.Fast_DF_TTS import speak
from Alert import Alert

last_alerted_percentage = None


def alert_and_speak(percentage, message):
    """Displays notification and speaks a message for a given battery level."""
    global last_alerted_percentage
    if last_alerted_percentage != percentage:
        t1 = threading.Thread(target=Alert, args=(message,))
        t2 = threading.Thread(target=speak, args=(message,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        last_alerted_percentage = percentage


def check_Percentage():
    """Displays and speaks out the current battery percentage."""
    battery = psutil.sensors_battery()
    if battery:
        percentage = int(battery.percent)
        message = f"Sir,the current battery level stands at {percentage} percent."
        alert_and_speak(percentage, message)


def battery_alert():
    """Monitors battery percentage and triggers alerts at specific thresholds."""
    while True:
        time.sleep(3)
        battery = psutil.sensors_battery()
        if battery:
            percentage = int(battery.percent)
            if battery.power_plugged:
                if percentage == 100:
                    alert_and_speak(
                        percentage,
                        "Sir, a quick update: The battery has reached 100 percent. It is fully charged. Kindly disconnect the charger to maintain battery health.",
                    )
                elif percentage == 80:
                    alert_and_speak(
                        percentage,
                        "Sir, just a gentle reminder: The battery is now at 80 percent. For optimal performance, you might want to unplug the charger.",
                    )
            else:
                if percentage == 20:
                    alert_and_speak(
                        percentage,
                        "Sir, sorry to disturb you, but the battery level is at 20 percent. Please consider plugging in the charger soon.",
                    )
                elif percentage == 15:
                    alert_and_speak(
                        percentage,
                        "Sir, my apologies for the interruption, but the battery is now at 15 percent. It is recommended to plug in the charger.",
                    )
                elif percentage == 10:
                    alert_and_speak(
                        percentage,
                        "Sir, I must inform you, the battery has reached 10 percent. Immediate charging is advised to avoid sudden shutdown.",
                    )
                elif percentage == 5:
                    alert_and_speak(
                        percentage,
                        "Sir, urgent attention needed: The battery is critically low at 5 percent. Please connect the charger right away to prevent shutdown.",
                    )
        time.sleep(10)


def check_Plug():
    """Monitors changes in the plug-in state and triggers appropriate notifications."""
    previous_state = psutil.sensors_battery().power_plugged
    while True:
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                alert_thread = threading.Thread(target=Alert, args=("Charger plugged in",))
                speak_thread = threading.Thread(target=speak, args=("Sir, just to let you know, the device is now plugged in and charging.",))
            else:
                alert_thread = threading.Thread(target=Alert, args=("Charger unplugged",))
                speak_thread = threading.Thread(target=speak, args=("Sir, the device has been unplugged. Please monitor the battery level closely.",))
           
            alert_thread.start()
            speak_thread.start()   
            alert_thread.join()
            speak_thread.join()
            
            previous_state = battery.power_plugged

        time.sleep(10)
