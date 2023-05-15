from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listadmin = Blueprint("routes_listadmin ", __name__)



@routes_listadmin.route('/indexlistadmin', methods=['GET'] )
def indexlistadmin():
    
    return render_template('/main/listadmin.html')