from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from utils.db import db
from models.ModelProduct import ModelProduct
from models.entities.Product import Product
from flask_login import login_required

crud = Blueprint("crud", __name__)


@crud.route("/admin")
@login_required
def mostrar():
    productos = ModelProduct.listar(db)

    return render_template("home.html", articulos=productos)


@crud.route("/admin/crear", methods=["POST"])
@login_required
def crear_producto():
    try:
        if request.method == "POST":
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            cantidad = request.form["cantidad"]
            precio = request.form["precio"]
           
            variable = ModelProduct.crear(db, codigo, nombre, cantidad, precio)
            
            productos = ModelProduct.listar(db)

            flash(variable)
            return render_template("home.html", articulos=productos)

    except Exception as e:
        flash(e.args[1])
        
        return redirect(url_for("crud.mostrar"))
    
@crud.route("/admin/delete/<int:id>")
@login_required
def delete(id):
    try:
        variable=ModelProduct.delete(db, id)
        flash(variable)
        return redirect(url_for("crud.mostrar"))    
    except Exception as e:
        flash(e.args[1])
        return redirect(url_for("crud.mostrar"))

@crud.route("/admin/edit/<int:id>", methods=['POST', 'GET'])
@login_required
def edit(id):
    
    productos = ModelProduct.get_by_id(db, id)
   
    return render_template("editar.html", product=productos)

@crud.route("/admin/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    try:
        
        
        if request.method == "POST":
            
            codigo = request.form["codigo"]
            nombre = request.form["nombre"]
            cantidad = request.form["cantidad"]
            precio = request.form["precio"]
            
            variable = ModelProduct.update(db, id, codigo, nombre, cantidad, precio)
            flash(variable)
            return redirect(url_for("crud.mostrar")) 
    except Exception as e:
        flash("Error al actualizar")
        return redirect(url_for("crud.mostrar"))