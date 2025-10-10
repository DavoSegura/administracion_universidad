from entities.carrera import Carrera
import config.connection as db
from server.carreraService import CarreraService

menu = "\n1.- Insert\n2.- Select\n3.- Update\n4.- Delete\n5.- Select by ID\n0.- Exit"

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
            ids_existentes = [carrera[0] for carrera in carreras]

            if idCarrera in ids_existentes:
                isIdValid = True
            else:   
                print("El ID introducido es incorrecto")
        else:
            print("El ID debe ser un dígito")

    return idCarrera

while run_app == True:
    print(menu)

    option = input("Selecciona una opción: ")

    if option == "1":
        nombre_carrera = ""
        while nombre_carrera == "":
            nombre_carrera = input("Introduce el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre_carrera)
        print(service_carreras.CreateCarrera(carrera))

    elif option == "2": 
        select_all_carreras = service_carreras.GetCarreras()
        result_text = ""
        for row in select_all_carreras:
            result_text += f"idCarrera: {row[0]}, nombre: {row[1]}\n"
        print(result_text)

    elif option == "3":
        message = "Introduce el ID de la carrera que quiere actualizar: "
        idCarrera = GetIdCarrera(message)

        nombre_carrera = ""
        while nombre_carrera == "":
            nombre_carrera = input("Introduce el nombre de la carrera actualizado: ")

        carrera = Carrera(idCarrera=idCarrera, nombre=nombre_carrera)
        print(service_carreras.UpdateCarrera(carrera))

    elif option == "4":
        message = "Introduce el ID de la carrera que quiere eliminar: "
        idCarrera = GetIdCarrera(message)

        print(service_carreras.DeleteCarrera(idCarrera))

    elif option == "5":
        message = "Introduce el ID de la carrera que quiere encontrar: "
        idCarrera = GetIdCarrera(message)

        print(service_carreras.GetCarreraById(idCarrera))

    elif option == "0":
        run_app = False
    else:
        print("Error. Introduce un número del menu.")
