from dao.carreraDAO import *
from flask import Flask, jsonify, request as req

app = Flask(__name__)

class CarreraService:
    def __init__(self):
        self.__carreraDAO = CarreraDao()

    def GetCarreras(self):
        return self.__carreraDAO.select()

    def GetCarreraById(self, idCarrera):
        carrera = self.__carreraDAO.select_by_id(idCarrera)
        if carrera is None:
            return f"No se encontró la carrera con ID {idCarrera}."
        return self.__carreraDAO.select_by_id(idCarrera)

    def CreateCarrera(self, carrera):
        return self.__carreraDAO.insert(carrera)

    def UpdateCarrera(self, carrera):
        return self.__carreraDAO.update(carrera)

    def DeleteCarrera(self, idCarrera):
        return self.__carreraDAO.delete_by_id(idCarrera)   
