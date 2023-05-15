from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_loanreservation = Blueprint("routes_loanreservation", __name__)



@routes_loanreservation.route('/indexloanreservation', methods=['GET'] )
def indexloan():
    
    return render_template('/main/loanreservation.html')
