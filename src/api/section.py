from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma
from Model.section import Section, sectionSchema

routes_section = Blueprint("routes_section", __name__)

section_Schema = sectionSchema()
sections_Schema = sectionSchema(many=True)




@routes_section.route('/section', methods=['GET'])
def obtenersection():    
    returnall = Section.query.all()
    result_section = sections_Schema.dump(returnall)
    return jsonify(result_section)






#<--------------------------CRUD section--------------------------->
@routes_section.route('/eliminarsection/<id>', methods=['GET'] )
def eliminarsection(id):
    
    clear = Section.query.get(id)
    db.session.delete(clear)
    db.session.commit()
    return jsonify(section_Schema.dump(clear))

@routes_section.route('/actualizarsection', methods=['POST'] )
def actualizarsection():
    id = request.json['id']
    year = request.json['year']
    especialidad = request.json['especialidad']
    seccion = request.json['seccion']
    
    rsection = Section.query.get(id)
    rsection.section = year
    rsection.section = especialidad
    rsection.section = seccion

    db.session.commit()
    return redirect('/section')

@routes_section.route('/savesection', methods=['POST'] )
def guardar_section():
    seccion = request.json['year', 'especialidad', 'seccion']
    new_seccion = Section(seccion)
    db.session.add(new_seccion)
    db.session.commit()
    return redirect('/section')