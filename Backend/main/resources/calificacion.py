from flask_restful import Resource
from flask import request

#Diccionario de prueba
CALIFICACIONES = {
    1: {'calificacion' : 5},
    2: {'calificacion' : 4},
    3: {'calificacion' : 3}
}

#Recurso Profesor
class Calificacion(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in CALIFICACIONES:
            #Devolver professor correspondiente
            return CALIFICACIONES[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in CALIFICACIONES:
            #Eliminar professor del diccionario
            del CALIFICACIONES[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in CALIFICACIONES:
            Calificacion = CALIFICACIONES[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Calificacion.update(data)
            return Calificacion, 201
        return '', 404

#Recurso Profesores
class Calificaciones(Resource):
    #Obtener lista de recursos
    def get(self):
        return CALIFICACIONES
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        calificacion = request.get_json()
        id = int(max(CALIFICACIONES.keys())) + 1
        CALIFICACIONES[id] = calificacion
        return CALIFICACIONES[id], 201
