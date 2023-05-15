from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_institution = Blueprint("routes_institution", __name__)


@routes_institution.route('/indexinstitution', methods=['GET'] )
def indexinstitution():
    
    return render_template('/main/institurion.html')



@routes_institution.route('/guardarinstitution',methods=['POST'])
def saveinstitution():
    #request.form['title']

    #en el fullname va el dato de la db y en Roles de usuarios va la tbala donde se sacan los datos de la db
    fullname = request.form['fullname']
    nombre = request.form['nombre']
    distrito = request.form['distrito']
    telefono = request.form['telefono']
    año = request.form['año']
    print(fullname,nombre,distrito,telefono,año)
    new_rol = RolesUsuarios(fullname)
    db.session.add(new_rol)
    db.session.commit()
    return fullname