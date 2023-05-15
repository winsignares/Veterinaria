from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')