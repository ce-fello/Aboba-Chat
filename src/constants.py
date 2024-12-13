HOSTNAME = 'localhost'
PORT = 3030
DB = 'my_database.db'
LAST_ID = 0
LAST_CHAT_ID = 0

def increment_last_id():
    global LAST_ID
    LAST_ID += 1

def increment_last_chat_id():
    global LAST_CHAT_ID
    LAST_CHAT_ID += 1
    