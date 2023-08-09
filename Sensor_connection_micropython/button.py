import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led = Pin(2, Pin.OUT)
try:
    while True:
        if not button.value():
            print('Button pressed!')
            led.value(1)
            
        else:
            led.value(0)
except:
    pass
            