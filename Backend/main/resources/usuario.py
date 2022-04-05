from flask_restful import Resource
from flask import request

#Diccionario de prueba
USUARIOS = {
    1: {'firstname': 'Pedro', 'lastname': 'Marco'},
    2: {'firstname': 'María', 'lastname': 'Sosa'}
}

#Recurso Profesor
class Usuario(Resource):
    #Obtener recurso
    def get(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in USUARIOS:
            #Devolver professor correspondiente
            return USUARIOS[int(id)]
        #Devolver error 404 en caso que no exista
        return '', 404
    #Eliminar recurso
    def delete(self, id):
        #Verificar que exista un Profesor con ese Id en diccionario
        if int(id) in USUARIOS:
            #Eliminar professor del diccionario
            del USUARIOS[int(id)]
            return '', 204
        return '', 404
    #Modificar recurso
    def put(self, id):
        if int(id) in USUARIOS:
            Usuario = USUARIOS[int(id)]
            #Obtengo los datos de la solicitud
            data = request.get_json()
            Usuario.update(data)
            return usuario, 201
        return '', 404

#Recurso Profesores
class Usuarios(Resource):
    #Obtener lista de recursos
    def get(self):
        return USUARIOS
    #Insertar recurso
    def post(self):
        #Obtener datos de la solicitud
        Usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = Usuario
        return USUARIOS[id], 201
