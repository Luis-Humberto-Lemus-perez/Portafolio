from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos



consultaDatos = Blueprint("consultaDatos", __name__)

@consultaDatos.route("/Consultar_Datos")
def Consultar_Datos():
    producto=Productos.query.all()
    clientes=Clientes.query.all()
    consumo=Consumos.query.all()
    categoria=Categorias.query.all()
    instancia=Instancias.query.all()
    pedido= Pedido.query.all()
    confi=Confi.query.all()
    factura=Factura.query.all()
    variable=""
    variable=metodo.mostrar_sistema(producto,categoria,clientes,instancia,confi,pedido)
   
  
    return render_template("consulta.html",variable=variable) 