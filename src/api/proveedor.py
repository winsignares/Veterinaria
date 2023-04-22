from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Proveedores  import Proveedores, ProveedoresSchema

routes_proveedores = Blueprint("routes_proveedor", __name__)

#Proveedores
Proveedor_schema = ProveedoresSchema()
Proveedores_schema = ProveedoresSchema(many=True)

#metodos para Proveedores inicio
#---------SAVE/CREAR------------
@routes_proveedores.route('/saveProveedores', methods=['POST'])
def guardar_Proveedores():    
    newProveedores = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    new_pro = Proveedores(newProveedores)
    db.session.add(new_pro)
    db.session.commit()
    return redirect('/Proveedores')

@routes_proveedores.route('/Proveedores', methods=['GET'])
def obtenerproveedor():    
    returnall = Proveedores.query.all()
   
    resultado_Proveedores = ProveedoresSchema.dump(returnall)
    return jsonify(resultado_Proveedores)

@routes_proveedores.route('/eliminarProveedores/<id>', methods=['GET'] )
def eliminarP(id):
    prov = Proveedores.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(Proveedores_schema.dump(prov)) 

@routes_proveedores.route('/actualizarProveedores', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    prov = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Proveedores.query.get(id)
    pusuario.Nombre_proveedor = prov
    db.session.commit()
    return redirect('/Proveedores')
#metodos para Proveedores final 