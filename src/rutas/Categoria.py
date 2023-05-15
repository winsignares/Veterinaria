from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_categorias = Blueprint("routes_categorias", __name__)


@routes_categorias.route('/indexcategorias', methods=['GET'])
def indexcategorias():
    
    return render_template('/main/Categoria.html')