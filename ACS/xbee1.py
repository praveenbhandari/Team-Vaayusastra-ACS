#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO
#from xbee import XBee

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5
 )

GPIO.output(17,GPIO.HIGH)
#xbee = XBee(ser, escaped=False)
counter=0       
      
while True:
    ser.write(str("counter: %d \n"%(counter)).encode('utf-8'))
    time.sleep(0.5)
    counter += 1 #unicode_escape
    try:
        x=str(ser.readline().decode('unicode_escape').strip())
    except:
        print("decode error")
    finally:
        print(x)
        if x == "1":
            print("detach")
            GPIO.output(17,GPIO.LOW)
            time.sleep(3)
            GPIO.output(17,GPIO.HIGH)
        else:
            print('intact')
            GPIO.output(17,GPIO.HIGH)
        #xbee.tx(dest_addr='\x0000\xFFFF', data='Hello World')
GPIO.cleanup()