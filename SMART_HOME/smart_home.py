# getting the main GPIO libraly
import RPi.GPIO as GPIO 
import time # getting the time libraly
from threading import Thread 

#from mfrc522 import SimpleMFRC522

#my imports
import rfid #script to read the rfid tags
import blink #linking led script
import smoke_check 
import smart_door
import motionsensor
import temp_humid #temperature and humidity sensor script 

#threads' stop variable
stop_blink_thread=False
stop_temp_thread=False
stop_smoke_thread=False
stop_door_thread=False
stop_motion_thread=False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #pin numbers are based on their order in the board


smoke_thread = Thread(target=smoke_check.check_smoke, args=(lambda: stop_smoke_thread,))
temp_thread = Thread(target=temp_humid.watch_temp, args=(lambda: stop_temp_thread,))
door_thread = Thread(target=smart_door.check_door, args=(lambda: stop_door_thread,))
motion_thread = Thread(target=motionsensor.check_motion, args=(lambda : stop_motion_thread, ))#instenciating a thread for the motion task
blink_thread = Thread(target=blink.blink_led, args=(lambda : stop_blink_thread, ))#instenciating a thread for the blink task

try:
    #blink
    blink_thread.start()
    
    #temperature
    temp_thread.start()
    
    #smoke
    smoke_thread.start()
   
    #Motion
    motion_thread.start()
    
    #RFID
    door_thread.start()
 
except KeyboardInterrupt:
    stop_blink_thread=True
    stop_temp_thread=True
    stop_smoke_thread=True
    stop_door_thread=True
    stop_motion_thread=True
    GPIO.cleanup()


