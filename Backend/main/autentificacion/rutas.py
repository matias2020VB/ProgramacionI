from flask import request, jsonify, Blueprint
from .. import db
from main.models import ProfessorModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

#Blueprint para acceder a los métodos de autenticación

aute = Blueprint('aute', __name__, url_prefix='/aute')

#Método de logueo

@aute.route('/login', methods=['POST'])
def login():
    
    #Busca al profesor en la db por mail
    
    professor = db.session.query(ProfessorModel).filter(ProfessorModel.email == request.get_json().get("email")).first_or_404()
    
    #Valida la contraseña
    
    if professor.validate_pass(request.get_json().get("contraseña")):
        
        #Genera un nuevo token
        
        #Pasa el objeto professor como identidad
        
        access_token = create_access_token(identity=professor)
        
        #Devolver valores y token
        
        data = {
            'id': str(professor.id),
            'email': professor.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Contraseña incorrecta, vuelva a intentarlo.', 401

#Método de registro

@auth.route('/register', methods=['POST'])
def register():
    
    #Obtener professor
    
    professor = ProfessorModel.from_json(request.get_json())
    
    #Verificar si el mail ya existe en la db
    
    exists = db.session.query(ProfessorModel).filter(ProfessorModel.email == professor.email).scalar() is not None
    if exists:
        return 'mail duplicado', 409
    else:
        try:
            #Agregar professor a DB
            
            db.session.add(professor)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return professor.to_json() , 201
