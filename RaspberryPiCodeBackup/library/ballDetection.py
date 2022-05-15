#Detects the ball through Camera

# import the necessary packages
from collections import deque
from picamera import PiCamera
from picamera.array import PiRGBArray
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import cv2
import imutils
import time
import motor_controller as mc
import io

WIDTH = 300
SHOWIMAGE = False
BALLINFRONTRANGE = WIDTH/4


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())







# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (0, 141, 149)
greenUpper = (255, 255, 255)
pts = deque(maxlen=args["buffer"])

# # if a video path was not supplied, grab the reference
# # to the webcam

time.sleep(2.0)

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
# start the FPS counter
fps = FPS().start()


last_move = ""


# keep looping
def detectBall():
    
	# grab the current frame
    e1 = cv2.getTickCount()
   
    
    
    frame = vs.read()
   

    frame = imutils.resize(frame, width=WIDTH)

    
    # resize the frame, blur it, and convert it to the HSV
    # color space
    #frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    # only proceed if at least one contour was found
    
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    e2 = cv2.getTickCount()
    timepassed = (e2 - e1)/ cv2.getTickFrequency()
    if center == None:
        radius = None
    # update the points queue
    
    #print("Pos: ",center,"Radius: ",radius)
    
    #print(timepassed)
    return (center, radius)
    