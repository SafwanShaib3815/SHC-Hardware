# getting the main GPIO libraly
import RPi.GPIO as GPIO 
import time # getting the time libraly
from threading import Thread 
from firebase import firebase
from firebase import firebase

#from mfrc522 import SimpleMFRC522

#my imports
import rfid #script to read the rfid tags
import behave #responce actions  script
import blink #linking led script
#import temp_humid #temperature and humidity sensor script 

pinsOut = [6,13,19,26] #creating a list (array) with the number of GPIO's that we use 
led_out = 23
stop_blink_thread=False
GPIO.setwarnings(False)
name=""
ID=0
#initializing the firebase object
myDB = firebase.FirebaseApplication("https://smarthomecontroller-a7978-default-rtdb.firebaseio.com/", None)

while True:
    ## Thread to to activate Temp-Humid sensor
    stop_blink_thread=False #allows the thread to go on
    blink_thread = Thread(target=blink.blink_led, args=(led_out, lambda : stop_blink_thread, ))#instenciating a thread for the blink task
    blink_thread.start()

    print("\n\n\nRFID sensor active...")#opening message
    id = rfid.read_rfid()
    #if white card taped
    if id == 291269522084:
        stop_blink_thread=True #causes the blinking thread to terminate
        blink_thread.join()
        print("\nMr. White is allowed to enter>>>>>>\n")
        behave.open_door() #opens the door
        name = "Mr White"
        ID = id
        print ("****************************\n--Door closed Mr. White\n****************************")	

    #if blue fob taped
    elif id == 347986796008:
        print("Mr. Blue is allowed to enter>>>>>>\n")#removing the warings 
        stop_blink_thread=True #causes the blinking thread to terminate
        blink_thread.join()
        behave.open_door() #oepns the door 
        name = "Mr Blue"
        ID = id

        print ("****************************\n--Door closed Mr. Blue\n****************************")

    else:
        print("Unauthorized person!!")
        GPIO.setmode(GPIO.BCM) #setting the mode for output pins
        GPIO.setup(pinsOut, GPIO.OUT) #output pins configured to out
        stop_blink_thread=True #causes the blinking thread to terminate
        GPIO.setup(led_out, GPIO.OUT) 
        GPIO.output(led_out, GPIO.LOW) #turn indicator led OFF while unauthorized person trying to enter
        #time.sleep()
        GPIO.output(pinsOut, GPIO.LOW) 
        time.sleep(1.5)
        GPIO.output(pinsOut, GPIO.HIGH)
        name = "Unauthorized user attempt!"
        ID = id
    data= {
        "name": name,
        "ID" : ID 
        }

    #print(data)
    myDB.post("Door Records",data)

if KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
