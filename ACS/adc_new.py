
import board
import time
import busio

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS     #change to ads1115 if you’re using ads1115 module

from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)         #change to ads1115 if you’re using ads1115 module

chan = AnalogIn(ads, ADS.P0)
while True:
    print(chan.value)
    time.sleep(0.5)