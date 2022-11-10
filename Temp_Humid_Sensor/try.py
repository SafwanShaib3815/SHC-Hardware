import board
import adafruit_am2320
import time
i2c = board.I2C()
sensor = adafruit_am2320.AM2320(i2c)
time.sleep(1)
print('Humidity: {0}%'.format(sensor.relative_humidity))
time.sleep(1)
print('Temperature: {0}C'.format(sensor.temperature))
