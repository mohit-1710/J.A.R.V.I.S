import threading        
import random
from internet_Check import is_Online
from Alert import Alert
from DATA.DLG_Data import online_dlg, offline_dlg
from TextToSpeech.Fast_DF_TTS import speak
from co_Brain import Jarvis
from Automation.Battery import check_Plug
from Time_Operations.brain import  input_manage
from Time_Operations.throw_alert import check_schedule , check_alarm

alarm_path = r'C:\Users\Mohit\OneDrive\Documents\AI_Project\BOT\Alarm_data.txt'

def run_online_actions(dialog):
    try:
        t1 = threading.Thread(target=Alert, args=(dialog,))
        t2 = threading.Thread(target=speak, args=(dialog,))
        t3 = threading.Thread(target=check_Plug)
        t4 = threading.Thread(target=check_schedule)
        t5 = threading.Thread(target=Jarvis)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()


    except Exception as e:
        print(f"Error occurred in online actions: {e}")

def main():
    if is_Online():
        ran_online_dlg = random.choice(online_dlg)
        run_online_actions(ran_online_dlg)
        # Jarvis()
    else:
        ran_offline_dlg = random.choice(offline_dlg)
        Alert(ran_offline_dlg)


# check_alarm()