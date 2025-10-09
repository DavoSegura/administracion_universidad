from server.carreraService import CarreraService
from entities.carrera import Carrera
from flask import Flask, jsonify, request

app = Flask(__name__)

service = CarreraService()

@app.route("/getAllCarreras", methods=["GET"])
def get_all_carreras():
    data = service.GetCarreras()
    return jsonify({"carreras": data})

@app.route("/getCarrerasById/<int:idCarrera>", methods=["GET"])
def get_carrera_by_id(idCarrera):
    result = service.GetCarreraById(idCarrera)
    return jsonify({"resultado": result})

@app.route("/createCarrera", methods=["POST"])
def create_carrera():
    data = request.get_json()
    if not data or "nombre" not in data:
        return jsonify({"error": "Falta el campo 'nombre'"})
    carrera = Carrera(nombre=data["nombre"])
    msg = service.CreateCarrera(carrera)
    return jsonify({"mensaje": msg})

@app.route("/updateCarrera/<int:idCarrera>", methods=["PATCH"])
def update_carrera(idCarrera):
    data = request.get_json()
    if not data or "nombre" not in data:
        return jsonify({"error": "Falta el campo 'nombre'"})
    carrera = Carrera(idCarrera=idCarrera, nombre=data["nombre"])
    msg = service.UpdateCarrera(carrera)
    return jsonify({"mensaje": msg})

@app.route("/deleteCarreraById/<int:idCarrera>", methods=["DELETE"])
def delete_carrera(idCarrera):
    msg = service.DeleteCarrera(idCarrera)
    return jsonify({"mensaje": msg})