from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_personal = Blueprint("routes_personal", __name__)


@routes_personal.route('/indexpersonal', methods=['GET'] )
def indexpersonal():
    
    return render_template('/main/personal.html')
