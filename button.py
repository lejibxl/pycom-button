import utime
from machine import Pin
import gc

class BUTTON:

  def __init__(self,pid='P12',longms=1000):
    self.longms = longms
    self.butms = utime.ticks_ms()
    self.ticks_sign = utime.ticks_diff(1, 2) # get the sign of ticks_diff, e.g. in init code.
    self.pin = Pin(pid, mode=Pin.IN, pull=Pin.PULL_UP)
    self.pin.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.press)

  def long(self):
      pass

  def short(self):
      print("short")
      pass

  def press(self,pin):
      #print("press :{}".format(pin))
      #print("time :{}".format((utime.ticks_diff(self.butms, utime.ticks_ms()) * self.ticks_sign)))
      if (utime.ticks_diff(self.butms, utime.ticks_ms()) * self.ticks_sign) > 300  :
            self.short()
            self.butms = utime.ticks_ms()
            gc.collect()

if __name__ == "__main__":
    #Switch
    pinON = BUTTON(pid='P4')
    #pinON.short = pin_handler_ON
    #pinON.long = pin_handler_long
    pinOFF = BUTTON(pid='P8')
    #pinOFF.short = pin_handler_OFF
    #pinOFF.long = pin_handler_long
