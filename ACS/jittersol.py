import RPi.GPIO as GPIO
import pigpio
import time

servo=19
servo1=13
pwm=pigpio.pi()
lpwm=pigpio.pi()
pwm.set_mode(servo,pigpio.OUTPUT)
lpwm.set_mode(servo1,pigpio.OUTPUT)
while True:
    pwm.set_PWM_frequency(servo,50)
    lpwm.set_PWM_frequency(servo1,50)
    print("0 deg")
    pwm.set_servo_pulsewidth(servo,500)
    lpwm.set_servo_pulsewidth(servo1,500)
    time.sleep(3)

    print("90 deg")
    pwm.set_servo_pulsewidth(servo,1500)
    lpwm.set_servo_pulsewidth(servo1,1500)
    time.sleep(3)

    print("180 deg")
    pwm.set_servo_pulsewidth(servo,2500)
    lpwm.set_servo_pulsewidth(servo1,2500)
    time.sleep(3)
