#!/usr/bin/env python3

# AM2320 PINOUT to Raspberry Pi 4B GPIO pins 
# ╔═════════╗
# ║╬╬╬╬╬╬╬╬╬║
# ║╬╬╬╬╬╬╬╬╬║
# ║         ║
# ║ 1 2 3 4 ║
# ╚═╪═╪═╪═╪═╝
#   │ │ │ │                    | Raspberry Pi pins
#   │ │ │ └─ SCL = GPIO 3(SCL) | pin #5
#   │ │ └─ GND = Ground        | pin #25
#   │ └─  SDA = GPIO 2(SDA)    | pin #3
#   └─ VDD = 3v3 power         | pin #1

# pip3 install adafruit-circuitpython-am2320
# pip3 install adafruit-blinka
# Read more at https://learn.adafruit.com/adafruit-am2320-temperature-humidity-i2c-sensor        

import time
import board 
import busio
import adafruit_am2320
from signal import signal, SIGINT
from sys import exit

def watch_temp_humid():
    #i2c = busio.I2C(board.SCL, board.SDA) OR :
    i2c = board.I2C() # create the I2C shared bus
    sensor = adafruit_am2320.AM2320(i2c) 
    print('Running. Press CTRL-C twice to exit.')
    while True:
        try:
            time.sleep(1)
            print("Temperature: ", sensor.temperature)
            time.sleep(1)
            print("Humidity: ", sensor.relative_humidity)
        except KeyboardInterrupt:
            exit(0)
        except:
            print("\r Trying again                                  ", end="")
            time.sleep(.5)

if __name__ == "__main__":
    watch_temp_humid()
