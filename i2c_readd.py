from smbus import SMBus
 
addr = 0x04 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
 
print ("Enter 1 for ON or 0 for OFF")
while True:
    bb=bus.read_byte(addr)
    print(bb)
    
