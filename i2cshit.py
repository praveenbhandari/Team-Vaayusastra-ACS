from smbus2 import SMBus
 
addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
 
print ("Enter 1 for ON or 0 for OFF")
while True:
    data=[1,2,3,4,5,6,7,8]
#    data=input("something")
    bus.write_i2c_block_data(addr,0,data)
    

#    bus.write_i2c_block_data(addr, 0 ,data)
#    ledstate = input(">>>>   ")
 
 #   if ledstate == "1":
  #      bus.write_byte(addr, 0x1) # switch it on
   # elif ledstate == "0":
    #    bus.write_byte(addr, 0x0) # switch it on
    #else:
     #   numb = 0
 