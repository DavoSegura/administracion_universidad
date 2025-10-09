import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

import config.db_global as db
from server.carreraService import CarreraService
from entities.carrera import Carrera
from flask import Flask, jsonify, request


if db.connection is None:
    db.init_connection()

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

@app.route("/createCarrera/", methods=["POST"])
def create_carrera():
    data = request.form["nombre"]
    if not data:
        return jsonify({"error": "Falta el campo 'nombre'"})
    carrera = Carrera(nombre=data)
    msg = service.CreateCarrera(carrera)
    return jsonify({"mensaje": msg})

@app.route("/updateCarrera/<int:idCarrera>", methods=["PATCH"])
def update_carrera(idCarrera):
    data = request.form["nombre"]
    if not data:
        return jsonify({"error": "Falta el campo 'nombre'"})
    carrera = Carrera(idCarrera=idCarrera, nombre=data)
    msg = service.UpdateCarrera(carrera)
    return jsonify({"mensaje": msg})

@app.route("/deleteCarreraById/<int:idCarrera>", methods=["DELETE"])
def delete_carrera(idCarrera):
    msg = service.DeleteCarrera(idCarrera)
    return jsonify({"mensaje": msg})

@app.route("/")
def main_web():
    return """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Administrador de Universidades</title>

  <style>
    body { font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; margin: 24px; background:#f5f7fb; color:#222; }
    .container { max-width:1000px; margin:0 auto; background:white; padding:20px; border-radius:8px; box-shadow:0 6px 20px rgba(0,0,0,0.06); }
    h1 { margin:0 0 12px 0; font-size:1.6rem; }
    .row { display:flex; gap:16px; flex-wrap:wrap; margin-bottom:12px; }
    .card { background:#fff; border:1px solid #e6e9ef; padding:12px; border-radius:8px; flex:1 1 300px; }
    label { display:block; font-size:0.9rem; margin-bottom:6px; }
    input[type="text"], input[type="number"], textarea { width:90%; padding:8px; border-radius:6px; border:1px solid #ccd3df; }
    button { padding:8px 12px; border-radius:6px; border:0; cursor:pointer; background:#2b6cb0; color:white; }
    button.secondary { background:#718096; }
    pre { background:#0f1724; color:#e6eef8; padding:12px; border-radius:6px; overflow:auto; }
    .small { font-size:0.85rem; color:#6b7280; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Administrador de Universidades</h1>
    <p class="small">Interfaz web simple para probar los endpoints de la API (GET/POST/PATCH/DELETE).</p>

    <div class="row">
      <div class="card">
        <h3>Listar todas las carreras</h3>
        <button id="btnList">Obtener todas</button>
        <pre id="allResult">Pulsa "Obtener todas" para ver el resultado aquí.</pre>
      </div>

      <div class="card">
        <h3>Buscar por ID</h3>
        <label for="idBuscar">ID</label>
        <input id="idBuscar" type="number" min="1" />
        <button id="btnGetById" class="secondary">Buscar</button>
        <pre id="byIdResult">Resultado de búsqueda...</pre>
      </div>
    </div>

    <div class="row">
      <div class="card">
        <h3>Crear carrera</h3>
        <label for="nombreCrear">Nombre</label>
        <input id="nombreCrear" type="text" placeholder="Ej: Ingeniería Informática" />
        <button id="btnCreate">Crear</button>
        <pre id="createResult">Estado de creación...</pre>
      </div>

      <div class="card">
        <h3>Actualizar carrera</h3>
        <label for="idUpdate">ID</label>
        <input id="idUpdate" type="number" min="1" />
        <label for="nombreUpdate">Nuevo nombre</label>
        <input id="nombreUpdate" type="text" />
        <button id="btnUpdate" class="secondary">Actualizar</button>
        <pre id="updateResult">Estado de actualización...</pre>
      </div>

      <div class="card">
        <h3>Eliminar carrera</h3>
        <label for="idDelete">ID</label>
        <input id="idDelete" type="number" min="1" />
        <button id="btnDelete">Eliminar</button>
        <pre id="deleteResult">Estado de eliminación...</pre>
      </div>
    </div>

    <hr/>
    <p class="small">Nota: esta UI asume que tu API expone los endpoints:</p>
    <ul class="small">
      <li><code>GET /getAllCarreras</code></li>
      <li><code>GET /getCarrerasById/&lt;id&gt;</code></li>
      <li><code>POST /createCarrera</code> (JSON {"nombre":"..."})</li>
      <li><code>PATCH /updateCarrera/&lt;id&gt;</code> (JSON {"nombre":"..."})</li>
      <li><code>DELETE /deleteCarreraById/&lt;id&gt;</code></li>
    </ul>
  </div>

  <script>
    const base = ''; // si Flask sirve el HTML desde la misma app, dejar vacío; si tu API está en otro dominio, poner la URL base.

    // Helpers
    const el = id => document.getElementById(id);
    const show = (id, text) => el(id).textContent = (typeof text === 'string') ? text : JSON.stringify(text, null, 2);

    // Listar todas
    el('btnList').addEventListener('click', async () => {
      show('allResult','Cargando...');
      try {
        const res = await fetch(base + '/getAllCarreras');
        const json = await res.json();
        // tu API devuelve { "carreras": "<texto>" } según la implementación actual
        show('allResult', json.carreras ?? json);
      } catch (err) {
        show('allResult','Error: ' + err);
      }
    });

    // Buscar por ID
    el('btnGetById').addEventListener('click', async () => {
      const id = el('idBuscar').value;
      if (!id) return show('byIdResult','Escribe un ID válido');
      show('byIdResult','Cargando...');
      try {
        const res = await fetch(base + '/getCarrerasById/' + encodeURIComponent(id));
        const json = await res.json();
        show('byIdResult', json.resultado ?? json);
      } catch (err) {
        show('byIdResult','Error: ' + err);
      }
    });

    // Crear
    el('btnCreate').addEventListener('click', async () => {
    const nombre = el('nombreCrear').value.trim();
    if (!nombre) return show('createResult','Escribe un nombre válido');
    show('createResult','Enviando...');
    try {
        const formData = new FormData();
        formData.append("nombre", nombre);

        const res = await fetch(base + '/createCarrera/', {
        method: 'POST',
        body: formData
        });
        const json = await res.json();
        show('createResult', json.mensaje ?? JSON.stringify(json));
    } catch (err) {
        show('createResult','Error: ' + err);
    }
    });

    // Actualizar carrera
    el('btnUpdate').addEventListener('click', async () => {
    const id = el('idUpdate').value;
    const nombre = el('nombreUpdate').value.trim();
    if (!id || !nombre) return show('updateResult','Escribe ID y nombre válidos');
    show('updateResult','Enviando...');
    try {
        const formData = new FormData();
        formData.append("nombre", nombre);

        const res = await fetch(base + '/updateCarrera/' + encodeURIComponent(id), {
        method: 'PATCH',
        body: formData
        });
        const json = await res.json();
        show('updateResult', json.mensaje ?? JSON.stringify(json));
    } catch (err) {
        show('updateResult','Error: ' + err);
    }
    });


    // Eliminar
    el('btnDelete').addEventListener('click', async () => {
      const id = el('idDelete').value;
      if (!id) return show('deleteResult','Escribe un ID válido');
      if (!confirm('¿Seguro que quieres eliminar la carrera con ID ' + id + '?')) return;
      show('deleteResult','Enviando...');
      try {
        const res = await fetch(base + '/deleteCarreraById/' + encodeURIComponent(id), {
          method: 'DELETE'
        });
        const json = await res.json();
        show('deleteResult', json.mensaje ?? JSON.stringify(json));
      } catch (err) {
        show('deleteResult','Error: ' + err);
      }
    });
  </script>
</body>
</html>

"""