import json
import random
import sqlite3
from constants import *


def get_last_id():
	"""
	Function to get the biggest ID in table Users.

	:returns: the biggest found index or zero if table doesn`t exists or an error has occured.
	:rtype: int
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'Users' ''')
		table = cursor.fetchone()
		db_connection.commit()
		if table != None:
			cursor.execute('''SELECT EXISTS(SELECT 1 FROM Users WHERE user_id = 1)''')
			exists = cursor.fetchone()[0]
			db_connection.commit()
			if exists == 1:
				cursor.execute('''SELECT MAX(user_id) FROM Users''')
				index = cursor.fetchone()
				if index[0] != ('None',):
					result = int(index[0])
					return result
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to get last ID!', error)
	return 0


def get_last_chat_id():
	"""
	Function to get the biggest ID in table Chats.

	:returns: the biggest found index or zero if table doesn`t exists or an error has occured.
	:rtype: int
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'Chats' ''')
		table = cursor.fetchone()
		db_connection.commit()
		if table != None:
			cursor.execute('''SELECT EXISTS(SELECT 1 FROM Chats WHERE chat_id = 1)''')
			exists = cursor.fetchone()[0]
			db_connection.commit()
			if exists == 1:
				cursor.execute('''SELECT MAX(chat_id) FROM Chats''')
				index = cursor.fetchone()
				if index[0] != ('None',):
					result = int(index[0])
					return result
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to get last chat ID!', error)
	return 0


def delete_users_table():
	"""
	Function that deletes table Users.

	:returns: deletes table.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''DROP TABLE Users''')
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to delete table!', error)
		

def delete_chats_table():
	"""
	Function that deletes table Chats.

	:returns: deletes table.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''DROP TABLE Chats''')
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to delete table!', error)


def delete_sessions_table():
	"""
	Function that deletes table Sessions.

	:returns: deletes table.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''DROP TABLE Sessions''')
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to delete table!', error)

def print_sessions_table():
	"""
	Function that prints table Sessions content.

	:returns: prints table content.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Sessions''')
		result = cursor.fetchall()
		for item in result:
			print(item)
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to print table!', error)


def print_chats_table():
	"""
	Function that prints table Chats content.

	:returns: prints table content.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Chats''')
		result = cursor.fetchall()
		for item in result:
			print(item)
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to print table!', error)


def print_users_table():
	"""
	Function that prints table Users content.

	:returns: prints table content.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users''')
		result = cursor.fetchall()
		for item in result:
			print(item)
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to print table!', error)


def get_id_by_login(login: str):
	"""
	Function that gets ID of user by his username(login).

	:param login: username of person.
	:type login: str
	:returns: ID of user.
	:rtype: int
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users WHERE username == ?''', 
				 (login, ))
		result = cursor.fetchone()[0]
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed to get bio of user!', error)
	return -1


def get_chat_id_by_members(member_id_1: str, member_id_2: str) -> int:
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT chat_id FROM Chats WHERE members_id LIKE ? AND members_id LIKE ?''', 
				 ('%' + member_id_1 + '%', '%' + member_id_2 + '%', ))
		result = int(cursor.fetchone()[0])
		print(result, 'CHAT ID BY MEMBERS')
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed to get bio of user!', error)
	return 0

def get_info_of_user(user_id):
	"""
	Function that gets bio of user by ID.

	:param user_id: ID of user whose bio we are getting.
	:type user_id: int
	:returns: string of user`s bio.
	:rtype: str
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users WHERE user_id == ?''', 
				 (user_id, ))
		result = cursor.fetchone()
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed to get bio of user!', error)


def update_user_info(user_id, surname, name, is_male, bio):
	"""
	Function that updates user`s information by given parameters.

	:param user_id: id of user whose info we change.
	:type: int
	:param surname: surname of the user.
	:type: str
	:param surname: name of user.
	:type: str
	:param is_male: represents sex of user.
	:type: bool
	:bio: information about user.
	:type: str
	:returns: updates info in table Users
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''UPDATE Users SET surname = ?, name = ?, is_male = ?, bio = ? WHERE user_id == ?''',
				 (surname, name, is_male, bio, user_id, ))
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to update user`s bio!', error)


def create_chat(members_ids: str) -> bool:
	"""
	Function that creates chat and writes down IDs of its members.

	:param members_ids: IDs of users who are members of chat.
	:type: str
	:returns: True if managed to create and False if didn`t.
	:rtype: bool
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	LAST_CHAT_ID = get_last_chat_id()
	print(LAST_CHAT_ID)
	try:
		cursor.execute('''
		INSERT INTO Chats (chat_id, members_id, number_of_messages, messages) VALUES (?, ?, ?, ?)
		''', (LAST_CHAT_ID + 1, members_ids, 0, '{}',))
		db_connection.commit()
		db_connection.close()
		increment_last_chat_id()
		print('Created chat')
		return True
	except Exception as error:
		db_connection.close()
		print('Failed to create chat!', error)
	return False


def add_message_to_chat(chat_id: int, owner: int, message: str):
	"""
	
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT number_of_messages FROM Chats WHERE chat_id == ?''', (chat_id, ))
		number_of_messages = int(cursor.fetchone()[0])
		cursor.execute('''SELECT messages FROM Chats WHERE chat_id == chat_id''')
		messages = json.loads(cursor.fetchone()[0])
		messages[str(number_of_messages + 1)] = {'owner': str(owner), 'message': message}
		cursor.execute('''UPDATE Chats SET number_of_messages = ?, messages = ? WHERE chat_id == ?''', 
				 (number_of_messages + 1, json.dumps(messages), chat_id, ))
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to add message to chat!', error)


def get_chats(user_id) -> list[int]:
	"""
	Function that gets list of IDs of whose member is user.

	:param user_id: ID of user.
	:type: int
	:returns: list of IDs.
	:rtype: list[int]
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		SELECT * FROM Chats WHERE members_id LIKE ?
		''', ('%' + str(user_id) + '%', ))
		result = cursor.fetchall()
		chats_id = []
		for item in result:
			chats_id.append(int(item[0]))
		return chats_id
	except Exception as error:
		print('Failed to get chats of user!', error)
	return []


def sign_user(login, password) -> bool:
	"""
	Function that authentiticate user with login and password.

	:param login: login of user.
	:type: str
	:param password: password of user.
	:type: str
	:returns: True if authentiticated succesfully and False otherwise.
	:rtype: bool
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		SELECT password FROM Users WHERE username == ?
		''', (login, ))
		user_password = cursor.fetchone()[0]
		db_connection.close()
		if user_password == password:
			print('Signed in user', login)
			return True
	except Exception as error:
		db_connection.close()
		print('Failed to sign in user!', error)
	print('Password incorrect!', login)
	return False


def register_user(username, password) -> bool:
	"""
	Function that registers user and writes down his login and password in db.

	:param username: username/login of user.
	:type: str
	:param password: password of user.
	:type: str
	:returns: True if registered succesfully and False otherwise.
	:rtype: bool
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	LAST_ID = get_last_id()
	try:
		cursor.execute('''
		INSERT INTO Users (user_id, username, password, surname, name, is_male, bio) VALUES (?, ?, ?, ?, ?, ?, ?)
		''', (LAST_ID + 1, username, password, '', '', '', '', ))
		db_connection.commit()
		db_connection.close()
		increment_last_id()
		print('Registered user', username, password)
		return True
	except Exception as error:
		db_connection.close()
		print('Failed to register user!', error)
	return False


def initialize_db():
	"""
	Function that creates tables Users, Chats and Sessions.

	:returns: creates tables.
	:rtype: void
	"""
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	name TEXT,
	surname TEXT,
	is_male BOOL,
	bio TEXT
	)
	''')
	db_connection.commit()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Chats (
	chat_id INTEGER PRIMARY KEY,
	members_id TEXT,
	number_of_messages INT,
	messages TEXT
	)
	''')
	db_connection.commit()
	db_connection.execute('''
	CREATE TABLE IF NOT EXISTS Sessions (
	session_id INTEGER PRIMARY KEY,
	user_id INTEGER,
	session TEXT
	)
	''')
	db_connection.close()
