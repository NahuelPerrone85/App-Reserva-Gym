"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Administrador
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from sqlalchemy import select

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['GET'])
def get_users():

    all_users =  db.session.execute(select(User)).scalars().all()
    if all_users is None:
        return 'Cant get users', 400
    
    result = list(map(lambda user: user.serialize(), all_users))

    return jsonify(result), 200

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user =  db.session.execute(select(User).where(User.id == user_id)).scalars().first()
    if user is None:
        return 'Cant get the user', 400

    return jsonify(user.serialize()), 200

@api.route('/user', methods=['POST'])
def add_users():

    body = request.get_json()

    if body is None:
        return 'El cuerpo debe seguir la siguiente estructura, {"name": name, "last_name": last_name, "password": password, "email": email}', 400
    if 'name' not in body:
        return 'Debes especificar name', 400
    if "last_name" not in body:
        return "Debe especificar last_name", 400
    if 'password' not in body:
        return 'Debes especificar password', 400
    if 'email' not in body:
        return 'Debes especificar email', 400
    
    new_user =  User(
        name = body['name'],
        last_name = body ["last_name"],
        password = body['password'],
        email = body['email'],
    )

    db.session.add(new_user)
    db.session.commit()
    

    return 'User successful created', 200

@api.route('/user/<int:user_id>', methods=['PUT'])
def edit_users(user_id):

    body = request.get_json()
    user = db.session.execute(select(User).where(User.id == user_id)).scalars().first()

    if user is None:
        return 'User dont exist', 400

    if body is None:
        return 'El cuerpo debe seguir la siguiente estructura, {"name": name, "last_name": last_name, "password": password, "email": email}', 400
    if 'name' in body:
        user.name = body['name']
    if 'last_name' in body:
        user.last_name = body['last_name']
    if 'password' in body:
        user.password = body['password']
    if 'email' in body:
        user.email = body['email']
    
    db.session.commit()
    
    return 'User with id ' + str(user_id) + ' has been edited', 200

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):

    user = db.session.execute(select(User).where(User.id == user_id)).scalars().first()

    if user is None:
        return 'User dont exist', 400

    db.session.delete(user)
    db.session.commit()

    return 'User with id ' + str(user_id) + ' has been deleted', 200

@api.route('/administrador', methods=['GET'])
def get_administradors():

    all_administradors =  db.session.execute(select(Administrador)).scalars().all()
    if all_administradors is None:
        return 'Cant get users', 400
    
    result = list(map(lambda administrador: administrador.serialize(), all_administradors))

    return jsonify(result), 200

@api.route('/administrador/<int:administrador_id>', methods=['GET'])
def get_administrador(administrador_id):

    administrador =  db.session.execute(select(Administrador).where(Administrador.id == administrador_id)).scalars().first()
    if administrador is None:
        return 'Cant get the administrador', 400

    return jsonify(administrador.serialize()), 200

@api.route('/administrador', methods=['POST'])
def add_administradors():

    body = request.get_json()

    if body is None:
        return 'El cuerpo debe seguir la siguiente estructura, {"name": name, "last_name": last_name, "password": password, "email": email}', 400
    if 'name' not in body:
        return 'Debes especificar name', 400
    if "last_name" not in body:
        return "Debe especificar last_name", 400
    if 'password' not in body:
        return 'Debes especificar password', 400
    if 'email' not in body:
        return 'Debes especificar email', 400
    
    new_administrador = Administrador(
        name = body['name'],
        last_name = body ["last_name"],
        password = body['password'],
        email = body['email'],
    )

    db.session.add(new_administrador)
    db.session.commit()
    

    return 'Administrador successful created', 200

@api.route('/administrador/<int:administrador_id>', methods=['PUT'])
def edit_administradors(administrador_id):

    body = request.get_json()
    administrador = db.session.execute(select(Administrador).where(Administrador.id == administrador_id)).scalars().first()

    if administrador is None:
        return 'Admin dont exist', 400

    if body is None:
        return 'El cuerpo debe seguir la siguiente estructura, {"name": name, "last_name": last_name, "password": password, "email": email}', 400
    if 'name' in body:
        administrador.name = body['name']
    if 'last_name' in body:
        administrador.last_name = body['last_name']
    if 'password' in body:
        administrador.password = body['password']
    if 'email' in body:
        administrador.email = body['email']
    
    db.session.commit()
    
    return 'Administrador with id ' + str(administrador_id) + ' has been edited', 200

@api.route('/administrador/<int:administrador_id>', methods=['DELETE'])
def delete_administradors(administrador_id):

    administrador = db.session.execute(select(Administrador).where(Administrador.id == administrador_id)).scalars().first()

    if administrador is None:
        return 'administrador dont exist', 400

    db.session.delete(administrador)
    db.session.commit()

    return 'Administrador with id ' + str(administrador_id) + ' has been deleted', 200