#the purpose of this code is to test the keyboard module 

import keyboard
import threading 
import time

stop_event = threading.Event()

def push_to_stop(): 
    global stop_event 
    keyboard.wait('space')
    stop_event.set() 
    print(stop_event)

stop_thread = threading.Thread(target = push_to_stop)

stop_thread.start() 

for i in range(100): 
    print(i)
    time.sleep(1)
    if stop_event.is_set(): 
        break 

stop_thread.join()

print("Main thread: Final state of stop_event:", stop_event.is_set())



