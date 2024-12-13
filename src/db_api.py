import sqlite3
from constants import *


def get_last_id():
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


def get_form_of_user(user_id):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users WHERE user_id == ?''', 
				 (user_id, ))
		result = cursor.fetchone()[4]
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed to get form of user!', error)


def get_bio_of_user(user_id):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users WHERE user_id == ?''', 
				 (user_id, ))
		result = cursor.fetchone()[3]
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed to get bio of user!', error)


def update_user_form(user_id, new_bio):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''UPDATE Users SET bio = ? WHERE user_id == ?''',
				 (new_bio, user_id, ))
		db_connection.commit()
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to update user`s bio!', error)


def create_chat(members_ids: str):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	LAST_CHAT_ID = get_last_chat_id()
	print(LAST_CHAT_ID)
	try:
		cursor.execute('''
		INSERT INTO Chats (chat_id, members_id, messages) VALUES (?, ?, ?)
		''', (LAST_CHAT_ID + 1, members_ids, '',))
		db_connection.commit()
		db_connection.close()
		increment_last_chat_id()
		print('Created chat')
		return True
	except Exception as error:
		db_connection.close()
		print('Failed to create chat!', error)
	return False


def get_chats(user_id) -> list[int]:
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


def sign_user(login, password):
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


def register_user(username, password, gender, bio):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	LAST_ID = get_last_id()
	try:
		cursor.execute('''
		INSERT INTO Users (user_id, username, password, gender, bio, form) VALUES (?, ?, ?, ?, ?, ?)
		''', (LAST_ID + 1, username, password, gender, bio, None, ))
		db_connection.commit()
		db_connection.close()
		increment_last_id()
		print('Registered user', username, password, gender, bio)
		return True
	except Exception as error:
		db_connection.close()
		print('Failed to register user!', error)
	return False


def initialize_db():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	gender TEXT,
	bio TEXT,
	form TEXT
	)
	''')
	db_connection.commit()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Chats (
	chat_id INTEGER PRIMARY KEY,
	members_id TEXT,
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

# user_id_1, user_id_2 
# -> json.dumps()
# chat_members 
#
# [{	
# 	'message_id': 'message_id',
# 	'owner': 'user_id',
# 	'time': 'time',
# 	'message': 'text'
# }, 
# {
# 	'message_id': 'message_id',
# 	'owner': 'user_id',
# 	'time': 'time',
# 	'message': 'text'
# },
# ...
# ] -> json.dumps()
# chat_messages