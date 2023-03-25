from machine import Pin, ADC, PWM
from time import sleep

#groove = ADC(Pin(15))
#groove.atten(ADC.ATTN_11DB)       #Full range: 3.3v

lop = Pin(5, Pin.IN)
lon= Pin(18, Pin.IN)
ecg=ADC(Pin(19))
ecg.atten(ADC.ATTN_11DB)


while True:
  #groove_val = groove.read()
  ecg_val = ecg.read()
  print(ecg_val)
  #print("GSR: ",groove_val, "ECG: ", ecg_val)
  sleep(0.1)

