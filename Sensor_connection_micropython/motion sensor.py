# from machine import Pin
# from time import sleep
# motion = False
# def handle_interrupt(pin):
#   global motion
#   motion = True
#   global interrupt_pin
#   interrupt_pin = pin
# led = Pin(4, Pin.OUT)
# pir = Pin(13, Pin.IN)
# pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
# while True:
#   if motion:
#     print('MOTION DETECTED')
#     led.value(1)
#     sleep(500)
#     led.value(0)
#     print('MOTION STOPPED')
#     motion = False
    
    
from machine import Pin
from time import sleep
motion = False
def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin
led = Pin(2, Pin.OUT)
pir = Pin(13, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
while True:
  if motion:
    print('MOTION DETECTED')
    led.value(1)
    sleep(5)
    led.value(0)
    print('MOTION STOPPED')
    sleep(10)
    motion = False    