from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users,UsuariosSchema

routes_user = Blueprint("routes_user", __name__)

#usuario
Usuario_Schema= UsuariosSchema()
Usuarios_Schema= UsuariosSchema(many=True)


@routes_user.route("/")
def index():
    return "index"

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Users.query.all()
   
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

#crud de usuarios
@app.route('/eliminar_Users/<id>', methods=['GET'] )
def eliminar_users(id):
    usuarios = Users.query.get(id)
    db.session.delete(usuarios)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(usuarios)) 

@app.route('/actualizarUsers', methods=['POST'] )
def actualizar_users():
    id = request.json['id']
    full_name = request.json['full_name']
    Email= request.json['Email']
    telefono= request.json['telefono']
    especialidad= request.json['especialidad']
    jornada= request.json['jornada']
    direccion= request.json['direccion']
    users= Users.query.get(id)
    users.full_name = full_name
    users.Email= Email
    users.telefono = telefono
    users.especialidad= especialidad
    users.jornada = jornada
    users.direccion= direccion
    db.session.commit()
    return redirect('/Usuarios')

@app.route('/save_Users', methods=['POST'] )
def guardar_Users():
    usuarios = request.json['full_name,Email,password,telefono,especialidad,jornada,direccion,id_roles']
    print(usuarios)
    new_Users = Users(usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')

@routes_user.route('/obtenerToken', methods=['GET'])
def obtenertoken():
    #var_request = json.loads(event["body"])   
    datatoken = generar_token("William", 123)
    var_Token = datatoken["token"]
    response = {"statusCode": 200, "body": json.dumps(var_Token)}    
    return response

@routes_user.route('/verificartoken', methods=['GET'])
def verificartoken():
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    print("token =>", token)
      # Call the function to validate token
    vf = verificar_token(token)
    print("vf =>", vf)
    return vf

@routes_user.route('/conlistpersonal', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(TblUsuarios, tblrolesusuarios). \
        select_from(TblUsuarios.Cedula, TblUsuarios.full_name, TblUsuarios.telefono, TblUsuarios.cargo, tblrolesusuarios.rol).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "personal").all()
    i=0
    for TblUsuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'DUI':TblUsuarios.Cedula,
		'Nombre':TblUsuarios.full_name,
		'Telefono':TblUsuarios.telefono,
		'Cargo': TblUsuarios.especialidad                      
        }
    print(datos)
    return datos


@routes_user.route('/conliststudiantes', methods=['GET'])
def consullist2():
    datos= {}
    resultado = db.session.query(TblUsuarios, tblrolesusuarios). \
        select_from(TblUsuarios.Cedula, TblUsuarios.full_name, TblUsuarios.jornada, tblrolesusuarios.rol).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "estudiante").all()
    i=0
    for TblUsuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'NIE':TblUsuarios.Cedula,
		'Nombre':TblUsuarios.full_name,
		'Jornada':TblUsuarios.jornada,                    
        }
    print(datos)
    return datos


