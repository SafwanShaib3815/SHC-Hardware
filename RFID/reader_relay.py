# getting the main GPIO libraly
import RPi.GPIO as GPIO
#import script to read the rfid tags
import Read
# getting the time libraly
import time
#creating a list (array) with the number of GPIO's that we use 
pins = [6,13,19,26] 

while True:
    id = Read.read_frid()

    #for loop where GPIO= 6 next 13 ,19, 26 
    if id == 291269522084:
        # setting a current mode
        GPIO.setmode(GPIO.BCM)
        #removing the warings 
        GPIO.setwarnings(False)
        #setting the mode for all pins so all will be switched on 
        GPIO.setup(pins, GPIO.OUT)
        print("WHITE card is allowed to enter")
        for pin in pins :
            #setting the GPIO to HIGH or 1 or true
            GPIO.output(pin,  GPIO.HIGH)
            #wait 0,5 second
            time.sleep(0.5)
            #setting the GPIO to LOW or 0 or false
            GPIO.output(pin,  GPIO.LOW)
            #wait 0,5 second
            time.sleep(0.5)
            #Checking if the current relay is running and printing it 
            if not GPIO.input(pin) : 
                print("Pin "+str(pin)+" is working" )
        GPIO.cleanup()
        print ("Shutdown All relays")	
    #same but the difference is that  we have 
    #for loop where pin = 26 next 19,13,6
    # backwards
    elif id == 347986796008:
        # setting a current mode
        GPIO.setmode(GPIO.BCM)
        #setting the mode for all pins so all will be switched on 
        GPIO.setwarnings(False)
        GPIO.setup(pins, GPIO.OUT)
        print ("BLUE tag is allowed to enter")
        for pin in reversed(pins) :
            GPIO.output(pin,  GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin,  GPIO.LOW)
            time.sleep(0.5)
            #Checking if the current relay is running and printing it 
            if not GPIO.input(pin) : 
                print("Pin "+str(pin)+" is working" )
        #cleaning all GPIO's 
        GPIO.cleanup()
        print ("Shutdown All relays")
    else:
        print("Unauthorized user!")
        GPIO.setmode(GPIO.BCM)
        #setting the mode for all pins so all will be switched on 
        GPIO.setwarnings(False)
        GPIO.setup(pins, GPIO.OUT)

        GPIO.output(pins, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(pins, GPIO.HIGH)
        GPIO.cleanup()


