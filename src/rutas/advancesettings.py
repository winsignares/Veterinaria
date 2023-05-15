from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_advancesettings = Blueprint("routes_advancesettings", __name__)


@routes_advancesettings.route('/indexAsettings', methods=['GET'] )
def indexAsettings():
    
    return render_template('/main/advancesettings.html')