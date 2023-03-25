from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  sensorValue = pot.read()
  voltage = sensorValue * (5.0 / 1024.0);
  print(voltage)
  sleep(0.1)