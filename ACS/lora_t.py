import  RPi.GPIO  as  GPIO 
from  time  import sleep
from  SX127x.LoRa  import  * 
from  SX127x.board_config  import BOARD
GPIO . setwarnings ( False )

BOARD . setup()
lora = LoRa()

lora . set_dio_mapping ([ 0 ] *  6 )

lora . set_freq ( 433 )
lora . set_bw (BW . BW62_5)
lora . set_spreading_factor ( 9 )
lora . set_coding_rate (CODING_RATE . CR4_5)
lora . set_preamble ( 8 )

lora . set_mode (MODE . RXCONT)

while  True :
    sleep ( 0.5 )
    flags = lora . get_irq_flags ()
     #print flags ["rx_done"], flags ["valid_header"] 
    #print flags
    
    if flags [ "rx_done" ] == 1  and flags [ "valid_header" ] == 1 :
         if flags [ "crc_error" ] == 0 :
            payload = lora . read_payload (nocheck = True )
            mystring = "" 
            for char in payload:
                mystring = mystring +  chr (char)
            print(mystring)
            lora . set_irq_flags (rx_done = None , valid_header = None , crc_error = None )
