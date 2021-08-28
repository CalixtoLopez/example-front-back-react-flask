"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
#tenemos que importar la tabla de la base de datos
from api.models import db, Account
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

## Los endpoints con las rutas a las que hago las llamadas
## Si queremos una cuenta no creamos el POST de una cuenta
## En este caso podemos poner account pero es mas sencilo con '/client' or '/business'
@api.route('/client', methods=['POST'])
def create_client():
    # Lo que tenemos que hacer es lo que nos envia el body es dicer el fecth
    # Aplicamos es esta propiedad de python a, b = 1, 2
    email = request.json.get('email',None)
    money = request.json.get('money',None)
    password = request.json.get('password',None)
    nick = request.json.get('nick',None)

    print({email} {money} {password} {nick})
    #siempre tenemos que tener un return vacio para que no dar problemas
    return {}, 200