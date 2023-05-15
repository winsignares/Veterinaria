from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listprovider = Blueprint("routes_listprovider", __name__)


@routes_listprovider.route('/indexlistprovider', methods=['GET'] )
def indexlistprovider():
    
    return render_template('/main/listprovider.html')
