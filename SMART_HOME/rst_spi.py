import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode (GPIO.BCM)

#resetting the rfid module
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(25, GPIO.LOW)
#resetting the SPI bus
call(['dtparam', 'spi=off'])
call(['dtparam', 'spi=on'])

GPIO.cleanup()
