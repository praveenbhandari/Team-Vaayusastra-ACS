import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 1000)
p.start(10)
input('Press return to stop:') 
p.stop()
GPIO.cleanup()