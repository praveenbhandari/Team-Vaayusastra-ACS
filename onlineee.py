from smbus2 import SMBus,i2c_msg
 
addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
 
print ("Enter 1 for ON or 0 for OFF")
while numb == 1:
 
    ledstate = input(">>>>   ")
    #bus,write
    if ledstate == "1":
        bus.write_byte(addr, 0x01) # switch it on
    elif ledstate == "0":
        bus.write_byte(addr, 0x00) # switch it on
    else:
        numb = 0
bus.close()
 