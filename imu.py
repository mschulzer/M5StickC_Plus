import utime
from machine import I2C, Pin
from mpu6886 import MPU6886

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.temperature)

    utime.sleep_ms(1000)
