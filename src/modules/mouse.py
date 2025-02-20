import time
from pynput.mouse import Controller

mouse = Controller()


start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 5: 
        break
    else :
        mouse.position = (0, 0)  
