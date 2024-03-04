from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos

consu = Blueprint("consu", __name__)
@consu.route("/consumo")
def consumo():
    return render_template("consumo.html")
@consu.route("/consumo/Crear_consumo",methods=['POST'])

def crear_consumo():
    try:
        variable=""
        idencliente=request.form['idcliente']
        idinstancia=request.form['idinstancia']
        tiempo=request.form['tiempo']
        fecha=request.form['fecha']
        for instancia in Instancias.query.all():
            if instancia.iden == idinstancia and instancia.idcliente==idencliente:
                consumo= Consumos(idencliente,idinstancia,tiempo,fecha)
                db.session.add(consumo)
                db.session.commit() 
                variable="El consumo se realizo de manera correcta"
                break
            else:
                variable="Error al realizar el consumo"
       
        return render_template("consumo.html",variable=variable)
    except:
        print("Error al crear el consumo")
   