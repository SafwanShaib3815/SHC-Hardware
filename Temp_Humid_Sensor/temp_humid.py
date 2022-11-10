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
import sys
import pyrebase
from signal import signal, SIGINT
from threading import Thread
import user_db

#initializing realtime database
db = user_db.User_db("somemail@mail.com", "Admin1234#") #use this function to post data to db db.data_send("temp", "humid", "motion", "smoke", "rfid white")



led_out=23
stop_blink_thread = False
#my imports
import blink

#from sys import exit


def watch_temp_blink():
    #i2c = busio.I2C(board.SCL, board.SDA) OR :
    i2c = board.I2C() # create the I2C shared bus
    sensor = adafruit_am2320.AM2320(i2c) 
    blink_thread = Thread(target=blink.blink_led, args=(led_out, lambda: stop_blink_thread,)) #a thread to start the blink task
    blink_thread.start()

#        db.data_send(sensor.temperature, sensor.relative_humidity, None, None, None)
    while True:
        try:
            time.sleep(2)
            temp=format(sensor.temperature)
            time.sleep(0.25)
            humid=format(sensor.relative_humidity)
            print("Temperature: ",temp,       end='\t\t')
            #sys.stdout.write("\rTemperature: %d" % sensor.temperature)
            print("Humidity:",humid, "%")
            #sys.stdout.write("\t\tHumidity: %d" % sensor.relative_humidity)
            db.data_send_set(temp, humid , None, None, None)
            #print(type(typ))
        except KeyboardInterrupt:
            quit()
        #except:
            #print("\r Trying again                                  ", end="")
            #time.sleep(.5)

    return
def watch_temp(stop):
    i2c = board.I2C() # create the I2C shared bus
    sensor = adafruit_am2320.AM2320(i2c) 
    print('Running. Press CTRL-C twice to exit.\n')

    while True:
        try:
            time.sleep(2)
            temp=format(sensor.temperature)
            time.sleep(0.25)
            humid=format(sensor.relative_humidity)
            print("Temperature: ",temp,       end='\t\t')
            #sys.stdout.write("\rTemperature: %d" % sensor.temperature)
            print("Humidity:",humid, "%")
            #sys.stdout.write("\t\tHumidity: %d" % sensor.relative_humidity)
            db.data_send_set(temp, humid , None, None, None)
        except KeyboardInterrupt:
            quit()
        except:
            print("\r Trying again                                  ", end="")
            time.sleep(.5)
        if stop():
            return

if __name__ == "__main__":
    watch_temp(lambda:False)

