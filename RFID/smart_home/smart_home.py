# getting the main GPIO libraly
import RPi.GPIO as GPIO 
import time # getting the time libraly
from threading import Thread 

#from mfrc522 import SimpleMFRC522

#my imports
import rfid #script to read the rfid tags
import behave #responce actions  script
import blink #linking led script
import smoke_check 
import temp_humid  
#import smart_door
import motionsensor
#import temp_humid #temperature and humidity sensor script 

pinsOut = [6,13,19,26] #creating a list (array) with the number of GPIO's that we use 
led_out = 23
#threads' stop variable
#stop_blink_thread=False
stop_temp_thread=False
stop_smoke_thread=False
stop_door_thread=False
stop_motion_thread=False

GPIO.setwarnings(False)

smoke_thread = Thread(target=smoke_check.check_smoke, args=(lambda: stop_smoke_thread,))
temp_thread = Thread(target=temp_humid.watch_temp, args=(lambda: stop_temp_thread,))
#door_thread = Thread(target=../smart_door.check_door, args=(lambda: stop_door_thread,))
motion_thread = Thread(target=motionsensor.check_motion, args=(lambda : stop_motion_thread, ))#instenciating a thread for the blink task
blink_thread = Thread(target=blink.blink_led, args=(led_out, lambda : stop_blink_thread, ))#instenciating a thread for the blink task

smoke_thread.start()
time.sleep(7)
#blink_thread.start()
time.sleep(2)
temp_thread.start()
time.sleep(3)
#door_thread.start()
#time.sleep(3)
motion_thread.start()
time.sleep(3)
import test

if KeyboardInterrupt:
    GPIO.cleanup()
#GPIO.cleanup()
