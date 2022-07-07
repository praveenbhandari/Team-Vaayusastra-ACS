import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)
p.start(0)
time.sleep(10)

p.ChangeDutyCycle(3)
time.sleep(10)