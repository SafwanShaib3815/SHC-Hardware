#Blinks a led continuesly
import sys
import time
import RPi.GPIO as GPIO


def blink_led(stop):
    
    led_out = 23
    try:
        while 1:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(led_out, GPIO.OUT)
            GPIO.output(led_out, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.setup(led_out, GPIO.OUT)
            GPIO.output(led_out, GPIO.LOW)
            time.sleep(0.5)
            if stop():
                return
    except KeyboardInterrupt:
        GPIO.cleanup()
        time.sleep(1) #allow it time to cleanup pins before exiting
        exit(0)
        return 

