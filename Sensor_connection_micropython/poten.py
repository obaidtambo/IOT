from machine import Pin, ADC, PWM
from time import sleep

pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)
pwm = PWM(Pin(2, Pin.OUT),1000)

while True:
  pot_value = pot.read()
  pwm.duty(pot_value)
  print(pot_value)
  pwm.duty(pot_value)

  
  
  sleep(0.5)
