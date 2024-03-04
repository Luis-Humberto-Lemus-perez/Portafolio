from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos
re = Blueprint("re", __name__)
@re.route("/reporte")
def reporte():
    var1=""
    var2=""
    #var1=metodo.reporte_categoria(lista_clientes)
    #var2=metodo.reporte_recursos(lista_clientes,lista_categoria,lista_recursos)
    return render_template("reporte.html", variable1=var1, variable2=var2)