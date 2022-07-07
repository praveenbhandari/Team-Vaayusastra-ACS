'''import time
import cv2
import numpy as np
import math
import RPi.GPIO as gpio
 #import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(35,gpio.OUT)
pwm=gpio.PWM(35, 50)
pwm.start(0)
print('waiting for 2 seconds')
time.sleep(2)
Xposition = 90
#Yposition = 90
#for i in range(0,1)
Xposition += 30
pwm.ChangeDutyCycle(1)'''
import RPi.GPIO as GPIO
import time

servo = 35

GPIO.setmode( GPIO.BCM )
GPIO.setup( servo, GPIO.OUT )

# info on frequency and PWM formula at https://rpi.science.uoit.ca/lab/servo/
pwm = GPIO.PWM( servo, 50 )
pwm.start( 2.5 )

print( "0 deg" )
pwm.ChangeDutyCycle( 2.5 )  # turn towards 0 degree
time.sleep( 3 )

print( "90 deg" )
pwm.ChangeDutyCycle( 7.5 )  # turn towards 90 degree
time.sleep( 3 )

print( "180 deg" )
pwm.ChangeDutyCycle( 12.5 ) # turn towards 180 degree
time.sleep( 3 )

pwm.stop()
GPIO.cleanup()