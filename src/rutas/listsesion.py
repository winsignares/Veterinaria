from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.section import * 


routes_listsesion = Blueprint("routes_listsesion", __name__)

@routes_listsesion.route('/indexlistsesion', methods=['GET'] )
def indexlistsesion():
    
    return render_template('/main/listsection.html')


'''
@routes_listsesion.route('/listasection', methods=['GET'])
def viewlistcategory(id):
        idn = Section.query.get(id)
        nombre = Section.query.get('nombre')
        result_Categoria = sectionSchema.dump(returnall)
        return result_Categoria
'''

@routes_listsesion.route('/listasection', methods=['GET'])
def obtenersection():    
    returnall = Section.query.all()
    result_section = sectionSchema.dump(returnall)
    return jsonify(result_section)
