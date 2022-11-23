import RPi.GPIO as GPIO
import time
import sys

#my imports 
import user_db
import behave


#initializing realtime database

db = user_db.User_db("somemail@mail.com", "Admin1234#")#use this function to post to db db.data_send("temp", "humid", "motion", "smoke", "rfid white")



# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9 
SPIMOSI = 10
SPICS = 7

#mq2_dpin = 0 #uncomment to use digital pin of the smoke sensor
mq2_apin = 4

#port init
def init():
         GPIO.setwarnings(False)
         GPIO.setmode(GPIO.BCM) #to specify whilch pin numbering system

         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         #GPIO.setup(mq2_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #uncomment to use digital pin of the smoke sensor


#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, GPIO.HIGH)	
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

#            uncomment below if you wish to use the digital pin of the smoke sensor 
             #if GPIO.input(mq2_dpin):
                #print("Gas not leak")
                #time.sleep(0.5)

             try:
                 gas_str_val = "%.2f"%((COlevel/1024.)*3.3) #String type of the gas value
                 gas_val = float(gas_str_val) #Float type of the gas value
                 gas_str= gas_str_val +" V" #concatenated string to be displayed on terminal

                 #Make action based on the gas value level
                 if gas_val >= 0.1:
                     behave.alarm_on() #turn the alarm on
                     print("Alarm turned on")
                 else:
                     behave.alarm_off() #turn the alarm off

                 #sys.stdout.write("\n\rCurrent Gas AD vaule "  + gas_str) #update the same value instead of printing a new line, need to import sys library for this
                 print("\tCurrent Gas AD vaule "  + gas_str,  end='\n\n') 
                 db.data_send_set(None,None, None, gas_str, None) 
                 time.sleep(3)
             except:
                 print ("something wrong heappened")
                 exit(1)
             if stop():
                 return


if __name__ =='__main__':
         try:
             check_smoke(lambda: False)
         except KeyboardInterrupt:
             GPIO.cleanup()
             exit(1)

