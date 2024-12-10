import sqlite3
from constants import *


def get_last_id():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT MAX(user_id) FROM Users''')
		result = int(cursor.fetchone()[0])
		db_connection.close()
		return result
	except Exception as error:
		db_connection.close()
		print('Failed get last ID!', error)
	return -1


def print_users_table():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT * FROM Users''')
		result = cursor.fetchall()
		for item in result:
			print(item)
	except Exception as error:
		print('Failed to print table!', error)


def get_form_of_user(user_id):
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
		print('Failed to get form of user!', error)


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


def sign_user(login, password):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		SELECT password FROM Users WHERE username == ?
		''', (login,))
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


def register_user(user_info):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''
		INSERT INTO Users (user_id, username, password, bio) VALUES (?, ?, ?, ?)
		''', (LAST_ID + 1, user_info[0], user_info[1], None))
		db_connection.commit()
		db_connection.close()
		update_last_id()
		print('Registered user', user_info)
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
	bio TEXT
	)
	''')
	db_connection.commit()
	db_connection.close()
