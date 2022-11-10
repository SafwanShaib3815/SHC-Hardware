#!/usr/bin/env python
# getting the main GPIO libraly
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read_rfid():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        print(id)
        print(text)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(0)
    return id 
if __name__ == "__main__":
    read_rfid()
    GPIO.cleanup()

