import RPi.GPIO as GPIO
import time

relay_pin1 = 6 #Smoke
relay_pin2 = 13 #Motion
relay_pin3 = 19 #RFID
relay_pin4 = 26 #Temp_Humid

indicator = 23 #indicator

#/////////////////////////// DOOR ACTIONS /////////////////// 

def open_door():
   #open the door & turn on led
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin3, GPIO.OUT) #safwan's pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.HIGH) #turn indicator led ON
        GPIO.output(relay_pin3, GPIO.LOW) #send LOW to safwan's pin to activate the relay
        time.sleep(2)
        GPIO.output(indicator, GPIO.LOW) #turn indicator led OFF
        GPIO.output(relay_pin3, GPIO.HIGH) #send HIGH to safwan's pin to deactivate the relay
    except KeyboardInterrupt:
        exit(0)
            
   
#/////////////////////// AC ACTIONS ///////////////////////// 

def ac_on():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin4, GPIO.OUT) #AC pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.HIGH) #turn indicator led ON
        GPIO.output(relay_pin4, GPIO.LOW) #send LOW to the AC's pin to activate the relay
    except KeyboardInterrupt:
        exit(0)

def ac_off():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin4, GPIO.OUT) #AC pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.LOW) #turn indicator led OFF
        GPIO.output(relay_pin4, GPIO.HIGH) #send HIGH to the AC's pin to deactivate the relay
    except KeyboardInterrupt:
        exit(0)



#/////////////////////// AC ACTIONS ///////////////////////// 
def light_on():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin2, GPIO.OUT) #Light pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.HIGH) #turn indicator led ON
        GPIO.output(relay_pin2, GPIO.LOW) #send LOW to the Light's pin to activate the relay
    except KeyboardInterrupt:
        exit(0)



def light_off():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin2, GPIO.OUT) #Light pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.LOW) #turn indicator led OFF
        GPIO.output(relay_pin2,  GPIO.HIGH) #send HIGH to the Light's pin to deactivate the relay
    except KeyboardInterrupt:
        exit(0)

#/////////////////////// ALARM ACTIONS ///////////////////////// 
def alarm_on():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin1, GPIO.OUT) #Alarm pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.HIGH) #turn indicator led ON
        GPIO.output(relay_pin1, GPIO.LOW) #send LOW to the Alarm's pin to activate the relay
    except KeyboardInterrupt:
        exit(0)



def alarm_off():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin1, GPIO.OUT) #Light pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.LOW) #turn indicator led OFF
        GPIO.output(relay_pin1,  GPIO.HIGH) #send HIGH to the Alarms's pin to deactivate the relay
    except KeyboardInterrupt:
        exit(0)




def main():
    GPIO.setmode(GPIO.BCM) #pin numbers are based on their order in the board

    #uncomment the functions you want to test 

    #Door action tests
    print("Opening door")
    open_door()
    time.sleep(2)
    
    #AC action tests
    ac_on()
    print("\nAC is on now")
    time.sleep(4)
    ac_off()
    print("AC is off")
    time.sleep(2)
    
    #Light action tests
    light_on()
    print("\nLight is on")
    time.sleep(4)
    light_off()
    print("Light is off")
    time.sleep(2)
    
    #Alarma action tests
    alarm_on()
    print("\nAlarm is on")
    time.sleep(4)
    alarm_off()
    print("Alarm is off")




    GPIO.cleanup()

if __name__ == "__main__":
    main()

