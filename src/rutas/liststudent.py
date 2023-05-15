from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_liststudent = Blueprint("routes_liststudent", __name__)

@routes_liststudent.route('/indexlist_student', methods=['GET'] )
def indexlist_student():
    
    return render_template('/main/liststudent.html')