from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_loan = Blueprint("routes_loan", __name__)



@routes_loan.route('/indexloan', methods=['GET'] )
def indexloan():
    
    return render_template('/main/loan.html')
