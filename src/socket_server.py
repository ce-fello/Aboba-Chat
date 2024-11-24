import socket
from _thread import *


def client_thread(connection):
	"""
	Function for processing the behavior of each client
	:param connection: tcp connection 
	:returns: void
	"""
	data = connection.recv(1024)
	message = data.decode()
	print('Got message from client', message)
	message_to_client = '200 OK'
	data_to_client = message_to_client.encode()
	connection.send(data_to_client)


HOSTNAME = 'localhost'
PORT = 3030

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = {}
index = 0

server.bind((HOSTNAME, PORT))
server.listen(5)

while True:
	try:
		connection, address = server.accept()
		print('Connected succesfully from', address)
	except Exception as error:
		print('error while accepting a connection\n', error)

	try:
		start_new_thread(client_thread, (connection, ))
	except Exception as error:
		print('error while creating new thread', error)

	try:
		if str(address) in connections.values():
			connections[index] = str(address)
			index += 1
			print('Succesfully added to connections list')
		else:
			print('Address already in connections')
	except Exception as error:
		print('error while adding to connections list\n', error)

	print(connections)
