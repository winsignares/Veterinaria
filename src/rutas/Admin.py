from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.RolesUsuarios import RolesUsuarios
routes_Admin = Blueprint("routes_Admin", __name__)


@routes_Admin.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    
    return render_template('/main/Admin.html')

@routes_Admin.route('/guardaradmin',methods=['POST'])
def saveadmin():
    #request.form['title']
    fullname = request.form['fullname']
    print(fullname)
    new_rol = RolesUsuarios(fullname)
    db.session.add(new_rol)
    db.session.commit()
    return fullname

