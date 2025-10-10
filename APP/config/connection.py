import mysql.connector

connection = None

def create_connection(password):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = password,
            database = "university"
        )
        return mydb
    except mysql.connector.Error as e:
        print("Error en la conexión a la base de datos:", e)

def init_connection():
    global connection
    password = input("Introduce la contraseña a la Base de Datos: ")
    if connection is None:
        connection = create_connection(password)
    return connection
