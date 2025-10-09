from config.connection import create_connection

connection = None

def init_connection():
    global connection
    password = "12345Aa."
    if connection is None:
        connection = create_connection(password)
    return connection
