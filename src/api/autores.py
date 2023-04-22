from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.autores import autores, AutoresSchema

routes_autores = Blueprint("routes_autor", __name__)

autor_schema = AutoresSchema()
autores_Schema = AutoresSchema(many=True)

#Datos de la tabla autores
@routes_autores.route('/autores', methods=['GET'])
def obtenerautores():    
    returnall = autores.query.all()
    result_autores = autores_Schema.dump(returnall)
    return jsonify(result_autores)


#<--------------------------CRUD AUTORES--------------------------->
@routes_autores.route('/eliminarautores/<id>', methods=['GET'] )
def eliminarautores(id):
    rol = autores.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(autor_schema.dump(rol))

@routes_autores.route('/actualizarautores', methods=['POST'] )
def actualizarautores():
    id = request.json['id']
    nombre = request.json['nombre']
    nacionalidad = request.json['nacionalidad']
    rautores = autores.query.get(id)
    rautores.autores = nombre
    rautores.autores = nacionalidad
    db.session.commit()
    return redirect('/autores')

@routes_autores.route('/saveautores', methods=['POST'] )
def guardar_autores():
    autor = request.json['nombre', 'nacionalidad']
    new_autor = autores(autor)
    db.session.add(new_autor)
    db.session.commit()
    return redirect('/autores')

