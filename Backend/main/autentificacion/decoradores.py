from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

#Decorador para restringir el acceso a usuarios admin

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #Verificar que el JWT es correcto
        verify_jwt_in_request()
        #Obtener claims de adentro del JWT
        claims = get_jwt()
        #Verificar que el rol sea admin
        if claims['rol'] =="admin" :
            #Ejecutar función
            return fn(*args, **kwargs)
        else:
            return 'Solo administradores pueden acceder', 403
    return wrapper

#Define el atributo que se utilizará para identificar el usuario

@jwt.user_identity_loader
def user_identity_lookup(professor):
    #Definir ID como atributo identificatorio
    return professor.id

#Define que atributos se guardarán dentro del token

@jwt.additional_claims_loader
def add_claims_to_access_token(professor):
    claims = {
        'rol': professor.role,
        'id': professor.id,
        'email': professor.email
    }
    return claims
