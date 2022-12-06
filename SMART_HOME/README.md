----------------------------------------
Database related notes 
----------------------------------------
install the following libraries:

`sudo pip3 install pyrebase`
`sudo pip3 install self`
#####################################################################################################################################################################

----------------------------------------
SPI bus conflict 
----------------------------------------
This project has two devices that use the SPI bus with different configration(RFID and MQ2 sensors), to allow the bus to work again with the rfid sensor resetting the bus is required using the 'dtparam' command as a root, for that install the needed library using the following command:

`sudo apt-get install libraspberry-bin` 
#####################################################################################################################################################################

----------------------------------------
Setting up python for RFID 
----------------------------------------
follow the following(mandatory):
1) Enable the spi bus on rpi using `sudo raspi-config` command > interfaces > spi > yes

2) Two ways to install the MFRC522:
FIRST:
`sudo pip3 install mfrc522`

SECOND:
-move to the directory where you wanna download the project from github
-clone the library project from github using the command `git clone https://github.com/mxgxw/MFRC522-python.git`

for the tutorial on how to use the MFRC522 reader check websit:

https://pimylifeup.com/raspberry-pi-rfid-rc522/

You may need to run follwing commands(Optional):
`sudo apt-get update`
`sudo apt-get upgrade`

installing necessary libraries:
`sudo apt-get install python3-dev python3-pip

To install spi related libraries:
 `sudo pip3 install spidev`
#####################################################################################################################################################################

----------------------------------------
AM2320 Temperature and Humidity sensor  |
----------------------------------------


for the board module to be imported, first you have to install it using one of the following commands until it works (exclude the backticks `):

` sudo pip install board `
` sudo pip3 install board `
` sudo pip3 install adafruit-blinka ` 
********************************************************************************************************************
for the busio library to be imported you can run command number 3 above

********************************************************************************************************************
for the adafruit-AM2320 to be imported install the dependency using following command:

` sudo pip3 install adafruit-circuitpython-am2320 `

see website: 
https://pypi.org/project/adafruit-circuitpython-am2320

********************************************************************************************************************
python simple test code:
https://learn.adafruit.com/adafruit-am2320-temperature-humidity-i2c-sensor/python-circuitpython
********************************************************************************************************************
arduino test code:
https://learn.adafruit.com/adafruit-am2320-temperature-humidity-i2c-sensor/arduino-usage
#####################################################################################################################################################################

----------------------------------------
MQ2 Gas Sensor
----------------------------------------
check below repository:
https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx/

