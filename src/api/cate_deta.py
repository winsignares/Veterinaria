from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Cate_deta import cate_deta, cate_detaSchema

routes_Catego_deta = Blueprint("routes_Catego_deta", __name__)

categoria_detaSchema = cate_detaSchema()
categorias_detaSchema = cate_detaSchema(many=True)

#Datos de la tabla Datos de categorias
@app.route('/cate_deta', methods=['GET'])
def category():    
    returnall = cate_deta.query.all()
    result_cate_deta = categorias_detaSchema.dump(returnall)
    return jsonify(result_cate_deta)

#guardar detalles de categorias 
@app.route('/savedeta_cate', methods=['POST'])
def guardar_C_D():
    cate_deta = request.json['id_cate', 'id_li' ]
    print(cate_deta)
    new_cate_deta = cate_deta(cate_deta)
    db.session.add(new_cate_deta)
    db.session.commit()
    return redirect('/savecatedeta')
#Eliminar   detalles de categorias
@app.route('/deletecate_deta/<id>', methods=['GET'] )
def eliminarC_D(id):
    cate_deta = cate_deta.query.get(id)
    db.session.delete(cate_deta)
    db.session.commit()
    return jsonify(cate_detaSchema.dump(cate_deta)) 
#Actualizar 
@app.route('/updatecate_deta', methods=['POST'] )
def actualizarC_D():
    id = request.json['id']
    cate_deta = request.json['id_cate','id_li']
    pcate_deta = cate_deta.query.get(id)
    pcate_deta.cantidad = cate_deta
    db.session.commit()
    return redirect('/updatecate_deta')
