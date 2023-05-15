from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_teacher = Blueprint("routes_teacher", __name__)

@routes_teacher.route('/indexteacher', methods=['GET'] )
def indexteacher():
    
    return render_template('/main/teacher.html')

@routes_teacher.route('/saveinstructor', methods=['POST'] )
def guardarinstru():
    full_name = request.json['full_name']
    Email = request.json['Email']
    telefono = request.json['telefono']
    especialidad = request.json['especialidad']
    jornada = request.json['jornada']
    direccion= request.json['direccion']
    print(full_name,Email,telefono,especialidad,jornada,direccion)
    new_Users = Users(full_name,Email,telefono,especialidad,jornada,direccion)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')