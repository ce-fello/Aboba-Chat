import socket
import json
from constants import *


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    def close_connection(self):
        self.client.close()

    def transfer_data(self, message: dict):
        try:
            data = json.dumps(message).encode() 
            self.client.send(data)
            print('Sent data to server')
        except Exception as error:
            print('Error while sending data to server!', error)
        try:
            data = self.client.recv(1024)
            print('Got data from server:', data.decode())
        except Exception as error:
            print('Error while recieving data from server!', error)

    def start_connection(self, hostname_to_connect, port):
        try:
            self.client.connect((hostname_to_connect, port))   
            print('Connected to', hostname_to_connect, port)
        except Exception as error:
            print('Error while connecting to server!', error)
