import sqlite3
from constants import *


def get_last_id():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	try:
		cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='Users' ''')
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
					print(result, 'get_last_id() result')
					return result
		db_connection.close()
	except Exception as error:
		db_connection.close()
		print('Failed to get last ID!', error)
	return 1


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


def register_user(username, password, gender, bio):
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	LAST_ID = get_last_id()
	try:
		print(LAST_ID, 'LAST_ID before db insert')
		cursor.execute('''
		INSERT INTO Users (user_id, username, password, gender, bio, form) VALUES (?, ?, ?, ?, ?, ?)
		''', (LAST_ID + 1, username, password, gender, bio, None))
		db_connection.commit()
		db_connection.close()
		increment_last_id()
		print('Registered user', username, password, gender, bio)
		print(LAST_ID, 'LAST_ID after reg')
		return True
	except Exception as error:
		db_connection.close()
		print('Failed to register user!', error, LAST_ID, 'LAST_ID in register_user()')
	return False


def initialize_db():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	gender BOOL,
	bio TEXT,
	form TEXT
	)
	''')
	db_connection.commit()
	db_connection.close()
