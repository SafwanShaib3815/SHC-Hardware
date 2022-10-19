import RPi.GPIO as GPIO
import time
import user_db

#initializing the database user
db = user_db.User_db("somemail@mail.com", "Admin1234#")



#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
#lGPIO.setup(2, GPIO.OUT)         #LED output pin
motionInPin = 5
motionOutPin = 13
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motionInPin, GPIO.IN)         #Read output from PIR motion sensor
    GPIO.setup(motionOutPin, GPIO.OUT)         #LED output pin
    i=GPIO.input(motionInPin)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        GPIO.output(motionOutPin, 1)  #Turn OFF LED
        time.sleep(0.1)
        GPIO.cleanup()
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        GPIO.output(motionOutPin, 0)  #Turn ON LED
        db.data_send(None, None, "Motion Detected", None, None)
        time.sleep(3)
        GPIO.cleanup()
    GPIO.cleanup()
