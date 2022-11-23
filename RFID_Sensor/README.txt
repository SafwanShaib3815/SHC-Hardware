
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

for the tutorial on how to use the MFRC522 reader check websit:

https://pimylifeup.com/raspberry-pi-rfid-rc522/

