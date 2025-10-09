from dao.carreraDAO import *

class CarreraService:
    def __init__(self, connection):
        self.__carreraDAO = CarreraDao(connection)

    def GetCarreras(self):
        return self.__carreraDAO.select()

    # def GetCarreraById(self, idCarrera):
    #     return self.__carreraDAO.GetCarreraById(idCarrera)

    def CreateCarrera(self, carrera):
        return self.__carreraDAO.insert(carrera)

    def UpdateCarrera(self, carrera):
        return self.__carreraDAO.update(carrera)

    def DeleteCarrera(self, idCarrera):
        return self.__carreraDAO.delete_by_id(idCarrera)   
    
