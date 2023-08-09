from machine import Pin, ADC, PWM
import time


groove = ADC(Pin(15))
ecg=ADC(Pin(2))
groove.atten(ADC.ATTN_11DB)       #Full range: 3.3v

lop = Pin(5, Pin.IN)
lon= Pin(18, Pin.IN)
#ecg=ADC(Pin(4))
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
          data='field1: '+ str(time.localtime()) +' field2: '+str(groove_val)+ ' field3: '+str(ecg_val)
          #request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = data, headers = HTTP_HEADERS )  
          #request.close()  
     #   data=str(time.localtime()))+", "+ groove_val+ ", "+ ecg_val
          file.write("\n" + data)
      
          print("GSR: ",groove_val, "ECG: ", ecg_val)
      time.sleep(0.0078125)
    print(" ********** 512 values completed *********")


