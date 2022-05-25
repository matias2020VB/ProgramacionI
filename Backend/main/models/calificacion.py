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
        return f'<puntaje: {self.puntaje}, comentario: {self.comentario}, usuarios: {self.usuario_id}, poema {self.poema_id}>'
    
    # Objeto a JSON
    def to_json(self):
        calificacion_json = {
            'id': self.id,
            'puntaje': str(self.puntaje),
            'comentario': str(self.comentario),
            'usuario_id': self.usuario.to_json(),
            'poema_id': self.poema.to_json_short()
    
        }
        return calificacion_json

    def to_json_short(self):
        calificacion_json = {
            'id' : self.id,
            'puntaje' : self.puntaje,
            'comentario' : self.comentario,
            'usuario_id' : self.usuario.to_json(),
            'poema_id' : self.poema.to_json(),
        }
        return calificacion_json

    @staticmethod
    # JSON a objeto
    def from_json(calificacion_json):
        id = calificacion_json.get('id')
        puntaje = calificacion_json.get('puntaje')
        comentario = calificacion_json.get('comentario')
        poema_id = calificacion_json.get('poema_id')
        usuario_id = calificacion_json.get('usuario_id')
        return Calificacion(id=id, puntaje=puntaje, comentario=comentario, poema_id=poema_id, usuario_id=usuario_id)