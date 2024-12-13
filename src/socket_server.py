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

	def send_response(self, connection, is_ok: bool):
		if is_ok == True:
			message = {'key': 'RESPONSE', 'value': 'ok'}
		else:
			message = {'key': 'RESPONSE', 'value': 'bad'}
		data = json.dumps(message).encode()
		print(json.dumps(message).encode())
		try:
			connection.send(data)
		except Exception as error:
			print('Failed to send ok response to client', connection, error)

	def run(self, number_of_connections):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.__hostname, self.__port))
		server.listen(number_of_connections)
		initialize_db()
		print_users_table()
		while True:
			try:
				connection, address = server.accept()
				print('Connected succesfully from', address)
			except Exception as error:
				print('error while accepting a connection!', error)
			try:
				start_new_thread(client_thread(self, connection), (connection, ))
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


def process_data(server: Server, connection, data: dict):
	match data['key']:
		case 'CLOSECON':
			pass
		case 'REGUSER':
			server.send_response(connection, register_user(data['login'], data['password'], data['gender'], data['bio']))
		case 'LOGUSER':
			server.send_response(connection, sign_user(data['login'], data['password']))


def client_thread(server, connection):
	flag_connection_closed = False
	while not flag_connection_closed:
		data = connection.recv(1024)
		message = data.decode()
		deserialised = json.loads(message)
		print('Got message from client: ', deserialised)
		process_data(server, connection, deserialised)
	connection.close()


server = Server(HOSTNAME, PORT)
server.run(5)
