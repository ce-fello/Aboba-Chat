import socket
import json
from _thread import *
from constants import *
from db_api import *


class Server:
	def __init__(self, hostname, port):
		self.__hostname = hostname
		self.__port = port
		self.__connections = {}
		self.__last_connection_index = 0

	def send_message_to_client():
		pass

	def run(self, number_of_connections):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.__hostname, self.__port))
		server.listen(number_of_connections)
		initialize_db()
		while True:
			try:
				connection, address = server.accept()
				print('Connected succesfully from', address)
			except Exception as error:
				print('error while accepting a connection!', error)
			try:
				start_new_thread(client_thread, (connection, ))
			except Exception as error:
				print('error while creating new thread!', error)
			try:
				if str(address) not in self.__connections.values():
					self.__connections[self.__last_connection_index] = str(address)
					self.__last_connection_index += 1
					print('Succesfully added to connections list')
				else:
					print('Address already in connections')
			except Exception as error:
				print('error while adding to connections list!', error)
			print(self.__connections)


def process_data(data: dict):
	match data['key']:
		case 'CLOSECON':
			pass
		case 'REGUSER':
			if register_user(data['login'], data['password'], data['gender'], data['bio'])
		case 'LOGUSER':
			sign_user(data['login'], data['password'])


def client_thread(connection):
	flag_connection_closed = False
	while not flag_connection_closed:
		data = connection.recv(1024)
		message = data.decode()
		deserialised = json.loads(message)
		print('Got message from client: ', deserialised)
		process_data(deserialised)
		message_to_client = '200 OK'
		data_to_client = message_to_client.encode()
		connection.send(data_to_client)
	connection.close()


server = Server(HOSTNAME, PORT)
LAST_ID = get_last_id()
server.run(5)
