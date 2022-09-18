#Blinks a led continuesly, provide GPIO pin number as an argument
import sys
import time
import RPi.GPIO as GPIO


if len(sys.argv) < 2:
    print("Provide a GPIO pin number based on the BOARD mode")
    exit(0)
pin=int(sys.argv[1])
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
           
    while 1:
        GPIO.output(pin, GPIO.HIGH)
#        time.sleep(0.05)
#        GPIO.output(pin, GPIO.LOW)
#        time.sleep(0.95)
except KeyboardInterrupt:
    GPIO.cleanup()
    quit()
