#Blinks a led continuesly
import sys
import time
import RPi.GPIO as GPIO


def blink_led(pin, stop):
    #if len(sys.argv) < 2:
    if pin == None: 
        print("Please provide pin number based on BCM mode")
        exit(0)
    #pin=int(sys.argv[1])
    pin=int(pin)
    try:
        while 1:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)
            if stop():
                return
    except KeyboardInterrupt:
        GPIO.cleanup()
        time.sleep(1) #allow it time to cleanup pins before exiting
        exit(0)
        return 
if __name__ == "__main__":
    if len(sys.argv) <   2: 
        print("Please provide pin number based on BCM mode")
        exit(0)
    blink_led(sys.argv[1], lambda: False) 
    #GPIO.cleanup()
