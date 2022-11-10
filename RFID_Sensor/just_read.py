#!/usr/bin/env python
# getting the main GPIO libraly
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
    print ("waiting a card...")
    id, text = reader.read()
    print(id)
    print(text)
except KeyboardInterrupt:
    exit(0)

GPIO.cleanup()
