#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('437-388-2002')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")
    text2 = reader.read()
    print (text2)
finally:
    GPIO.cleanup()
