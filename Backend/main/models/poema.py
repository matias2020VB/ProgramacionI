from .. import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Professor: %r %r >' % (self.firstname, self.lastname)
    #Convertir objeto en JSON
    def to_json(self):
        professor_json = {
            'id': self.id,
            'firstname': str(self.firstname),
            'lastname': str(self.lastname),

        }
        return professor_json

    def to_json_short(self):
        professor_json = {
            'id': self.id,
            'lastname': str(self.lastname),

        }
        return professor_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(professor_json):
        id = professor_json.get('id')
        firstname = professor_json.get('firstname')
        lastname = professor_json.get('lastname')
        return Professor(id=id,
                    firstname=firstname,
                    lastname=lastname,
                    )
