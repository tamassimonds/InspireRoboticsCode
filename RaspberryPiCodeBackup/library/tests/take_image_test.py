from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()
camera.vflip = True

print(os.getcwd() + "/testImage.jpg")


camera.capture(os.getcwd() + "/testImage.jpg")
