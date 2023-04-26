from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.estadosolicitud import estadosolicitud, estadoSchema

routes_stadosolicitud = Blueprint("routes_stadosolicitud", __name__)

#Roles
Estado_schema = estadoSchema()
Estados_schema = estadoSchema(many=True)

@routes_stadosolicitud.route("/")
def stadosolicitudes():
    return "stadosolicitudes"


#Roles
#---------SAVE/CREAR------------
@routes_stadosolicitud.route('/stadosolicitudes', methods=['GET'])
def crear_stadosolicitudes():
    returnall = stadosolicitudes.query.all()
    resultado_stadosolicitudes = estadoSchema.dump(returnall)
    return jsonify(resultado_stadosolicitudes)


@routes_stadosolicitud.route('/saveestadosolicitud', methods=['POST'] )
def guardar_estadosolicitud():
    fecha = request.json['fecha']
    id_solicitud = request.json['id_solicitud']
    fecha_devolucion = request.json['fecha_devolucion']
    dias_atraso = request.json['dias_atraso']
    estado = request.json['estado']
    print(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado)
    new_estadosolicitud = estadosolicitud(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado)
    db.session.add(new_estadosolicitud)
    db.session.commit()
    return redirect('/estadosolicitud')

# eliminar
@routes_stadosolicitud.route('/eliminarestadosolicitud/<id>', methods=['GET'] )
def eliminaestadosoli(id):
    fecha = estadosolicitud.query.get(id)
    id_solicitud = estadosolicitud.query.get(id)
    fecha_devolucion = estadosolicitud.query.get(id)
    dias_atraso = estadosolicitud.query.get(id)
    estado = estadosolicitud.query.get(id)
    
    db.session.delete(fecha,id_solicitud,fecha_devolucion, dias_atraso,estado)
    db.session.commit()
    return jsonify(estadoSchema.dump(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado))

# actualizar
@routes_stadosolicitud.route('/actualizar_estadosolicitud', methods=['POST'] )
def actualizar_estadosolicitud():
    id = request.json['id']
    fechas = request.json['fechas']
    id_solicitudes = request.json['id_solicitud']
    fecha_devoluciones = request.json['fecha_devolucion']
    dias_atrasos = request.json['dias_atraso']
    estados = request.json['estado']
    
    estadosolicitud = estadosolicitud.query.get(id)
    estadosolicitud.fechas = fechas 
    estadosolicitud.id_solicitudes = id_solicitudes
    estadosolicitud.fecha_devolucion = fecha_devoluciones
    estadosolicitud.dias_atraso = dias_atrasos  
    estadosolicitud.estado = estados
    db.session.commit()
    return redirect('/estadosolicitud')

