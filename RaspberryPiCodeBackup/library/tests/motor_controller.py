import argparse
import pyrebase

import RPi.GPIO as GPIO


Motor1A = 35  #Left F
Motor1B = 36
Motor2A = 37  #Right F
Motor2B = 38
Motor1A = 35  #Left F
Motor1B = 36
Motor3A = 15  #Right F
Motor3B = 16

GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)




def set_motor1_speed(speed):
    

    if speed == 100:
        motor1_forward()
    elif speed == -100:
        motor1_backward()
    elif speed == 0:
        motor1_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor2_speed(speed):

    if speed == 100:
        motor2_forward()
    elif speed == -100:
        motor2_backward()
    elif speed == 0:
        motor2_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor3_speed(speed):

    if speed == 100:
        motor3_forward()
    elif speed == -100:
        motor3_backward()
    elif speed == 0:
        motor3_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")
    

 
def motor1_forward():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    
def motor1_backward():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

def motor1_stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)

def motor2_forward():
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    
def motor2_backward():
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)

def motor2_stop():
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

def motor3_forward():
    GPIO.output(Motor3B,GPIO.LOW)
    GPIO.output(Motor3A,GPIO.HIGH)

def motor3_backward():
    GPIO.output(Motor3B,GPIO.HIGH)
    GPIO.output(Motor3A,GPIO.LOW)

def motor3_stop():
    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.LOW)

def stop_all():
    motor1_stop()
    motor2_stop()
    motor3_stop()
    
