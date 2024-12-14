import json
import socket
from db_api import *
from _thread import *
from constants import *


class Server:
	"""Class representing a server"""
	def __init__(self, hostname, port):
		"""
		Constructor of class Server.

		:param hostname: name or ip address of host.
		:type: str
		:param port: number of port on which server is run.
		:type: int
		"""
		self.__hostname = hostname
		self.__port = port
		"""
		:param __hostname: name or ip address of host.
		:type: str
		:param __port: number of port on which server is run.
		:type: int
		"""

	def send_response(self, connection: socket, is_ok: bool):
		"""
		Sends status of processing the request to client.

		:param connection: the socket connection on what we send the data.
		:type connection: socket
		:param is_ok: param that define what we send.
		:param is_ok: bool
		:return: sends encoded json dictionary.
		:rtype: void
		"""
		if is_ok == True:
			message = {'key': 'RESPONSE', 'value': 'ok'}
		else:
			message = {'key': 'RESPONSE', 'value': 'bad'}
		data = json.dumps(message).encode()
		print(data)
		try:
			connection.send(data)
		except Exception as error:
			print('Failed to send ok response to client', connection, error)

	def send_message(self, connection, message: str):
		"""
		Function that sends message to socket.

		:param connection: socket to which we send message.
		:type connection: socket
		:param message: message that we send to socket.
		:type message: str
		:returns: sends data to socket.
		:rtype: void
		"""
		data = json.dumps(message).encode()
		print(data)
		try:
			connection.send(data)
		except Exception as error:
			print('Failed to send ok response to client', connection, error)


	def run(self, number_of_connections: int):
		"""
		Runs server main cycle and setup everything.

		:param number_of_connections: number of connections given to server to listen to.
		:type: int
		:returns: runs server and its main cycle in which all requests are processed.
		:rtype: void
		:raises OSError: [Errno 98] Adress already in use.
		"""
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.__hostname, self.__port))
		server.listen(number_of_connections)
		initialize_db()
		print_users_table()
		print_chats_table()
		print(get_id_by_login('billyh'))
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
			print(self.__connections)


def process_data(server: Server, connection: socket, data: dict):
	"""
	Process recieved data from client. Watches on 'key' value of data and process relying on its value.

	:param server: server that has to process recieved data.
	:type: Server
	:param connection: socket to whom we send response.
	:type: socket
	:param data: data that we have recieved from client.
	:type: dict
	:returns: process recieved data.
	:rtype: void
	"""
	match data['key']:
		case 'CLOSECON':
			pass
		case 'REGUSER':
			server.send_response(connection, register_user(data['login'], data['password']))
		case 'LOGUSER':
			server.send_response(connection, sign_user(data['login'], data['password']))
		case 'CRTCHAT':
			server.send_response(connection, create_chat(data['members_id']))
		case 'ADDMSG':
			add_message_to_chat(data['chat_id'], data['owner_id'], data['message'])
		case 'GETCHATS':
			server.send_message(connection, get_chats(data['user_id']))
		case 'UPDUSERINFO':
			update_user_info(data['user_id'], data['surname'], data['name'], data['is_male'], data['bio'])
		case 'GETBIO':
			server.send_message(connection, get_bio_of_user(data['user_id']))
		case 'GETID':
			server.send_message(connection, get_id_by_login(data['login']))


def client_thread(server: Server, connection: socket):
	"""
	Function that describes a processing of a single client after it has connected to server

	:param server: server we connect to.
	:type: Server
	:param connection: socket we connect from.
	:type: socket
	:returns: runs a cycle to process data from client.
	:rtype: void
	"""
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
"""A variable that creates an instance of Server"""
