from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users
routes_report= Blueprint("routes_report",__name__)

@routes_report.route('/indexreport', methods=['GET'])
def indexreport():
    return render_template('/main/report.html')



@app.route('/listreports', methods=['GET'])
def lista_reports():
    data={}
    result= db.session.query(TblUsuarios,tblrolesusuarios). \
        select_from(TblUsuarios.rol).join(tblrolesusuarios.roles).all()
    i=0
    for TblUsuarios,tblrolesusuarios in result:
        data[i]={
            'roles':TblUsuarios.rol
            
            
        } 
        print(data)
        return data