from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import poemaModel

#Diccionario de prueba
POEMAS = {
    1: {'title' : 'Considerando el frio', 'Author': 'César Vallejo'},
    2: {'title' : 'Ya no será', 'Author': 'Idea Vilariño'},
    3: {'title' : 'No se porque me quejo', 'Author': 'Gloria Fuentes'}
}

#Recurso Poema
class Poema(Resource):
    
    def get(self, id):
        
         poema = db.session.query(poemaModel).get_or_404(id)
        return poema.to_json()
    
    #Eliminar recurso
    def delete(self, id):
        
        poema = db.session.query(poemaModel).get_or_404(id)
        db.session.delete(poema)
        db.session.commit()
        return '', 204

    #Modificar recurso
    def put(self, id):
        
         poema = db.session.query(poemaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(poema, key, value)
        db.session.add(poema)
        db.session.commit()
        return poema.to_json() , 201

#Recurso Profesores
class Poemas(Resource):
    def get(self):
        poemas = db.session.query(poemaModel).all()
        return jsonify([poema.to_json() for poema in poemas])
    
    def post(self):
         poema = poemaModel.from_json(request.get_json())
        db.session.add(poema)
        db.session.commit()
        return poema.to_json(), 201