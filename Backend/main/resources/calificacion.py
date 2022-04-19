from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import calificacionModel

#Diccionario de prueba
CALIFICACIONES = {
    1: {'calificacion' : 5},
    2: {'calificacion' : 4},
    3: {'calificacion' : 3}
}


class Calificacion(Resource):
  
    def get(self, id):
        
       calificacion = db.session.query(calificacionModel).get_or_404(id)
            return calificacion
       
    def put(self, id):
        calificacion = db.session.query(calificacionModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(calificacion, key, value)
        db.session.add(qualify)
        db.session.commit()
        return calificacion.to_json() , 201

 def delete(self, id):
        
        calificacion = db.session.query(califcacionModel).get_or_404(id)
        db.session.delete(calificacion)
        db.session.commit()
        return '', 204


class Calificaciones(Resource):
    
    def get(self):
        calificacion = db.session.query(calificacionModel).all()
        return jsonify([calificacion.to_json() for calificacion in calificaciones])

   
    def post(self):
        calificacion = calificacionModel.from_json(request.get_json())
        db.session.add(calificacion)
        db.session.commit()
        return calificacion.to_json(), 201