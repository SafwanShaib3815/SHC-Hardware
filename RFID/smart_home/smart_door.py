# getting the main GPIO libraly
import RPi.GPIO as GPIO 
import time # getting the time libraly
#from threading import Thread 
from firebase import firebase
import datetime

#from mfrc522 import SimpleMFRC522

#my imports
import rfid #script to read the rfid tags
import behave #responce actions  script
import blink #blinking led script
#import temp_humid #temperature and humidity sensor script 
import user_db

pinsOut = [6,13,19,26] #creating a list (array) with the number of GPIO's that we use 
led_out = 23
#stop_blink_thread=False
GPIO.setwarnings(False)
name=""

#initializing the firebase object
db = user_db.User_db("somemail@mail.com", "Admin1234#")#use this function to post to the realtime database db.data_send("Temperature", "Humidity", "Motion", "Smoke", "rfid ")


        
while True:
    ## Thread to to activate Temp-Humid sensor
    #stop_blink_thread=False #allows the thread to go on
    #blink_thread = Thread(target=blink.blink_led, args=(led_out, lambda : stop_blink_thread, ))#instenciating a thread for the blink task
    #blink_thread.start()

    print("\n\n\nRFID sensor active...")#opening message
    id = rfid.read_rfid()
    #if white card taped
    if id == 291269522084:
        #stop_blink_thread=True #causes the blinking thread to terminate
        #blink_thread.join()
        print("\nMr. White is allowed to enter>>>>>>\n")
        behave.open_door() #opens the door
        name = "Mr White"
        print ("****************************\n--Door closed Mr. White\n****************************")	

    #if blue fob taped
    elif id == 347986796008:
        print("Mr. Blue is allowed to enter>>>>>>\n")#removing the warings 
        #stop_blink_thread=True #causes the blinking thread to terminate
        #blink_thread.join()
        behave.open_door() #oepns the door 
        name = "Mr Blue"
        
        print ("****************************\n--Door closed Mr. Blue\n****************************")

    
    else:
        #actions to do in case of unuthorized people
        print("Unauthorized person!!")
        GPIO.setmode(GPIO.BCM) #setting the mode for output pins
        #stop_blink_thread=True #causes the blinking thread to terminate
        GPIO.setup(led_out, GPIO.OUT) 
        GPIO.output(led_out, GPIO.LOW) #turn indicator led OFF while unauthorized person trying to enter
        time.sleep(1.5)

        #Values to be sent to DB
        name = "Unauthorized user attempt!"
    db.data_send_set(None, None, None, None, name)
    db.data_send_push(None, None, None, None, name)


       
    if KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()
