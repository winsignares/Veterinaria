from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_PresPendientes = Blueprint("routes_PresPendientes", __name__)



@routes_PresPendientes.route('/indexPresPendientes', methods=['GET'] )
def indexPresPendientes():
    
    return render_template('/main/loanpending.html')