from sense_hat import SenseHat
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message
import configparser
from sensor import Sensor


config = configparser.ConfigParser()
config.read('config.ini')
conn = config['iot_conn']['conn']

sensor = Sensor(conn)
sensor.connect()
sensor.setData('temperature')

i = 0
while i <= 10:
    sensor.showMessage()
    sensor.sendMessage()
    time.sleep(10)
    i += 1