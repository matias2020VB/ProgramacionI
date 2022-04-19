import email
from .. import db

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<usuario: %r %r >' % (self.firstname, self.password, self.role, self.email)
    
    #Convertir objeto en JSON
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'firstname': str(self.firstname),
            'lastname': str(self.lastname),
            'role': str(self.role),
            'email': str(self.email),
        }
        return usuario_json


    def to_json_short(self):
        usuario_json = {
            'id': self.id,
            'lastname': str(self.lastname),
            'password': str(self.firstname)
            'role': str(self.role),
            'email': str(self.email),

        }
        return usuario_json

    @staticmethod
    
    #Convertir JSON a objeto
    def from_json(usuario_json):
        firstname = usuario_json.get('firstname')
        password = usuario_json.get('password')
        role = usuario_json.get('role')
        email = usuario_json.get('email')
        
        return usuario(id=id,
                    firstname=firstname,
                    lastname=lastname,
                    role=role
                    email=email
                    )

