from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_student = Blueprint("routes_student", __name__)



@routes_student.route('/indexstudent', methods=['GET'] )
def indexstudent():
    
    return render_template('/main/student.html')