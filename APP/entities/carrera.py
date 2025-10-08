class Carrera:
    def __init__(self, nombre, idCarrera=None):
        self.__idCarrera = idCarrera
        self.SetNombre(nombre)

    def GetNombre(self):
        return self.__nombre
    def SetNombre(self, nombre):
        self.__nombre = nombre
    def GetIdCarrera(self):
        return self.__idCarrera

