from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listteacher = Blueprint("routes_listteacher", __name__)


@routes_listteacher.route('/indexlistteacher', methods=['GET'] )
def indexlistteacher():
    
    return render_template('/main/listteacher.html')