import keyboard
loop = ""

count = 0
import motor_controller as mc 
keysPressed = {"w": False, "a": False, "s": False, "d": False} 


while True:
    if keyboard.is_pressed("w"):
        #W Pressed
        if keysPressed["w"] == False:
            keysPressed["w"] = True
            print("You pressed w")
            mc.motor3_forward()
            mc.motor1_backward()
            

    else:
        #W Released
        if keysPressed["w"] == True:
            keysPressed["w"] = False
            print("w released")
            mc.motor3_stop()
            mc.motor1_stop()

    
    if keyboard.is_pressed("a"):
        #a Pressed
        if keysPressed["a"] == False:
            keysPressed["a"] = True
            print("You pressed a")
            mc.motor2_forward()
    else:
        #a Released
        if keysPressed["a"] == True:
            keysPressed["a"] = False
            print("a released")
            mc.motor2_stop()

    if keyboard.is_pressed("s"):
        #s Pressed
        if keysPressed["s"] == False:
            keysPressed["s"] = True
            print("You pressed s")
            mc.motor1_forward()
            mc.motor3_backward()
    else:
        #s Released
        if keysPressed["s"] == True:
            keysPressed["s"] = False
            print("s released")
            mc.motor3_stop()
            mc.motor1_stop()

    if keyboard.is_pressed("d"):
        #d Pressed
        if keysPressed["d"] == False:
            keysPressed["d"] = True
            print("You pressed d")
            mc.motor2_backward()
    else:
        #d Released
        if keysPressed["d"] == True:
            keysPressed["d"] = False
            print("d released")
            mc.motor2_stop()

    
