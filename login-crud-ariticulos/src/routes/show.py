from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from utils.db import db
from models.ModelProduct import ModelProduct

show = Blueprint("show", __name__)


@show.route("/articulos")
def ver():
    try:

        productos = ModelProduct.listar(db)
        print(productos[0].codigo)
        return render_template("articulos.html", articulos=productos)
    except Exception as ex:

        return render_template("articulos.html")
