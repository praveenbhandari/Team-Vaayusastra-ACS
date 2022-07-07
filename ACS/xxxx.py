import time
from xbee import XBee
SERIAL_PORT = "/dev/ttyS0"
BAUD_RATE = 9600

# set the pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE)
xbee = XBee(ser, escaped=False)
while True:
    xbee.send('tx',dest_addr=b'\x00\xFF', data="testtttt")
print(xbee.wait_read_frame())

ser.close()