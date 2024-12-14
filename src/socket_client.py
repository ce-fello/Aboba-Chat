import socket
import json
from constants import *


class Client:
    """Class that represents Client"""
    def __init__(self):
        """Constructor method"""
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    """
    :param client: socket of connection
    :type client: socket
    """

    def close_connection(self):
        """
        Method that closes connection with server.
        :returns: closes connection.
        :rtype: void
        """
        self.client.close()

    def get_data(self):
        """
        Method that gets data from server.
        
        :returns: data from server.
        :rtype: any
        """
        try:
            message = self.client.recv(1024)
            return json.loads(message.decode())
        except Exception as error:
            print('Error while recieving data from server!', error)

    def get_response(self) -> bool:
        """
        Method that gets data from server and returns True if OK and False otherwise.
        
        :returns: True or False.
        :rtype: bool
        """
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
        """
        Method that sends data to server.

        :param message: message that we send to server.
        :type message: dict
        :returns: sends data to server.
        :rtype: void
        """
        try:
            data = json.dumps(message).encode() 
            self.client.send(data)
            print('Sent data to server', data)
        except Exception as error:
            print('Error while sending data to server!', error)

    def start_connection(self, hostname_to_connect, port):
        """
        Method that starts connection with server.

        :param hostname_to_connect: hostname to whon we want to connect.
        :type hostname_to_connect: str
        :param port: port of host to whom we want to connect.
        :type port: int
        :returns: connects to hostname on port.
        :rtype: void
        """
        try:
            self.client.connect((hostname_to_connect, port))   
            print('Connected to', hostname_to_connect, port)
        except Exception as error:
            print('Error while connecting to server!', error)
