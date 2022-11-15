import machine
import st7789
import axp192
import vga1_8x16 as font

i2c = machine.I2C(0, sda=machine.Pin(21), scl=machine.Pin(22), freq=400000)
pmu = axp192.AXP192(i2c, board=axp192.M5StickCPlus)

spi = machine.SPI(2, baudrate=20000000, polarity=1, sck=machine.Pin(13, machine.Pin.OUT), miso=machine.Pin(4, machine.Pin.IN), mosi=machine.Pin(15, machine.Pin.OUT))
display = st7789.ST7789(spi, 135, 240, rotation=3, reset=machine.Pin(18, machine.Pin.OUT), dc=machine.Pin(23, machine.Pin.OUT), cs=machine.Pin(5, machine.Pin.OUT))

display.init()

display.fill(st7789.WHITE)
display.text(font, "Hello, World!", 50, 80, st7789.BLACK, st7789.WHITE)

spi.deinit()
