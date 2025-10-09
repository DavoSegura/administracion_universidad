from entities.carrera import Carrera
import config.db_global as db

class CarreraDao:
    def __init__(self):
        self.__connection = db.connection

    def insert(self, carrera):
        mycursor = self.__connection.cursor()
        sql = "INSERT INTO carreras (nombre) VALUES (%s)"
        values = (carrera.GetNombre(),)
        mycursor.execute(sql, values)
        self.__connection.commit()

    def select(self):
        mycursor = self.__connection.cursor()
        mycursor.execute("SELECT idCarrera, nombre FROM carreras")
        myresult = mycursor.fetchall()
        result_text = ""
        for row in myresult:
            result_text += f"idCarrera: {row[0]}, nombre: {row[1]}\n"
        return result_text
    
    def select_by_id(self, id):
        mycursor = self.__connection.cursor()
        mycursor.execute(("SELECT idCarrera, nombre FROM carreras WHERE idCarrera = %s"), (id,))
        return mycursor.fetchone()

    def update(self, carrera):
        mycursor = self.__connection.cursor()
        sql = "UPDATE carreras SET nombre = %s WHERE idCarrera = %s"
        values = (carrera.GetNombre(), carrera.GetIdCarrera())
        mycursor.execute(sql, values)
        self.__connection.commit()

    def delete_by_id(self, id):
        mycursor = self.__connection.cursor()
        sql = "DELETE FROM carreras WHERE idCarrera = %s"
        values = (id,)
        mycursor.execute(sql, values)
        self.__connection.commit()
        return mycursor.rowcount
