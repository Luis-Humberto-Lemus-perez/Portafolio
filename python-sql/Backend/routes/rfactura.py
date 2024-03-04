from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos

fact = Blueprint("fact", __name__)
@fact.route("/factura")
def factura():
    return render_template("factura.html")
@fact.route("/factura/Crear_factura",methods=['POST'])

def crear_factura():
    try:
        variable=""
        variable1=""
        iden=request.form['id']
        factura=Factura.query.all()
        for cliente in Clientes.query.all():
            if cliente.iden == iden:
                
                variable1=metodo.Generar_factura(factura,iden)
                variable="Factura generada"
                break
            else:
                variable="El cliente no existe ingrese de nuevo"
        return render_template("factura.html" ,variable=variable, variable1=variable1)
    except:
        return render_template("factura.html" ,variable="Error al generar la factura")