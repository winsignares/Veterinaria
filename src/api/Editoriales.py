from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Editoriales import Editoriales,EditorialesSchema

routes_Editorial = Blueprint("routes_Editorial", __name__)

#editorial

editorial_Schema = EditorialesSchema()
editoriales_Schema = EditorialesSchema(many=True)

@routes_Editorial.route('/Editoriales', methods=['GET'])
def Editoriales():    
    returnall = Editoriales.query.all()
   
    result_Editoriales = EditorialesSchema.dump(returnall)
    return jsonify(result_Editoriales)