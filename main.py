import serial
import time
import schedule
import requests

def main_func():
    arduino = serial.Serial('com3', 9600)
    print('Connection established')
    arduino_data = arduino.readLine()
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split(" ")
    for item in list_values:
        payload = {'number': item}
        r = requests.post('', data=payload)
    
    list_values.clear()
    arduino.close()



list_values = []

schedule.every(3).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)
