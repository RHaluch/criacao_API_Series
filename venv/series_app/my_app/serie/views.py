import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.serie.models import Serie
from my_app import api, db

serie = Blueprint('serie', __name__)

parser = reqparse.RequestParser()
parser.add_argument('titulo', type=str)
parser.add_argument('genero', type=str)
parser.add_argument('temporadas', type=int)
parser.add_argument('mediaIMDB', type=float)
parser.add_argument('ativa', type=bool)

@serie.route("/")
@serie.route("/home")

def home():
    return "Catalogo de Series"

class SerieAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            series = Serie.query.paginate(page, 10).items
        else:
            series = [Serie.query.get(id)]
        if not series:
            abort(404)
        res = {}
        for ser in series:
            res[ser.id] = {
                'titulo': ser.titulo,
                'genero': ser.genero,
                'temporadas': str(ser.temporadas),
                'mediaIMDB': str(ser.mediaIMDB),
                'ativa': ser.ativa
            }

        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        genero = args['genero']
        temporadas = args['temporadas']
        mediaIMDB = args['mediaIMDB']
        ativa = args['ativa']

        ser = Serie(titulo, genero, temporadas, mediaIMDB, ativa)
        db.session.add(ser)
        db.session.commit()
        res = {}
        res[ser.id] = {
            'titulo': ser.titulo,
            'genero': ser.genero,
            'temporadas': str(ser.temporadas),
            'mediaIMDB': str(ser.mediaIMDB),
            'ativa': ser.ativa
        }

        return json.dumps(res)

api.add_resource(
    SerieAPI, '/api/serie','/api/<int:id>','/api/serie/<int:id>/<int:page>'
)