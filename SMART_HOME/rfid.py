#!/usr/bin/env python
# getting the main GPIO libraly
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from subprocess import call


id = None

def read_rfid():
    #restarting the spi bus 
    call(['dtparam', 'spi=off'])
    call(['dtparam', 'spi=on'])

    reader = SimpleMFRC522()
    try:
        id = reader.read_id()
        time.sleep(1)
        print(id)
#    except KeyboardInterrupt:
#        GPIO.cleanup()
#        exit(0)
        return id 
    except:
        return 0
if __name__ == "__main__":
    read_rfid()
    #GPIO.cleanup()
