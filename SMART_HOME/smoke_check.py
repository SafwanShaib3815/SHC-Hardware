import RPi.GPIO as GPIO
import time
import sys
import user_db

#initializing realtime database

db = user_db.User_db("somemail@mail.com", "Admin1234#")#use this function to post to db db.data_send("temp", "humid", "motion", "smoke", "rfid white")



# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9 
SPIMOSI = 10
#chip select pins
SPICS = 7
rfidcs = 8

mq2_dpin = 0 
mq2_apin = 4

indicator = 23

#port init
def init():
         GPIO.setwarnings(False)
         #GPIO.cleanup() #clean up at the end of your script
         GPIO.setmode(GPIO.BCM) #to specify whilch pin numbering system
         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         GPIO.setup(rfidcs, GPIO.OUT)
         GPIO.setup(mq2_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, GPIO.HIGH)	
        GPIO.output(rfidcs, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)  # start clock low
        GPIO.output(cspin, GPIO.LOW)     # bring CS low

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

        GPIO.output(cspin, GPIO.HIGH)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
def check_smoke(stop):
         init()

         print("Smoke sensor warming up, please wait 2 seconds ...")
         time.sleep(2)
         while True:
             COlevel=readadc(mq2_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
             v =  str("%.2f"%((COlevel/1024.)*3.3))+" V"
             #if GPIO.input(mq2_dpin):
                #print("Gas not leak")
                #time.sleep(0.5)

             try:
                gas_val = str("%.2f"%((COlevel/1024.)*3.3))+" V"
                #sys.stdout.write("\n\rCurrent Gas AD vaule "  + gas_val )
                print("\tCurrent Gas AD vaule "  + gas_val,  end='\n\n') 
                db.data_send_set(None,None, None, gas_val, None) 
                time.sleep(3)
             except:
                print ("something wrong heappened")
                #GPIO.cleanup()
                exit(1)
             if stop():
                return

if __name__ =='__main__':
         try:
             check_smoke(lambda: False)
         except KeyboardInterrupt:
             #GPIO.cleanup()
             exit(1)

