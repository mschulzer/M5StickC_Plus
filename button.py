from micropython import const
from ubutton import Button

_BUTTON_A_PIN = const(39)
_BUTTON_B_PIN = const(38)
_BUTTON_C_PIN = const(37)

m5button = Button()
buttonA = m5button.register(_BUTTON_A_PIN)
buttonB = m5button.register(_BUTTON_B_PIN)
buttonC = m5button.register(_BUTTON_C_PIN) # M5-knappen!

while True:
  if buttonC.wasPressed():
    print("Hello, World!")
