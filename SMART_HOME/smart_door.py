# getting the main GPIO libraly
import RPi.GPIO as GPIO 
import time # getting the time libraly
#from firebase import firebase
import datetime


#my imports
import rfid #script to read the rfid tags
import behave #responce actions  script
import user_db

pinsOut = [6,13,19,26] #creating a list (array) with the number of GPIO's that we use 
led_out = 23
#rfidcs = 8
#smkcs = 7
#stop_blink_thread=False
GPIO.setwarnings(False)
name=""

#initializing the firebase object
db = user_db.User_db("somemail@mail.com", "Admin1234#")#use this function to post to the realtime database db.data_send("Temperature", "Humidity", "Motion", "Smoke", "rfid ")

#GPIO.setmode(GPIO.BCM)

def check_door(stop):
        
    while True:
        print("\n\n\nRFID sensor active...")#opening message
        #GPIO.setup(rfidcs, GPIO.OUT)
        #GPIO.setup(smkcs, GPIO.OUT)
        
        #GPIO.output(rfidcs, True)
        #GPIO.output(smkcs, True)
        #GPIO.output(rfidcs, False)
        #time.sleep(1)
        id = rfid.read_rfid()
        time.sleep(3)
        #GPIO.output(rfidcs, True)
        #if white card taped
        if id == 291269522084:
            print("\nMr. White is allowed to enter>>>>>>\n")
            behave.open_door() #opens the door
            name = "Mr White"
            #if blue fob taped
        elif id == 347986796008:
            print("Mr. Blue is allowed to enter>>>>>>\n")#removing the warings 
            behave.open_door() #oepns the door 
            name = "Mr Blue"
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

        if stop():
            return
#GPIO.cleanup()


if __name__ == '__main__':
    check_door(lambda:False)
