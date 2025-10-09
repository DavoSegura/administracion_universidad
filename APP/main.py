from entities.carrera import Carrera
import config.db_global as db
from server.carreraService import CarreraService

menu = "\n1.- Insert\n2.- Select\n3.- Update\n4.- Delete\n5.- Select by ID\n0.- Exit"

correct_password = False
while correct_password == False:
    password = input("Introduce la contraseña a la Base de Datos: ")
    db.init_connection(password)
    if db.connection:
        correct_password = True
        print("¡Conexión establecida!")

# service_carreras = CarreraDao(connection)
service_carreras = CarreraService() 
run_app = True

while run_app == True:
    print(menu)

    option = input("Selecciona una opción: ")

    if option == "1":
        nombre_carrera = ""
        while nombre_carrera == "":
            nombre_carrera = input("Introduce el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre_carrera)
        service_carreras.CreateCarrera(carrera)

    elif option == "2": 
        select_all_carreras = service_carreras.GetCarreras()
        print(select_all_carreras)

    elif option == "3":
        idCarrera = int(input("Introduce el ID de la carrera que quiere actualizar: "))
        nombre = input("Introduce el nombre de la carrera actualizado: ")
        carrera = Carrera(idCarrera=idCarrera, nombre=nombre)
        service_carreras.UpdateCarrera(carrera)

    elif option == "4":
        idCarrera = int(input("Introduce el ID de la carrera que quiere eliminar: "))
        service_carreras.DeleteCarrera(idCarrera)

    elif option == "5":
        idCarrera = int(input("Introduce el ID de la carrera que quiere encontrar: "))
        print(service_carreras.GetCarreraById(idCarrera))
    elif option == "0":
        run_app = False
    else:
        print("Error. Introduce un número del menu.")
        