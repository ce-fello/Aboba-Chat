import sqlite3
from constants import *


def print_users_table():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users''')
		result = cursor.fetchall()
		for item in result:
			print(item)
	except Exception as error:
		print('Failed to print table', error)


def sign_user(login, password):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		SELECT password FROM Users WHERE username == ?
		''', (login))
		user_password = cursor.fetchone()
		if user_password == password:
			print('Signed in user', login)
			return True
	except Exception as error:
		print('Failed to sign in user!', error)
	return False


def register_user(user_info):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		INSERT INTO Users (user_id, username, password, bio) VALUES (?, ?, ?, ?)
		''', (LAST_ID + 1, user_info[0], user_info[1], None))
		update_last_id()
		print('Registered user', user_info)
		return True
	except Exception as error:
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
	bio TEXT
	)
	''')
	# db_connection.commit()
	# cursor.execute('INSERT INTO Users (user_id, username, password, bio) VALUES (?, ?, ?, ?)', (1, 'huila', 'aboba', 'Ya gnom'))
	# db_connection.commit()
	# cursor.execute('INSERT INTO Users (user_id, username, password, bio) VALUES (?, ?, ?, ?)', (2, 'loh', 'hui', 'Ya indeec'))
	db_connection.commit()
	db_connection.close()