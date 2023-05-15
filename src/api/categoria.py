from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Categorias import Categorias, CategoriasSchema

routes_category = Blueprint("routes_categ", __name__)

#Categoria - Schema
Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)

@routes_category.route('/indexcategoria', methods=['GET'] )
def indexCategoria():
    
    return "Categoria || Hola Mundo!!"

#---------SAVE/CREAR------------
@routes_category.route('/savecategoria', methods=['POST'] )
def guardar_categoria():
    categori = request.json['N_cat']
    print(categori)
    new_Cat = Categorias(categori)
    db.session.add(new_Cat)
    db.session.commit()
    return redirect('/viewCategoria')
#------------View----------------
@routes_category.route('/viewCategoria', methods=['GET'])
def view_categoria():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = Categorias.query.all()    
        result_Categoria = CategoriasSchema.dump(returnall)
        return jsonify(result_Categoria)
    else:
        return vf
#-------Eliminar - Categoria-------
@routes_category.route('/clearCat', methods=['GET'] ) 
def eliminar_Cat(id):
    Cat = Categorias.query.get(id)
    db.session.delete(Cat)
    db.session.commit()
    return jsonify(CategoriasSchema.dump(Cat)) 

#-------Actualizar - Categoria------
@routes_category.route('/updateCat', methods=['POST'] )
def actualizar_Cat():
    id = request.json['id']
    N_cat = request.json['N_cat']
    Descripcion = request.json['Descripcion']
    updateCat = Categorias.query.get(id)
    updateCat.nameCat = N_cat
    updateCat.descripCat = Descripcion
    db.session.commit()
    return redirect('/Categorias')