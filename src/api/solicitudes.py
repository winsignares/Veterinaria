from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from Model.Solicitudes import Solicitudes, SolicitudesSchema

routes_solicitudes = Blueprint("routes_solicitud", __name__)

solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)

#metodo para solicitudes
@app.route('/solicitudes', methods=['GET'])
def solicitudes():
    returnall = Solicitudes.query.all()
    resultado_solicitudes = solicitudes_schema.dump(returnall)
    return jsonify(resultado_solicitudes)
#guardar solicitudes 
@app.route('/savesolicitudes', methods=['POST'])
def guardar_solicitudes():
    solicitudes = request.json['fecha_solicitud', 'cantidad','Id_usu' ]
    print(solicitudes)
    new_soli = Solicitudes(solicitudes)
    db.session.add(new_soli)
    db.session.commit()
    return redirect('/savesolicitudes')
#Eliminar   solicitudes
@app.route('/deletesolicitudes', methods=['GET'] )
def eliminarD():
    solicitudes = Solicitudes.query.get(all)
    db.session.delete(solicitudes)
    db.session.commit()
    return jsonify(solicitudes_schema.dump(solicitudes)) 
#Actualizar Solicitudes
@app.route('/updatesolicitudes', methods=['POST'] )
def actualizarS():
    id = request.json['id']
    solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Solicitudes.query.get(id)
    pusuario.cantidad = solicitudes
    db.session.commit()
    return redirect('/updatesolicitudes')



    