import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
if __name__ == '__main__':
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
   # GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pressed = False
    while True:
        # button is pressed when pin is LOW
        if not GPIO.input(BUTTON_GPIO):
            if not pressed:
                print("Connected")
                pressed = True
        # button not pressed (or released)
        else:
            pressed = False
            print("Released")
            p = GPIO.PWM(18, 50)
            p.start(0)
            print("start")
            p.ChangeDutyCycle(10) #100%
            
            GPIO.cleanup()
        time.sleep(0.1)