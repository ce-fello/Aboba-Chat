import socket
from socket_server import HOSTNAME, PORT


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    client.connect((HOSTNAME, PORT))          
    print('Connected to', HOSTNAME, PORT)
except Exception as error:
    print('Error while connecting to server\n', error)

while True:
    message = input()
    try:
        data = message.encode()
        client.send(data)
        print('Sent data to server')
    except Exception as error:
        print('Error while sending data to server\n', error)
        
    try:
        data = client.recv(1024)
        if not data:
            break
        print('Got data from server:', data.decode())
    except Exception as error:
        print('Error while recieving data from server', error)
