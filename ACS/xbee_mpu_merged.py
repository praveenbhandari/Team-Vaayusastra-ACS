#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO
from mpu9250_i2c import *
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
#xbee = XBee(ser)
counter=0   

      
while True:
    try:
        ax,ay,az,gx,gy,gz = mpu6050_conv() # read and convert mpu6050 data
        mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    except:
        continue
    #some='x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az).encode('unicode_escape')
    
    #some=bytes("{}".format(ax), 'ascii')

    #some='x = {0:2.2f}'.format(ax).encode('unicode_escape').strip()
    #y = {1:2.2f}, z {2:2.2f}
    #xbee.write(data='test')
    #ser.write(some)
    #ser.write(str(ay).encode('utf-8'))
    #ser.write(str(az).encode('utf-8'))
    #time.sleep(1)
    #ser.write(str(format(gx)).encode('utf-8'))
    #ser.write(str(format(gy)).encode('utf-8'))
    #ser.write(str(format(gz)).encode('utf-8'))
    #time.sleep(1)
    #ser.write(str(format(mx)).encode('utf-8'))
    #ser.write(str(format(my)).encode('utf-8'))
    #ser.write(str(format(mz)).encode('utf-8'))
    #time.sleep(1)
    print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az))
    print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(gx,gy,gz))
    print('mag [uT]:   x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(mx,my,mz))



#    ser.write(str(format(ax)).encode('utf-8'))
#    ser.write(str(format(ay)).encode('utf-8'))
#    ser.write(str(format(ay)).encode('utf-8'))
    #time.sleep(0.5)
    #ser.write(str(format(mx,my,mz)).encode('utf-8'))
    #bytes("{}".format(data), 'utf-8')
    ser.write(str(counter).encode('unicode_escape'))
    time.sleep(1)
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