import os
from flask import Flask
from dotenv import load_dotenv
#Importar librería flask_restful
from flask_restful import Api
#Importar directorio de recursos
import main.resources as resources
#Inicializar API de Flask Restful
api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    #Cargar a la API el Recurso Profesors e indicar ruta
    api.add_resource(resources.ProfessorsResource, '/professors')
    #Cargar a la API el Recurso Profesor e indicar ruta
    api.add_resource(resources.ProfessorResource, '/professor/<id>')
    #Cargar la aplicación en la API de Flask Restful
    api.init_app(app)
    return app
