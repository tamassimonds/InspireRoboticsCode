
#!/usr/bin/python3



import serial
import time

import requests
import time
import colors

lastDistance = 0



try:
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout =5)
except:
    try:
        ser = serial.Serial('/dev/ttyACM1', 115200, timeout =5)
    except:
        try:
            ser = serial.Serial('/dev/ttyACM2', 115200, timeout =5)
        except:
            try:
                ser = serial.Serial('/dev/ttyACM3', 115200, timeout =5)
            except:
                try:
                    ser = serial.Serial('/dev/ttyACM4', 115200, timeout =5)
                except:
                    pass

# read from Arduino


input = ""



def parseInput(input, sensorData):
    
    #Takes the input from the arduino and parses the strin into its values

    #The format used it
    # D#  for distance sensor, # is the number of the distance sensor 1-3
    # IMU gives the pitch roll and yaw
    arduinoData = input.split("\n")

    for data in arduinoData:
        #print(data)
        if "DS1" in data:
            distanceSensor1 = float(data.split(" ")[1])
            sensorData["DS1"] = distanceSensor1
        if "DS2" in data:
            distanceSensor2 = float(data.split(" ")[1])
            sensorData["DS2"] =  distanceSensor2
        if "DS3" in data:
            distanceSensor3 = float(data.split(" ")[1])
            sensorData["DS3"] = distanceSensor3
        if "Pitch" in data:
            sensorData["pitch"] = float(data.split(" ")[1])
            sensorData["roll"] = float(data.split(" ")[3])
            sensorData["yaw"] = float(data.split(" ")[5])
            
 
    return sensorData
    

def readArduinoData():
    sensorData = {}
    #Below is some very bad code but it works and its 1am so it will do
    #Good luck debugging this if it doesn't work though

    #the for loop is a bit of a botch but it just reads a few lines before updating the values
    #The issue was the program is single threaded so if we just read one value form the arduino we would them have to wait
    #for the camera program to execture
    #the program is I/O bound so this was a bottle neck
    for i in range(5):
       
        if ser.in_waiting > 0:
            try:
                input = ser.readline().decode("utf-8").rstrip()                
            except:
                input = ""
                print(f"{colors.FAIL }ERROR: Unable to read Data from arduino, please check wiring{colors.ENDC}")
            
        
            
            if input == "":
                pass
            else:
                
                sensorData = parseInput(input, sensorData)
       
    
    ser.flushInput()
    return sensorData