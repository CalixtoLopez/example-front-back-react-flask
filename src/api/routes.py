"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from decimal import Decimal
from flask import Flask, request, jsonify, url_for, Blueprint
from sqlalchemy import exc
#tenemos que importar la tabla de la base de datos
from api.models import db, Account, Client
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

@api.route('/client/<int:id>', methods=['PUT'])
#@jwt_required() ## requiere instalacion
def edit_client(id):
    new_info = { 
        'email' : request.json.get('email', None),
        #money = request.json.get('money', None)
        'password' : request.json.get('password', None)
        #'nick' : request.json.get('nick', None)
    }
    account = Account.get_by_id(id)
    if account:
        update_client = account.edit_client(**{
            key: value for key,value in new_info.items()
            if value is not None
        })
        return jsonify(update_client.to_dict()), 200
    return {'error': 'Fail no user¡¡'} , 400


@api.route('/account/', methods=['GET'])
def get_account_all():
    accounts = Account.get_all()
    if accounts:
        accounts_to_dict = [account.to_dict() for account in accounts ]
        return jsonify(accounts_to_dict), 200 
    return jsonify({'error': 'Accounts no fount¡¡¡¡'}), 404

@api.route('/client/', methods=['GET'])
def get_client_all():
    clients = Client.get_all()
    if clients:
        clients_to_dict = [client.to_dict() for client in clients ]
        return jsonify(clients_to_dict), 200 
    return jsonify({'error': 'Clients no fount¡¡¡¡'}), 404

@api.route('/client/<int:id>', methods=['GET'])
def get_client_id(id):
    account = Account.get_by_id(id)
    if account:
        account_id = account.to_dict()
        return jsonify(account_id), 200 
    return jsonify({'error': 'Account no fount¡¡¡¡'}), 404

@api.route('/client/', methods=['POST'])
def create_client():
    # Lo que tenemos que hacer es lo que nos envia el body es dicer el fecth
    # Podemosa palicar esta propiedad de python a, b = 1, 2
    email = request.json.get('email', None)
    money = request.json.get('money', None)
    password = request.json.get('password', None)
    nick = request.json.get('nick', None)
    
    if not (email and money and password and nick):
        return({'error': 'Missing info'}), 400
    
    # Lo primero es crearnos la cuenta
    account = Account(
        email=email,
        money=Decimal(f'{money}'),
        is_client=True,
        _password=password,
        _is_active=True
    )
    # Para saber que esta creada la cuenta lo envolvemos en un try
    try:
        account.create()
        #con esto me devuelve la cuenta lo que queremos es que me devuelva la cuenta del cliente
        #return jsonify(account.to_dict()), 201
    except exc.IntegrityError:
        return({"error" : "This mail is ready in use"}), 400
    
    
    #En postman haremos una peticion al api con esta ruta y esto nos ayuda ver el json con los dato metidos

    client = Client(nick=nick, account_id=account.id)
    try:
        client.create()
        return jsonify(client.to_dict()), 201
        
    except exc.IntegrityError:
        return({"error" : "This nick is ready in use"}), 400

    print({email}, {money}, {password}, {nick})
    #siempre tenemos que tener un return vacio para que no dar problemas
    #
    #return {}, 200
