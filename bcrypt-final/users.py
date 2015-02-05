from flask.ext.restful import reqparse
from flask.ext import restful
from database import db


class UserLib:

	@staticmethod
	def create(usename, password):
		''' Cria um usuario '''
		user = UserModel(name, username, password)
		db.session.add(user)
		db.session.commit()

		return {"status": True}

	
class ListUsersRest(restful.Resource):


	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username', type=str, required=True)
		parser.add_argument('password', type=str, required=True)
		args = parser.parse_args()
		return UserLib.create(args['username'], args['password'])