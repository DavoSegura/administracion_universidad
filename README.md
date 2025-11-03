# Administrador de Universidades

Aplicación en Python para gestionar carreras universitarias mediante una API REST construida con **Flask** y acceso a **MySQL**.

## 📂 Estructura del proyecto
API_administracion_universidad/
├── APP/
│ ├── api/
│ │ └── api.py
│ ├── config/
│ │ └── connection.py
│ │ └── db_global.py
│ ├── dao/
│ │ └── carreraDAO.py
│ ├── entities/
│ │ └── carrera.py
│ ├── server/
│ │ └── carreraService.py
│ └── main
├── .gitignore
└── README.md

## ⚙️ Configuración y ejecución

1. Instalar dependencias:

```bash
pip install flask mysql-connector-python
```
## ⚡Funcionalidades

### Endpoints de la API
```bash
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/getAllCarreras` | Lista todas las carreras |
| GET | `/getCarrerasById/<id>` | Busca una carrera por ID |
| POST | `/createCarrera/` | Crea una nueva carrera (`request.form["nombre"]`) |
| PATCH | `/updateCarrera/<id>` | Actualiza una carrera (`request.form["nombre"]`) |
| DELETE | `/deleteCarreraById/<id>` | Elimina una carrera por ID |
```
### Interfaz web

- Permite listar todas las carreras, buscar por ID, crear, actualizar y eliminar carreras.
- Los formularios envían datos usando `FormData` para ser compatibles con los endpoints de Flask.


## 🖥️ Ejecución

### Web
```bash
python -m flask --app APP.api.api run
```
### Consola
```bash
python APP/main.py
```
## 🗄️ Creación del schema
Puedes encontrar la base de datos en la carpeta BD con los diagramas informativos.
