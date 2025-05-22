from flask import Blueprint, request, jsonify
from models import db, Persona

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    return jsonify({"mensaje": "API de gestión de personas está funcionando"})

@routes.route('/personas', methods=['POST'])
def agregar_persona():
    data = request.json
    persona = Persona(nombre=data['nombre'], curp=data['curp'])
    db.session.add(persona)
    db.session.commit()
    return jsonify({"mensaje": "Persona agregada"}), 201

@routes.route('/personas', methods=['GET'])
def obtener_personas():
    personas = Persona.query.all()
    return jsonify([{"id": p.id, "nombre": p.nombre, "curp": p.curp} for p in personas])
