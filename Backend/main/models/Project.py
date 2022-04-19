from .. import db
from . import ProfessorModel

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    #Campo clave foranea
    professorId = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    #Relación
    professor = db.relationship('Professor',back_populates="projects",uselist=False,single_parent=True)
    def __repr__(self):
        return '<Project: %r %r >' % (self.name, self.year)
    #Convertir objeto en JSON
    def to_json(self):
        self.professor = db.session.query(ProfessorModel).get_or_404(self.professorId)
        project_json = {
            'id': self.id,
            'name': str(self.name),
            'year': str(self.year),
            'professor': self.professor.to_json()
        }
        return project_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(project_json):
        id = project_json.get('id')
        name = project_json.get('name')
        year = project_json.get('year')
        professorId = project_json.get('professorId')
        return Project(id=id,
                    name=name,
                    year=year,
                    professorId = professorId
                    )
