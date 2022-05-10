from .. import db

class Calificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puntaje = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Integer, nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    poema_id = db.Column(db.Integer, db.ForeignKey('poema.id'), nullable=False)

# Relaciones
    
    usuario = db.relationship('Usuario', back_populates="calificaciones", uselist=False, single_parent=True)
    poema = db.relationship('Poema', back_populates="calificaciones", uselist=False, single_parent=True)

    def __repr__(self):
        return f'<puntaje: {self.puntaje}, comentario: {self.comentario}, usuarios: {self.usuario_id}, poema {self.poemaa_id}>'
    # Objeto a JSON
    def to_json(self):
        poema = poema.to_json()
        usuarios = [usuarioss.to_json() for usuarios in self.usuarios]
        calificacion_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'contrasña': str(self.contrasña),
            'rol': str(self.rol),
            'email': str(self.email),
            'poema' : poema,
            'usuario' : usuario
        }
        return calificacion_json

    def to_json_short(self):
        calificacion_json = {
            'id' : self.id,
            'puntaje' : self.puntaje,
            'comentario' : self.comentario,
            'usuario_id' : self.usuario_id,
            'poema_id' : self.poema_id
        }
        return calificacion_json

    @staticmethod
    # JSON a objeto
    def from_json(calificacion_json):
        id = calificacion_json.get('id')
        puntaje = calificacion_json.get('puntaje')
        comentario = calificacion_json.get('comentario')
        poemaa_id = calificacion_json.get('poema_id')
        usuario_id = calificacion_json.get('usuario_id')
        return calificacion(id=id, puntaje=puntaje, comentario=comentario, poema_id=poema_id, usuario_id=usuario_id)