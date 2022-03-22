from flask_restful import Resource
from flask import request


PROFESSORS = {
	1: {'firstname': 'Pedro', 'lastname': 'Marco'},
	2: {'firstname': 'Maria', 'lastname': 'Sosa'},
}

class Professor(Resource):
	def get(self, id):
		if int(id) in PROFESSORS:
			return PROFESSORS(int(id))
		return '', 404

	
	def delete(self,id):
		if int(id) in PROFESSORS:
			del PROFESSORS[int(id)]
			return '', 204
		return '', 404


	def put(self,id):
		if int(id) in PROFESSORS:
			professor = PROFESSORS[int(id)]
			data = request.get_json()
			professor.update(data)
			return professor, 201
		return '', 404


class Professors(Resource):
			def get(self):
				return PROFESSORS
			def post(self):
				professor = request.get_json()
				print(PROFESSORS.keys())
				print(max(PROFESSORS.keys()))
				id = int(max(PROFESSORS.keys())) + 1
				PROFESSORS[id] = professor
				return PROFESSORS[id], 201