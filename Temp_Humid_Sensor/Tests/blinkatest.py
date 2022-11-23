import board
import digitalio
import busio

print("Hello blinka!")

#Try to get a digital input

pin = digitalio.DigitalInOut(board.D4)
print("Digital Ok!")

#try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

#Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("\nDigital I/O, I2C and SPI all worked !!\n")
