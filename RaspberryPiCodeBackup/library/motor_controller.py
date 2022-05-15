#Interfaces with motors
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

fPWM = 100  # Hz (not higher with software PWM)


pwmMotor1A = GPIO.PWM(Motor1A, fPWM)
pwmMotor1A.start(0)
pwmMotor1B = GPIO.PWM(Motor1B, fPWM)
pwmMotor1B.start(0)
pwmMotor2A = GPIO.PWM(Motor2A, fPWM)
pwmMotor2A.start(0)
pwmMotor2B = GPIO.PWM(Motor2B, fPWM)
pwmMotor2B.start(0)
pwmMotor3A = GPIO.PWM(Motor3A, fPWM)
pwmMotor3A.start(0)
pwmMotor3B = GPIO.PWM(Motor3B, fPWM)
pwmMotor3B.start(0)


def set_motor1_speed(speed):
    

    if speed > 0:
        motor1_forward(speed)
    elif speed < 0:
        motor1_backward(abs(speed))
    elif speed == 0:
        motor1_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor2_speed(speed):

    if speed > 0:
        motor2_forward(speed)
    elif speed < 0:
        motor2_backward(abs(speed))
    elif speed == 0:
        motor2_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor3_speed(speed):

    if speed > 0:
        motor3_forward(speed)
    elif speed < 0:
        motor3_backward(abs(speed))
    elif speed == 0:
        motor3_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")
    

 
def motor1_forward(speed=100):
    pwmMotor1A.ChangeDutyCycle(0)
    pwmMotor1B.ChangeDutyCycle(speed)
    
def motor1_backward(speed=100):
    pwmMotor1A.ChangeDutyCycle(speed)
    pwmMotor1B.ChangeDutyCycle(0)


def motor1_stop():
    pwmMotor1B.ChangeDutyCycle(0)
    pwmMotor1A.ChangeDutyCycle(0)


def motor2_forward(speed=100):
    pwmMotor2A.ChangeDutyCycle(0)
    pwmMotor2B.ChangeDutyCycle(speed)
    
def motor2_backward(speed=100):
    pwmMotor2A.ChangeDutyCycle(speed)
    pwmMotor2B.ChangeDutyCycle(0)
    

def motor2_stop():
    pwmMotor2B.ChangeDutyCycle(0)
    pwmMotor2A.ChangeDutyCycle(0)

def motor3_forward(speed=100):
    pwmMotor3A.ChangeDutyCycle(0)
    pwmMotor3B.ChangeDutyCycle(speed)
    
def motor3_backward(speed=100):
    pwmMotor3A.ChangeDutyCycle(speed)
    pwmMotor3B.ChangeDutyCycle(0)
    

def motor3_stop():
    pwmMotor3B.ChangeDutyCycle(0)
    pwmMotor3A.ChangeDutyCycle(0)

def stop_all():
    motor1_stop()
    motor2_stop()
    motor3_stop()
    
