import socket


HOSTNAME = 'localhost'
PORT = 3030

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    client.connect((HOSTNAME, PORT))          
    print('Connected to', HOSTNAME, PORT)
except Exception as error:
    print('error while connecting to server\n', error)

while True:
    text = input()
    try:
        client.send(text.encode())
        print('Sent to server')
    except Exception as error:
        print('error while sending data to server\n', error)
    try:
        data = client.recv(1024)
        print('Got from server')
        if not data:
            break
        print(data.decode())
    except Exception as error:
        print('error while getting info from server', error)
