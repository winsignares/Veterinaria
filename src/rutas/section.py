from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.section import Section
routes_section = Blueprint("routes_section", __name__)


@routes_section.route('/indexsection', methods=['GET'] )
def indexsection():
    
    return render_template('/main/Section.html')



@routes_section.route('/guardarsection',methods=['POST'])
def saveSection():
    #request.form['title']
    year = request.form['year']
    especialidad = request.form['especialidad']
    seccion = request.form['seccion'] 
    print(year)
    new_section = Section(year, especialidad, seccion)
    db.session.add(new_section)
    db.session.commit()
    return "ok"


 
