from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Libros import Libros,LibrosSchema

routes_Libros = Blueprint("routes_Libros", __name__)

#libros

libro_schema = LibrosSchema()
libros_Schema = LibrosSchema(many=True)


@routes_Libros.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = libros_Schema.dump(returnall)
    return jsonify(resultado_libros)

@routes_Libros.route('/', methods=['POST'] )
def guardar_Libros():
    addlibros = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov']
    print(addlibros)
    new_libro = Libros(addlibros)
    db.session.add(new_libro)
    db.session.commit()
    return redirect('/libros')

@routes_Libros.route('/actualizarlibros', methods=['POST'] )
def actualizarL():

    id = request.json['id']
    libro = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion']
    nlibros = Libros.query.get(id)
    nlibros.libro = libro
    db.session.commit()
    return redirect('/libros')

@routes_Libros.route('/eliminarlibros/<id>', methods=['GET'] )
def eliminarL(id):

    libro = Libros.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify(libros_Schema.dump(libro)) 