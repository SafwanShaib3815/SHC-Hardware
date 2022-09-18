# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_am2320

# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
#i2c = board.I2C()  # uses board.SCL and board.SDA (another way to initialize the i2c bus)
am = adafruit_am2320.AM2320(i2c)

while True:
    time.sleep(1)
    print("Temperature: ", am.temperature)
    time.sleep(1)
    print("Humidity: ", am.relative_humidity)
