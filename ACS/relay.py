import RPi.GPIO as gpio
import time
#channel=20
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(35,gpio.OUT)

def mott_o(pin):
    gpio.output(pin,gpio.HIGH)
    time.sleep(1)

def mott_of(pin):
    gpio.output(pin,gpio.HIGH)
    time.sleep(1)
    
pwm=gpio.PWM(35, 50)
while(True):
    pwm.start(0)
    pwm.ChangeDutyCycle(5) # left -90 deg position
    time.sleep(1)
    print("onn")
    pwm.ChangeDutyCycle(7.5) # neutral position
    time.sleep(1)
    pwm.ChangeDutyCycle(10) # right +90 deg position
    time.sleep(1)
    print("off")
pwm.stop()
gpio.cleanup()