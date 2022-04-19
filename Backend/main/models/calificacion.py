from .. import db
class calificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    usuarioID = db.Column(db.Integer, nullable=False)
    poemaID = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<calificacion: %r %r >' % (self.id, self.score, self.comment, self.usuarioID, self.poemaID)
    

    #Convertir objeto en JSON
    def to_json(self):
        calificacion_json = {
            'id': self.id,
            'score': str(self.score),
            'comment': str(self.comment),
            'usuarioID': str(self.usuarioID),
            'poemaID': str(self.poemaID),
        }
        return calificacion_json

    def to_json_short(self):
        calificacion_json = {
            'id': self.id,
            'score': str(self.score),
            'comment': str(self.comment),
            'usuarioID': str(self.usuarioID),
            'poemaID': str(self.poemaID),
        }
        
        return calificacion_json
    
    @staticmethod
    
    #Convertir JSON a objeto
    
    def from_json(calificacion_json):
        id = calificacion_json.get('id')
        score = mark_json.get('score')
        comment = calificacion_json.get('comment')
        userID = calificacion_json.get('usuarioID')
        poemaID = calificacion_json.get('poemaID'),
        return calificacion(id=id,
                    score=score,
                    comment=comment,
                    usuarioID=usuarioID,
                    poemaID=poemaID
                    )
