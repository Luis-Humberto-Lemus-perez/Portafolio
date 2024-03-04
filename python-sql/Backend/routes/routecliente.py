from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos
global idencliente
idencliente=""
client = Blueprint("client", __name__)
@client.route("/cliente")

def cliente():
    return render_template("crearcliente.html")
@client.route("/cliente/Crear_cliente",methods=['POST'])
def crear_cliente():
    try:
        global idencliente
   
        idencliente=request.form['iden']
        nombre=request.form['nombre']
        usuario=request.form['us']
        clave=request.form['clave']
        direc=request.form['direc']
        correo=request.form['correo']
        cliente1=Clientes(idencliente,nombre,usuario,clave,direc,correo,0)
        db.session.add(cliente1)
        db.session.commit()
        return redirect(url_for('client.cliente'))
    except:
        print("Error al crear el cliente")
@client.route("/cliente/Crear_instancia",methods=['POST'])

def crear_instancia():
    try:
        global idencliente
        var1=""
        iden=request.form['iden']
        idconfi=request.form['idconfi']
        nombre=request.form['nombre']
        fechainicio=request.form['fechainicio']
        estado=request.form['estado']
        fechafinal=request.form['fechafinal']
        for confi in Confi.query.all():
            if confi.iden == idconfi:
                instancia=Instancias(idencliente, iden,idconfi,nombre,fechainicio,estado,fechafinal)
                db.session.add(instancia)
                db.session.commit()
                break
        return redirect(url_for('client.cliente'))
        
    except:
        print("Error al crear la instancia")