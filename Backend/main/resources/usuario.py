from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel

#Diccionario de prueba
USUARIOS = {
    1: {'firstname': 'Ana', 'lastname': 'Rotschtein'},
    2: {'firstname': 'Roberto', 'lastname': 'Vilches'},
    3: {'firstname': 'Silvina', 'lastname': 'Bru'}
}

#Recurso Usuario
class Usuario(Resource):
   
    def get(self, id):
        user = db.session.query(UsuarioModel).get_or_404(id)  
        return usuario.to_json()
        
    
    def delete(self, id):
        
        user = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201


class Usuarios(Resource):
    #Obtener lista de recursos
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])

    def post(self):

        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
