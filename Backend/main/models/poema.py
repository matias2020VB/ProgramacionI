from email.policy import default
from .. import db
from sqlalchemy.sql import func

class poema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    usuarioID = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String(100), nullable=False)
    dateTime = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return '<poema: %r %r >' % (self.id, self.title, self.usuarioID, self.body, self.dateTime)
    

    #Convertir objeto en JSON
    def to_json(self):
        poema_json = {
            'id': self.id,
            'title': str(self.title),
            'usuarioID': str(self.usuarioID),
            'body': str(self.body),
            'dateTime': str(self.dateTime),
        }
        return poema_json

    def to_json_short(self):
        poema_json = {
            'id': self.id,
            'title': str(self.title),
            'usuarioID': str(self.usuarioID),
            'body': str(self.body),
            'dateTime': str(self.dateTime),
        }
        
        
        return poema_json
    

    @staticmethod
    #Convertir JSON a objeto
    
    def from_json(poema_json):
        id = poema_json.get('id')
        title = poema_json.get('title')
        usuarioID = poema_json.get('usuarioID')
        body = poema_json.get('body')
        dateTime = poema_json.get('dateTime'),

        return Professor(id=id,
                     title=title,
                    userID=userID,
                    body=body,
                    dateTime=dateTime
                    )
