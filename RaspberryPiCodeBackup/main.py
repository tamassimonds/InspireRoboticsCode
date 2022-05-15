#This is where students write there code

if __name__ == "__main__":
    print("SETTTING UP")

import time


import os, sys
sys.path.insert(0,'library')# insert the folder lib in system path
import motor_controller as mc
import controller

#Values from your arduiono


#Debug Settings
PRINT_SENSOR_DATA = True 


last_move = ""


def mainLoop():
    #This is where students will run there code
    #This is also the main while loop of the codebase
    
    while True:
        controller.update()
        (D1Value, D2Value, D3Value, pitch, yaw, roll) = controller.getArduinoValues()
        #print("test")
        center, radius = controller.getBallPosCamera()
        
        if PRINT_SENSOR_DATA:
            controller.printAllSensorData(D1Value, D2Value, D3Value, yaw, roll, pitch ,center, radius)

        #controller.followBall(center, radius)

        #print(D1Value, D2Value, D3Value, yaw, roll, pitch ,center, radius)
        
        #print(D1Value)
        
        



if __name__ == "__main__":
    print("CONFIGURATION COMPLETE")
    mainLoop()



