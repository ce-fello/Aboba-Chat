import sqlite3
from constants import *

def get_last_id():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	cursor.execute('SELECT * FROM Users')
	data = cursor.fetchall()
	for item in data:
		print(item)
	db_connection.close()
	return 1

def sign_user():
	return -1

def register_user():
	db_connection = sqlite3.connect(DB)
	cursor = db_connection.cursor()
	cursor.execute('''
	
	''')

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