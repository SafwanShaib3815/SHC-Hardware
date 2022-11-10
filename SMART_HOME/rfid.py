#!/usr/bin/env python
# getting the main GPIO libraly
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

rfidcs = 8
smkcs = 7
id = None
GPIO.setmode(GPIO.BCM)
GPIO.setup(rfidcs, GPIO.OUT)
GPIO.setup(smkcs, GPIO.OUT)

def read_rfid():
    reader = SimpleMFRC522()
    try:
        
        GPIO.output(rfidcs, True)
        GPIO.output(smkcs, True)
        GPIO.output(rfidcs, False)
        id, text = reader.read()
        time.sleep(1)
        print(id)
        print(text)
#    except KeyboardInterrupt:
#        GPIO.cleanup()
#        exit(0)
        return id 
    except:
        return 0
if __name__ == "__main__":
    read_rfid()
    #GPIO.cleanup()
