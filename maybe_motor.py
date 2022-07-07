import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
p = GPIO.PWM(18, 50)

p.start(0)
print ("starting 0")
time.sleep(3)

p.ChangeDutyCycle(3)
print("start")
time.sleep(5)
#p.ChangeDutyCycle(6.5) ##40 %
#p.ChangeDutyCycle(7) ##50 %
#p.ChangeDutyCycle(7.5) ##50-60 %
#time.sleep(5)
#p.ChangeDutyCycle(8) #60%
#p.ChangeDutyCycle(8.5) #60-70%
#p.ChangeDutyCycle(9) #75%
#p.ChangeDutyCycle(9.5) #80%
p.ChangeDutyCycle(10) #100%



            time.sleep(2)
            p.ChangeDutyCycle(3)
            print("start")
            time.sleep(0.5)
            p.ChangeDutyCycle(6.5) ##40 %
            time.sleep(1)
            p.ChangeDutyCycle(7) ##50 %
            time.sleep(1.5)
            p.ChangeDutyCycle(7.5) ##50-60 %
            time.sleep(2)
            p.ChangeDutyCycle(8) #60%
            time.sleep(2.5)
            p.ChangeDutyCycle(8.5) #60-70%
            time.sleep(3)
            p.ChangeDutyCycle(9) #75%
            time.sleep(3.5)
            p.ChangeDutyCycle(9.5) #80%
            time.sleep(4)
            p.ChangeDutyCycle(10) #100%
 

