import socket
import sqlite3
from _thread import *
from constants import HOSTNAME, PORT


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


db_connection = sqlite3.connect('my_database.db')
cursor = db_connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL
)
''')

db_connection.commit()
db_connection.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = {}
index = 0

server.bind((HOSTNAME, PORT))
server.listen(5)

while True:
	try:
		db_connection, address = server.accept()
		print('Connected succesfully from', address)
	except Exception as error:
		print('error while accepting a connection\n', error)

	try:
		start_new_thread(client_thread, (db_connection, ))
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
