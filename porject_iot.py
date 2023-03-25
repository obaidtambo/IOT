from machine import Pin, ADC, PWM
from time
import urequests
import network

import json

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'HLKGWQGNIVAIWBWR' 


ssid='Obaid'
password='obaid1717'

# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 

groove = ADC(Pin(15))
groove.atten(ADC.ATTN_11DB)       #Full range: 3.3v

lop = Pin(5, Pin.IN)
lon= Pin(18, Pin.IN)
ecg=ADC(Pin(2))
ecg.atten(ADC.ATTN_11DB)
file = open("iot_data1.txt", "w")
print("file Created")


while True:
    
  for i in range(512)  
      if lop==1 or lon==1:
          print("!-")
      else:    
          groove_val = groove.read()
          ecg_val = ecg.read()
          # print(ecg_val)
          #file = open("iot_data1.csv", "a")
          data={'field1':time.localtime(), 'field2':groove_val, 'field3':ecg_val}
          #request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = data, headers = HTTP_HEADERS )  
          #request.close()  
     #   data=str(time.localtime()))+", "+ groove_val+ ", "+ ecg_val
          file.write("\n" + json.dump(data))
      
          print("GSR: ",groove_val, "ECG: ", ecg_val)
      sleep(0.0078125)
      print(" ********** 512 values completed *********")



