from Automation.Automation_Brain import Auto_main_brain,clear_file
from NetHyTech_STT import listen
import threading
from Automation.Battery import battery_alert,check_Percentage,check_Plug
from Time_Operations.brain import input_manage


numbers = ["1:","2:","3:","4:","5:","6:","7:","8:","9:","0:",]

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt" , "r") as file:
            input_text = file.read().lower()
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("tell me"):
                output_text = output_text.replace(" p.m.","PM")
                output_text = output_text.replace(" a.m.","AM")
                for number in numbers:
                    if number in output_text:
                        output_text = output_text.replace(number,f"0{number}")
                        input_manage(output_text)
                        clear_file()
            else :
                Auto_main_brain(output_text)
            
        else:   
            pass
        

def Jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

