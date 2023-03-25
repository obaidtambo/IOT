from machine import Pin, I2C
from time import sleep
import dht

DHT=dht.DHT11(Pin(14))
DEFAULT_I2C_ADDR=0x27
i2c=I2C(scl=Pin(19),sda=Pin(13),freq=400000)
DHT.measure()
while True:
    #DHT.measure()
    temp=DHT.temperature()
    lcd.move_to(0,0)
    humd=DHT.humidity()
    lcd.move_to(0,1)
    sleep_ms(1000)
    
    
