import RPi.GPIO as GPIO
import time

relay_pin1 = 6 #Abdulrahman
relay_pin2 = 13 #Nkeiru
relay_pin3 = 19 #safwan
relay_pin4 = 26 #tanush

indicator = 23 #indicator

GPIO.setmode(GPIO.BCM) #pin numbers are based on their order in the board
#/////////////////////////// SAFWAN'S ACTIONS /////////////////// 

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
        #GPIO.cleanup()
        return
            
   
#/////////////////////// TANUSH'S ACTIONS ///////////////////////// 

def ac_on():
    try:
        GPIO.setwarnings(False)
        GPIO.setup(relay_pin4, GPIO.OUT) #Tanush's pin set to out
        GPIO.setup(indicator, GPIO.OUT) #indicator pin set to out
        GPIO.output(indicator, GPIO.HIGH) #turn indicator led ON
        GPIO.output(relay_pin4, GPIO.LOW) #send LOW to Tanush's pin to activate the relay
        time.sleep(2)
        GPIO.output(indicator, GPIO.LOW) #turn indicator led OFF
        GPIO.output(relay_pin4, GPIO.HIGH) #send HIGH to Tanush's pin to deactivate the relay
    except KeyboardInterrupt:
        exit(0)
        #GPIO.cleanup()


def main():
    #uncomment the functions you want to test, not advised 
    open_door()
    time.sleep(1)
    ac_on()

if __name__ == "__main__":
    main()

