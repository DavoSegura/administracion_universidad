from config.connection import create_connection

connection = None

def init_connection(password):
    global connection
    if connection is None:
        connection = create_connection(password)
    return connection
