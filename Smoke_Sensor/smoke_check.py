import RPi.GPIO as GPIO
import time
import sys
import blink
from threading import Thread
import user_db

#initializing realtime database

db = user_db.User_db("somemail@mail.com", "Admin1234#")#use this function to post to db db.data_send("temp", "humid", "motion", "smoke", "rfid white")



# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9 
SPIMOSI = 10
SPICS = 7
mq2_dpin = 0 
mq2_apin = 4

stop_blink_thread = False
indicator = 23

#port init
def init():
         GPIO.setwarnings(False)
         GPIO.cleanup() #clean up at the end of your script
         GPIO.setmode(GPIO.BCM) #to specify whilch pin numbering system
         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         GPIO.setup(mq2_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)	

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
#main ioop
def check_smoke_blink():
         init()
         blink_thread = Thread(target=blink.blink_led, args=(indicator, lambda: stop_blink_thread,)) #start a new thread to blink indicator
         blink_thread.start()

         print("please wait...")
         time.sleep(1)
         while True:
                  COlevel=readadc(mq2_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                  v =  str("%.2f"%((COlevel/1024.)*3.3))+" V"
                  
                  if GPIO.input(mq2_dpin):
                           print("Gas not leak")
                           time.sleep(0.5)
                  try:
                      print("\n\nGas leakage")
                      gas_val = str("%.2f"%((COlevel/1024.)*3.3))+" V"
                      sys.stdout.write("\rCurrent Gas AD vaule %s "  + gas_val )
                      db.data_send_set(None,None, None, gas_val, None) 
                      #print("Current Gas AD vaule = %d" + str("%.2f"%((COlevel/1024.)*3.3))+" V")
                      time.sleep(1)
                  except:
                      print ("something wrong heappened")
                      GPIO.cleanup()
                      exit(1)

def check_smoke(stop):
         init()

         print("please wait...")
         time.sleep(1)
         while True:
                  COlevel=readadc(mq2_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                  v =  str("%.2f"%((COlevel/1024.)*3.3))+" V"
                  
                  if GPIO.input(mq2_dpin):
                           print("Gas not leak")
                           time.sleep(0.5)
                  try:
                      print("\n\nGas leakage")
                      gas_val = str("%.2f"%((COlevel/1024.)*3.3))+" V"
                      sys.stdout.write("\rCurrent Gas AD vaule %s "  + gas_val )
                      db.data_send_set(None,None, None, gas_val, None) 

                      time.sleep(1)
                  except:
                      print ("something wrong heappened")
                      GPIO.cleanup()
                      exit(1)
                  if stop():
                      return

if __name__ =='__main__':
         try:
             check_smoke(lambda: False)
         except KeyboardInterrupt:
             stop_blink_thread = True 
             GPIO.cleanup()
             exit(1)

GPIO.cleanup()
         
