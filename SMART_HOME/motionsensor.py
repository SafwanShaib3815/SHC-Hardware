import RPi.GPIO as GPIO
import time
import sys

#my imports
import user_db
import behave

db = user_db.User_db("somemail@mail.com", "Admin1234#")


motionInPin = 5 #Motion sensor signal pin
skip_send = None


def check_motion(stop):
    skip_send = None
    while True:
        GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
        #GPIO.setup(motionOutPin, GPIO.OUT)         #LED output pin
        i=GPIO.input(motionInPin)
        if i==0:                 #When output from motion sensor is LOW
            if not skip_send:#skip this if skip_send is true
                db.data_send_set(None, None, "No Motion Detected", None, None)
                print ("\nNo Motion Detected",i)
            behave.light_off() #Turn the light off
            skip_send = True #allows to skip sending same thing to the db each loop
            time.sleep(0.1)
        elif i==1:               #When output from motion sensor is HIGH
            print ("\nMotion Detected",i)
            behave.light_on()
            db.data_send_set(None, None, "Motion Detected!!", None, None)
            db.data_send_push(None, None, "Date and time a motion was detected", None, None)
            time.sleep(3)
            skip_send = False
        if stop():
            return
    
if __name__=="__main__":
    #testing the function
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        check_motion(lambda: False)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(0)
