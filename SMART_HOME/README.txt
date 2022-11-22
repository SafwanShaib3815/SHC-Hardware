
*************************************** firebase related notes **************************************
install the following libraries:

`sudo pip3 install requests==1.1.0`
`sudo pip3 install python-firebase`
#####################################################################################################################################################################

*************************************** SPI bus conflict **************************************

This project has two devices that use the SPI bus with different configration(RFID and MQ2 sensors), to allow the bus to work again with the rfid sensor resetting the bus is required using the 'dtparam' command as a root, for that install the needed library using the following command:

`sudo apt-get install libraspberry-bin` 
#####################################################################################################################################################################

*************************************** Setting up python for RFID **************************************
Upgrading:
`sudo apt-get update`
`sudo apt-get upgrade`

installing necessary libraries:
`sudo apt-get install python3-dev python3-pip

To install spi related libraries:
 `sudo pip3 install spidev`

Two ways to install the MFRC522:
1)
-move to the directory where you wanna download the project from github
-clone the library project from github using the command `git clone https://github.com/mxgxw/MFRC522-python.git`

2)
`sudo pip3 install mfrc522`

#####################################################################################################################################################################

