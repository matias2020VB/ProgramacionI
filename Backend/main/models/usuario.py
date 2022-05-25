from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    calificaciones = db.relationship('Calificacion', back_populates="usuario", cascade="all, delete-orphan")
    poemas = db.relationship('Poema', back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return '<usuario: %r %r >' % (self.nombre, self.contraseña, self.rol, self.email)
    
    #Convertir objeto en JSON
    def to_json_complete(self):
        poemas = [poema.to_json() for poema in self.poemas]
        calificaciones = [calificacion.to_json_short() for calificacion in self.calificaciones],
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'rol': str(self.rol),
            'email': str(self.email),
            'poemas' : poemas,
            'calificaciones' : calificaciones,
        }
        return usuario_json

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            #'contraseña': str(self.contraseña),
            #'email': str(self.email),
            #'rol': str(self.rol),
            'numero_poemas': len(self.poemas),
            'numero_calificaciones': len(self.calificaciones),
            'poemas':[poema.to_json_short() for poema in self.poemas],
            
        }
        return usuario_json


    def to_json_short(self):
        usuario_json = {
            'id' : self.id,
            'nombre' : self.nombre,
        }
        return usuario_json

    @staticmethod
    
    #Convertir JSON a objeto
    def from_json(usuario_json):
        nombre = usuario_json.get('nombre')
        contraseña = usuario_json.get('contraseña')
        rol = usuario_json.get('rol')
        email = usuario_json.get('email')
        id=usuario_json.get('id')
        
        return Usuario(id=id,
                    nombre=nombre,
                    rol=rol,
                    email=email,
                    )

