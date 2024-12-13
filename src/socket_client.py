import socket
import json
from constants import *


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    def close_connection(self):
        self.client.close()

    def get_data(self):
        try:
            message = self.client.recv(1024)
            return json.loads(message.decode())
        except Exception as error:
            print('Error while recieving data from server!', error)

    def get_response(self) -> bool:
        try:
            message = self.client.recv(1024)
            data = json.loads(message.decode())
            print('Got data from server:', data)
            if data['value'] == 'ok':
                return True
        except Exception as error:
            print('Error while recieving data from server!', error)
        return False
    
    def transfer_data(self, message: dict):
        try:
            data = json.dumps(message).encode() 
            self.client.send(data)
            print('Sent data to server', data)
        except Exception as error:
            print('Error while sending data to server!', error)

    def start_connection(self, hostname_to_connect, port):
        try:
            self.client.connect((hostname_to_connect, port))   
            print('Connected to', hostname_to_connect, port)
        except Exception as error:
            print('Error while connecting to server!', error)
