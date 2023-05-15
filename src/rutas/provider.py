from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Proveedores import Proveedores
routes_provider = Blueprint("routes_provider", __name__)

@routes_provider.route('/indexprovider', methods=['GET'] )
def indexprovider():
    
    return render_template('/main/provider.html')

@routes_provider.route('/guardaradmin',methods=['POST'])
def saveprovider():
    #request.form['title']
    Nombre_proveedor = request.form['Nombre_proveedor']
    Telefono = request.form['Telefono']
    Direccion = request.form['Direccion']
    Descripcion = request.form['Descripcion']
    print(Nombre_proveedor,Telefono,Direccion,Descripcion)
    
    new_provider = Proveedores(Nombre_proveedor,Telefono,Direccion,Descripcion)
    db.session.add(new_provider)
    db.session.commit()
    return Nombre_proveedor,Telefono,Direccion,Descripcion
