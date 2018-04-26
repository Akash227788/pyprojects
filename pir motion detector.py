
# coding: utf-8

# In[ ]:


import RPi.GPIO as GPIO
import time
import os
import datetime
import sys


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            fswebcam f 5 -f 10 -r 1280x720 image2.jpg
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()

