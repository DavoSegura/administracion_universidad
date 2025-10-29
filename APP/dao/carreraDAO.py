from entities.carrera import Carrera
import config.connection as db

class CarreraDao:
    def __init__(self):
        self.__connection = db.connection

    def insert(self, carrera):
        mycursor = self.__connection.cursor()
        sql = "INSERT INTO carreras (nombre) VALUES (%s)"
        values = (carrera.GetNombre(),)
        mycursor.execute(sql, values)
        self.__connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")

    def select(self):
        mycursor = self.__connection.cursor()
        mycursor.execute("SELECT idCarrera, nombre FROM carreras")
        myresult = mycursor.fetchall()
        carreras = []
        for row in myresult:
            carrera = Carrera(row[1], row[0])
            carreras.append(carrera)
        return carreras
    
    def select_by_id(self, id):
        mycursor = self.__connection.cursor()
        mycursor.execute(("SELECT idCarrera, nombre FROM carreras WHERE idCarrera = %s"), (id,))
        row = mycursor.fetchone()
    
        if row:
            carrera = Carrera(idCarrera=row[0], nombre=row[1])
            return carrera
        else:
            return None

    def update(self, carrera):
        mycursor = self.__connection.cursor()
        sql = "UPDATE carreras SET nombre = %s WHERE idCarrera = %s"
        values = (carrera.GetNombre(), carrera.GetIdCarrera())
        mycursor.execute(sql, values)
        self.__connection.commit()
        return (f"Se han modificado {mycursor.rowcount} valores")

    def delete_by_id(self, carrera):
        id = carrera.GetIdCarrera()
        mycursor = self.__connection.cursor()
        sql = "DELETE FROM carreras WHERE idCarrera = %s"
        values = (id,)
        mycursor.execute(sql, values)
        self.__connection.commit()
        return (f"Se han eliminado {mycursor.rowcount} valores")
