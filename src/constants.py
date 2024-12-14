HOSTNAME = 'localhost' 
PORT = 27012
DB = 'my_database.db'
LAST_ID = 0
LAST_CHAT_ID = 0


def increment_last_id():
    """
    Increments LAST_ID - variable that shows the biggest ID of Users
    """
    global LAST_ID
    LAST_ID += 1


def increment_last_chat_id():
    """
    Increments LAST_CHAT_ID - variable that shows the biggest ID of Chats
    """
    global LAST_CHAT_ID
    LAST_CHAT_ID += 1
