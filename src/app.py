#10.230.16.229
#10.230.16.238
#10.230.16.196

#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#from dotenv import load_dotenv

#importar routes
from api.user import routes_user
from api.roles import routes_roles
from api.categoria import routes_category
from api.autores import routes_autores
from api.proveedor import routes_proveedores
from api.Editoriales import routes_Editorial
from api.solicitudes import routes_solicitudes
from api.estadosoli import routes_stadosolicitud
from api.Libros import routes_Libros
from api.Det_Solicitud import routes_Dsolicitudes
from api.section import routes_section
#rutas

#Santiago
from rutas.home import routes_home
#luis
from rutas.advancesettings import routes_advancesettings
#dainer
from rutas.Admin import routes_Admin
#Gonzalo
from rutas.book import routes_book
#David
from rutas.catalogo import routes_catalogo
#Antonio
from rutas.Categoria import routes_categorias 
#Edwin
from rutas.institution import routes_institution
#Alejo
from rutas.listadmin import routes_listadmin 
#Alet
from rutas.listcategory import routes_listcategory
#Julieth
from rutas.list_personal import routes_listpersonal
#Wilches
from rutas.listprovider import routes_listprovider
#Benedetty
from rutas.listsesion import routes_listsesion
#Jasson
from rutas.liststudent import routes_liststudent
#Sthiwar
from rutas.loan import routes_loan
#Hader
from rutas.listteacher import routes_listteacher
#Jean
from rutas.loanpending import routes_PresPendientes
#Ivan
from rutas.personal import routes_personal
#Ivan villalobos
from rutas.loanreservation import routes_loanreservation
#Saray
from rutas.student import routes_student
#Camilo
from rutas.reports import routes_report
#Jonathan
from rutas.section import routes_section
#Jorge
from rutas.SearchBooks import routes_searchbooks 
from rutas.teacher import routes_teacher

#ubicacion del api 
app.register_blueprint(routes_stadosolicitud, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_Libros, url_prefix="/api")
app.register_blueprint(routes_autores,  url_prefix="/api")
app.register_blueprint(routes_Dsolicitudes, url_prefix="/api")
app.register_blueprint(routes_category, url_prefix="/api")
app.register_blueprint(routes_proveedores, url_prefix="/api")
app.register_blueprint(routes_Editorial, url_prefix="/api")
app.register_blueprint(routes_solicitudes, url_prefix="/api")

#ubicación rutas

#Santiago
app.register_blueprint(routes_home, url_prefix="/fronted")
#luis

#dainer
app.register_blueprint(routes_Admin, url_prefix="/fronted")
#Gonzalo
app.register_blueprint(routes_book, url_prefix="/fronted")
#David
app.register_blueprint(routes_catalogo, url_prefix="/fronted")
#Antonio
app.register_blueprint(routes_categorias, url_prefix="/fronted")
#Edwin
app.register_blueprint(routes_institution, url_prefix="/fronted")
#Alejo
app.register_blueprint(routes_listadmin, url_prefix="/fronted")
#Alet
app.register_blueprint(routes_listcategory, url_prefix="/fronted")
#Julieth
app.register_blueprint(routes_listpersonal, url_prefix="/fronted")
#Wilches
app.register_blueprint(routes_listprovider, url_prefix="/fronted")
#Benedetty
app.register_blueprint(routes_listsesion, url_prefix="/fronted")
#Jasson
app.register_blueprint(routes_liststudent, url_prefix="/fronted") 
#Sthiwar
app.register_blueprint(routes_loan, url_prefix="/fronted")
#Hader
app.register_blueprint(routes_listteacher, url_prefix="/fronted")
#Jean
app.register_blueprint(routes_PresPendientes, url_prefix="/fronted")
#Ivan
app.register_blueprint(routes_personal, url_prefix="/fronted")
#Ivan villalobos
app.register_blueprint(routes_loanreservation, url_prefix="/fronted")
#Saray
app.register_blueprint(routes_student, url_prefix="/fronted")
#Camilo
app.register_blueprint(routes_report, url_prefix="/fronted")
#Jonathan
app.register_blueprint(routes_section, url_prefix="/fronted") 
#Jorge
app.register_blueprint(routes_searchbooks, url_prefix="/fronted")
#Julieth
app.register_blueprint(routes_teacher, url_prefix="/fronted")

#------------------------------------------------
@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/login.html', titles=titulo)

@app.route("/algo")
def otr():
    return "hola Santiago"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


#<----------------------------------------------------------------->
'''
@app.route('/consultar3tabla', methods=['GET'])
def consultar3tablas():
    datos= {}
    resultado = db.session.query(Employee,Department, Company). \
        select_from(Employee).join(Department).join(Company).all()
    i=0
    for employee,department,company  in resultado:
        i+=1
        datos[i]={
           
                'Ename': employee.name,
                'Dname': department.name,
                'Cname': company.name          
        }
    print(datos)
    return "Algo"
'''