import RPi.GPIO as GPIO
import time
import sys
import user_db

db = user_db.User_db("somemail@mail.com", "Admin1234#")

#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
#lGPIO.setup(2, GPIO.OUT)         #LED output pin
motionInPin = 5
motionOutPin = 13
skip_send = None


def check_motion_blink():
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
        GPIO.setup(motionOutPin, GPIO.OUT)         #LED output pin
        i=GPIO.input(motionInPin)
        if i==0:                 #When output from motion sensor is LOW
            if not skip_send:#skip this if skip_send is true
                db.data_send_set(None, None, "No Motion Detected", None, None)
                print ("\n\nNo Motion Detected",i)
            GPIO.output(motionOutPin, 1)  #Turn OFF LED
            skip_send = True #allows to skip sending same thing to the db each loop
            time.sleep(0.1)
            #GPIO.cleanup()
        elif i==1:               #When output from motion sensor is HIGH
            print ("\n\nMotion Detected",i)
            GPIO.output(motionOutPin, 0)  #Turn ON LED
            db.data_send_set(None, None, "Motion Detected!!", None, None)
            time.sleep(3)
            skip_send = False
            #GPIO.cleanup()




        #GPIO.cleanup()
def check_motion(stop):
    skip_send = None
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
        GPIO.setup(motionOutPin, GPIO.OUT)         #LED output pin
        i=GPIO.input(motionInPin)
        if i==0:                 #When output from motion sensor is LOW
            if not skip_send:#skip this if skip_send is true
                db.data_send_set(None, None, "No Motion Detected", None, None)
                print ("\nNo Motion Detected",i)
            GPIO.output(motionOutPin, 1)  #Turn OFF LED
            skip_send = True #allows to skip sending same thing to the db each loop
            time.sleep(0.1)
        elif i==1:               #When output from motion sensor is HIGH
            print ("\nMotion Detected",i)
            GPIO.output(motionOutPin, 0)  #Turn ON LED
            db.data_send_set(None, None, "Motion Detected!!", None, None)
            db.data_send_push(None, None, "Date and time a motion was detected", None, None)
            time.sleep(3)
            skip_send = False
        if stop():
            return
    
if __name__=="__main__":
#    check_motion_blink()
    check_motion(lambda: False)
