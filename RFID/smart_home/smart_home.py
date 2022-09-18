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
import smart_door
#import temp_humid #temperature and humidity sensor script 

pinsOut = [6,13,19,26] #creating a list (array) with the number of GPIO's that we use 
led_out = 23
#threads' stop variable
stop_blink_thread=False
stop_temp_thread=False
stop_smoke_thread=False
stop_door_thread=False

GPIO.setwarnings(False)

temp_thread = Thread(target=temp_humid.watch_temp, args=(lambda: stop_temp_thread,))
smoke_thread = Thread(target=smoke_check.check_smoke, args=(lambda: stop_smoke_thread))
door_thread = Thread(target=smart_door.check_door, args=(lambda: stop_door_thread))
blink_thread = Thread(target=blink.blink_led, args=(led_out, lambda : stop_blink_thread, ))#instenciating a thread for the blink task

blink_thread.start()
temp_thread.start()
smoke_thread.start()
door_thread.start()
    

if KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
