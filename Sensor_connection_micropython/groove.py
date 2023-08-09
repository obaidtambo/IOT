from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
pot.width(ADC.WIDTH_10BIT)

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.5)