from .. import db
import statistics, datetime as dt

class Poema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    cuerpo = db.Column(db.String(1000), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=dt.datetime.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

# Relaciones

    usuario = db.relationship('Usuario', back_populates="poemas", uselist=False, single_parent=True)
    calificaciones = db.relationship('Calificacion', back_populates="poema", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<titulo: {self.titulo}, Poema: {self.cuerpo}, usuarioID: {self.user_id}, Date {self.fecha}>'

    def puntaje_promedio(self):
        calificaciones_lista = []
        if len(self.calificaciones) == 0:
            promedio = 0
        else:
            for calificaciones in self.calificaciones:
                puntaje = calificaciones.puntaje
                calificaciones_lista.append(puntaje)
            promedio = statistics.mean(calificaciones_lista)

            return promedio

    def to_json(self):
        poema_json = {
            'id' : self.id,
            'titulo' : str(self.titulo),
            'cuerpo' : str(self.cuerpo),
            'usuario' : self.usuario.to_json(),
            'date' : str(self.fecha.strftime("%d-%m-%Y")),
            'calificaciones' : [calificacion.to_json_short() for calificacion in self.calificaciones],
            'puntaje promedio' : self.puntaje_promedio()
        }
        return poema_json

    def to_json_short(self):
        poema_json = {
            'id' : self.id,
            'titulo' : self.titulo,
            'cuerpo' : self.cuerpo,
        }
        return poema_json

    @staticmethod
    def from_json(poem_json):
        id = poema_json.get('id')
        titulo = poema_json.get('titulo')
        usuario_id = poema_json.get('usuario_id')
        cuerpo = poema_json.get('cuerpo')
        return Poema(id=id, titulo=titulo, usuario_id=usuario_id, cuerpo=cuerpo)