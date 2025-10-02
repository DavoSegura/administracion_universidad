import mysql.connector

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
