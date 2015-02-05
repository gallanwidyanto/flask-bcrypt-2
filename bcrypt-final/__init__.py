#-*-encoding:utf-8-*-
from flask import Flask, request
from flask import Blueprint
from flask.ext import restful
from flask.ext.restful.utils import cors
from database import db


api = restful.Api()
blueprint = Blueprint('hello_blueprint', __name__)
api.init_app(blueprint)
blueprint.config = {}
api.decorators = [cors.crossdomain(origin='*', headers=["Authorization", "Content-Type"])]


class UserModule:

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            url_prefix = kwargs.get('url_prefix', '/api')
            self.init_app(args[0], url_prefix=url_prefix)

    def init_app(self, app, url_prefix='/api'):
        db.init_app(app)
        app.register_blueprint(blueprint, url_prefix=url_prefix)


# Declaração das Rotas da API

from users import ListUsersRest

api.add_resource(ListUsersRest, '/users')