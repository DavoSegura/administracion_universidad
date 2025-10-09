from config.connection import create_connection

connection = None

def init_connection():
    global connection
    password = input("Introduce la contraseña a la Base de Datos: ")
    if connection is None:
        connection = create_connection(password)
    return connection
