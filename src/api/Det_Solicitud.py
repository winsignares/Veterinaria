from flask import Blueprint, request, jsonify, json
from Model.Det_Solicitud import Det_Solicitud, Det_SolicitudesSchema
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

routes_Dsolicitudes = Blueprint("routes_Dsolicitudes",__name__)

detalleSolicitud_schema= Det_SolicitudesSchema()
detalleSolicitudes_schema= Det_SolicitudesSchema(many=True)

@app.route('/eliminardet_solicitud/<id>', methods=['GET'] )
def eliminardetalles (id):
    DetSolicitud = Det_Solicitud.query.get(id)
    db.session.delete(Det_Solicitud)
    db.session.commit()
    return jsonify(detalleSolicitudes_schema.dump(Det_Solicitud))

@app.route('/savedet_solicitud', methods=['POST'] )
def guardar_detalles():
    DetSolicitud  = request.json['idlibros', 'idSolicitudes']
    print(Det_Solicitud)
    new_DSolicitud = Det_Solicitud(Det_Solicitud)
    db.session.add(new_DSolicitud)
    db.session.commit()
    return redirect('/det_solicitud')

@app.route('/actualizadet_solicitud', methods=['POST'] )
def actualizar_detalles():
    id = request.json['id']
    idlibros = request.json['idlibros']
    idSolicitudes = request.json['idSolicitudes']
    DetSolicitud  = Det_Solicitud.query.get(id)
    DetSolicitud.Det_Solicitud = idlibros
    DetSolicitud.Det_Solicitud = idSolicitudes
    db.session.commit()
    return redirect('/det_solicitud')