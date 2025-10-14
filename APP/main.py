from entities.carrera import Carrera
import config.connection as db
from server.carreraService import CarreraService

menu = "\n1.- Insert\n2.- Select\n3.- Update\n4.- Delete\n0.- Exit"

correct_password = False
while correct_password == False:
    db.init_connection()
    if db.connection:
        correct_password = True
        print("¡Conexión establecida!")

service_carreras = CarreraService() 
run_app = True

def GetIdCarrera(message):
    isIdValid = False
    while isIdValid == False:
        idCarrera = input(message)

        if idCarrera.isdigit():
            idCarrera = int(idCarrera)

            carreras = service_carreras.GetCarreras()
            ids_existentes = [carrera.GetIdCarrera() for carrera in carreras]

            if idCarrera in ids_existentes:
                isIdValid = True
            else:   
                print("El ID introducido es incorrecto")
        else:
            print("El ID debe ser un dígito")

    return idCarrera

def GetNameCarrera(message):
    isIdValid = False
    while isIdValid == False:
        nameCarrera = input(message)

        if nameCarrera != "":
            carreras = service_carreras.GetCarreras()
            namesCarreras = [carrera.GetNombre() for carrera in carreras]

            if nameCarrera in namesCarreras:
                isIdValid = True
            else:   
                print("El nombre introducido no ha sido encontrado")
        else:
            print("El ID es incrorrecto")

    return nameCarrera

def GetCarreraById(idCarrera):
    carreras = service_carreras.GetCarreras()
    carreraSelected = None

    for carrera in carreras:
        if idCarrera == carrera.GetIdCarrera():
            carreraSelected = carrera

    return carreraSelected

def GetCarreraByName(nameCarrera):
    carreras = service_carreras.GetCarreras()
    carreraSelected = None

    for carrera in carreras:
        if nameCarrera == carrera.GetNombre():
            carreraSelected = carrera

    return carreraSelected

while run_app == True:
    print(menu)

    option = input("Selecciona una opción: ")

    if option == "1":
        message = "Introduce el nombre de la carrera: "
        nameCarrera = input(message)
        carrera = Carrera(nombre=nameCarrera)
        print(service_carreras.CreateCarrera(carrera))

    elif option == "2": 
        carreras = service_carreras.GetCarreras()
        result_text = ""
        for carrera in carreras:
            result_text += f"idCarrera: {carrera.GetIdCarrera()}, nombre: {carrera.GetNombre()}\n"
        print(result_text)

    elif option == "3":
        message = "Introduce el ID de la carrera que quiere actualizar: "
        idCarrera = GetIdCarrera(message)

        message = "Introduce el nombre de la carrera actualizado: "
        nameCarrera = GetNameCarrera(message)

        carrera = Carrera(idCarrera=idCarrera, nombre=nameCarrera)
        print(service_carreras.UpdateCarrera(carrera))

    elif option == "4":
        message = "Introduce el nombre de la carrera que quieras eliminar: "
        nameCarrera = GetNameCarrera(message)
        carrera = GetCarreraByName(nameCarrera)

        print(service_carreras.DeleteCarrera(carrera))

    # elif option == "5":
    #     message = "Introduce el ID de la carrera que quiere encontrar: "
    #     idCarrera = GetIdCarrera(message)

    #     print(service_carreras.GetCarreraById(idCarrera))

    elif option == "0":
        run_app = False
    else:
        print("Error. Introduce un número del menu.")
