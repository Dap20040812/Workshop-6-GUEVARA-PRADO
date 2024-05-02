import thingspeak
import time
import random
import smbus
import RPi.GPIO as GPIO

API_KEY = 'XDT3Z7N5FSEP0YMI'
address = 0x04


#API_KEY = 'N1DUE51PRFXCVSDO'
canal = thingspeak.Channel(2524802, API_KEY)

def recive_data():
    bus = smbus.SMBus(1)
    temperature = bus.read_byte(address)
    voltage = temperature * (5.0 / 255)
    temperatureC = voltage
    #temperature_float= float.fromhex(''.join(format(byte,'02x') for byte in temperature))
    return (temperature*500) / 1023

while True:
    GPIO.setmode(GPIO.BOARD)
    pin_led = 11
    GPIO.setup(pin_led, GPIO.OUT)
    try:     
        data = recive_data()
        if data >= 30:
           GPIO.output(pin_led, GPIO.HIGH)
        else:
           GPIO.output(pin_led, GPIO.LOW)
        print("Dato: {}".format(data))
        canal.update({1: data})
        time.sleep(1)
    except IOError as e:
        print(e)
        time.sleep(1)
    finally:
        GPIO.cleanup()    
    
    #valor = random.randint(0,100)
    #
    #print(valor)
    #time.sleep(1)
