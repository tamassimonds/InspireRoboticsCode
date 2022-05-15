#Used to control robot with keyboard
import requests
import time

import motor_controller as mc 



from pynput.keyboard import Key, Listener
print("wroking")
def on_press(key):
    print('{0} pressed'.format(
        key))
    try:
        if key.char == ('w'):
            mc.motor3_forward()
            mc.motor1_backward()
        
        if key.char == ('s'):
            mc.motor1_forward()
            mc.motor3_backward()
        if key.char == ('a'):
            mc.motor2_forward()
        if key.char == ('d'):
            mc.motor2_backward()
    except:
        pass
def on_release(key):
    print('{0} release'.format(
        key))
    try:
            
        if key.char == ('w'):
            mc.motor3_stop()
            mc.motor1_stop()
        if key.char == ('s'):
            mc.motor3_stop()
            mc.motor1_stop()
        if key.char == ('a'):
            mc.motor2_stop()
        if key.char == ('d'):
            mc.motor2_stop()
    
        if key == Key.esc:
            # Stop listener
            return False
    except:
        pass
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()