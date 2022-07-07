#! /usr/bin/python

from  time  import sleep
from  SX127x.LoRa  import  * 
from  SX127x.board_config  import BOARD

BOARD.setup()

rssi_value=0

class  LoRaRcvCont (LoRa):
    def  __init__(self,verbose = False):
        super(LoRaRcvCont,self ).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([ 0 ]*6)

    def  on_rx_done(self):
        print(" \n Received data:")
        self.clear_irq_flags(RxDone=1)
        payload=self.read_payload(nocheck = True)
        mystring="" 
        for char in payload:
            mystring = mystring+chr(char)
        print ("RSSI:",rssi_value)
        print(mystring)
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def  on_cad_done( self ):
        print(" \n on_CadDone" )
        print(self.get_irq_flags())

    def  on_rx_timeout( self ):
        print( " \n on_RxTimeout" )
        print(self.get_irq_flags())

    def  on_valid_header(self):
        print( " \n on_ValidHeader" )
        print(self.get_irq_flags())

    def  on_payload_crc_error ( self ):
        print( " \n on_PayloadCrcError" )
        print(self.get_irq_flags())

    def  start ( self ):
        self. reset_ptr_rx ()
        self . set_mode (MODE . RXCONT)
        global rssi_value
        while  True :
            sleep ( .5 )
            rssi_value =  self . get_rssi_value ()

lora = LoRaRcvCont (verbose = False )
lora . set_mode (MODE . STDBY)
lora . set_pa_config (pa_select = 1 )
lora . set_freq ( 433 )
lora . set_bw (BW . BW62_5) # BW7_8 BW10_4 BW15_6 BW20_8 BW31_25 BW41_7 BW62_5 BW125 BW250 BW500 
lora . set_spreading_factor ( 9 ) # 6 - 12 
lora . set_rx_crc ( True )
lora . set_coding_rate (CODING_RATE . CR4_5) # CR4_5 CR4_6 CR4_7 CR4_8 Default is CR4_5 
lora . set_preamble ( 8 )
 # lora.set_pa_config (max_power = 0, output_power = 0) 
# lora.set_lna_gain (GAIN.G1) 
# lora.set_implicit_header_mode (False) 
# lora.set_low_data_rate_optim (True) 
# lora.set_pa_ramp (PA_RAMP.RAMP_50_us) 
# lora.set_agc_auto_on (True)

print (lora)
assert (lora . get_agc_auto_on () ==  1 )
try : input ( "Press enter to start ..." )
except : pass

try :
    lora . start ()
except  KeyboardInterrupt :
    sys . stdout . flush ()
    print ( "" )
    sys . stderr . write ( "KeyboardInterrupt \n " )
finally :
    sys . stdout . flush ()
    print ( "" )
    lora . set_mode (MODE . SLEEP)
    print (lora)
    BOARD . teardown ()