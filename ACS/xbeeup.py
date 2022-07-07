#!/usr/bin/env python3
#
# Acts as a receiver of data from a sending XBee module, and controls
# LEDs (up, down, left, right) associated with the codes sent by the trasmitter.
# See README for additional information.
#
# **NOTE: REQUIRES PYTHON 3**

import serial, time
import RPi.GPIO as GPIO
from xbee import XBee

GPIO.output(21,GPIO.HIGH)
# assign the LED pins and XBee device settings

SERIAL_PORT = "/dev/ttyS0"
BAUD_RATE = 9600

# set the pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# initialize GPIO outputs for LEDsfor l in [LED_UP_PIN, LED_DOWN_PIN, LED_LEFT_PIN, LED_RIGHT_PIN]:


# handler for whenever data is received from transmitters - operates asynchronously
def receive_data(data):
    print("Received data: {}".format(data))
    rx = data['rf_data'].decode('utf-8')
    print(rx)
    state, led = rx[:1], rx[1:]
    if rx[1:] ==  "up":
        GPIO.output(21,GPIO.HIGH )
    # parse the received contents and activate the respective LED if the data
    # received is actionable
    else:
        print("ERROR: Received invalid STATE '{}' - ignoring transmission".format(state))

    print("Packet: {}".format(data))
    print("Data: {}".format(data['rf_data']))

# configure the xbee and enable asynchronous mode
ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE)
xbee = XBee(ser, callback=receive_data, escaped=False)

while True:
    try:
        # operate in async mode where all messages will go to handler
        time.sleep(0.001)
    except KeyboardInterrupt:
        break

# clean up
GPIO.cleanup()
xbee.halt()
ser.close()