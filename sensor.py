from sense_hat import SenseHat
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message
import configparser

class Sensor():
    def __init__(self, conn):
        self.conn = conn

    # create client
    def client(self):
        return self.client

    # connect to client
    def connect(self):
        self.client = IoTHubDeviceClient.create_from_connection_string(self.conn)
        self.client.connect()

    # connect to sensor
    def sensor(self):
        sensor = SenseHat()
        return sensor 
    
    # set data type to retreive
    def setData(self, dataType):
        self.sensorType = dataType

    # get data from sensor
    def getData(self):
        if self.sensorType == 'temperature':
            self.data = self.sensor().get_temperature()
        return self.data

    def showData(self):
        print(self.data)

    # compose message
    def message(self):
        msg = {}
        msg[f"{self.sensorType}"] = self.getData()
        json_msg = json.dumps(msg)
        return json_msg

    def showMessage(self):
        print(self.message())

    # send message using client
    def sendMessage(self):
        self.client.send_message(self.message())
