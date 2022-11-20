import machine
from micropython import const

_SPEAKER_PIN  = const(25)

class Speaker:
  def __init__(self, pin=25, volume=5):
    self.pwm = machine.PWM(machine.Pin(pin), freq = 1, duty = 0, timer = 2)
    self._timer = None
    self._volume = volume
    self._beat_time = 500
    self._timer = machine.Timer(8)
    self._timer.init(period=10, mode=self._timer.ONE_SHOT, callback=self._timeout_cb)   

  def _timeout_cb(self, timer):
    self.pwm.duty(0)
    time.sleep_ms(1)
    self.pwm.freq(1)
    self._timer.stop()

  def tone(self, freq=1800, duration=200, timer=True, volume=None):
    if volume == None:
      self.pwm.init(freq=freq, duty=self._volume)
    else:
      self.pwm.init(freq=freq, duty=volume)
    duration = max(0, duration)
    if timer:
      if self._timer.isrunning():
        self._timer.period(duration)
      else:
        self._timer.init(period=duration, mode=self._timer.ONE_SHOT, callback=self._timeout_cb)   
      time.sleep_ms(duration-15)
    else:
      time.sleep_ms(duration)
      self.pwm.duty(0)
      time.sleep_ms(1)
      self.pwm.freq(1)
    

  def sing(self, freq=1800, beat=1, end=True, volume=None):
    self.tone(freq, int(beat*self._beat_time), end, volume)
  
  def set_beat(self, value=120):
    self._beat_time = int(60000 / value)

  def volume(self, val):
    self._volume = val

    
speaker = Speaker()
