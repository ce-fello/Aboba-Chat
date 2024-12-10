import socket
from constants import *


class Client:
    def __init__(self):
        pass

    def close_connection(self, client):
        client.close()

    def transfer_data(self, client):
        while True:
            message = input()
            try:
                data = message.encode()
                client.send(data)
                if message == 'CLOSECON':
                    self.close_connection(client)
                print('Sent data to server')
            except Exception as error:
                print('Error while sending data to server!', error)
            try:
                data = client.recv(1024)
                if not data:
                    break
                print('Got data from server:', data.decode())
            except Exception as error:
                print('Error while recieving data from server!', error)

    def start_connection(self, hostname_to_connect, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        try:
            client.connect((hostname_to_connect, port))   
            print('Connected to', hostname_to_connect, port)
        except Exception as error:
            print('Error while connecting to server!', error)
        self.transfer_data(client)

client = Client()
client.start_connection(HOSTNAME, PORT)
