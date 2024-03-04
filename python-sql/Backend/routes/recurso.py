from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos



recurso = Blueprint("recurso", __name__)

@recurso.route("/recurso")
def recurso1():
    return render_template("crearrecurso.html")

@recurso.route("/recurso/Crear_recurso",methods=['POST'])
def crear_recurso(): 
    try:

                # receive data from the form
                iden = request.form['iden']
                nombre = request.form['nombre']
                abre = request.form['abre']
                metrica = request.form['metrica']
                tipo = request.form['tipo']
                hora = request.form['hora']

                # create a new Contact object
                new_contact = Productos(iden,nombre,abre,metrica,tipo,hora)

                # save the object into the database
                db.session.add(new_contact)
                db.session.commit()

               

                
                #flash('Product added successfully!')
                return redirect(url_for('resurso.recurso1'))
    except:
                
        
        print("Error en el recurso de base de datos")
        return recurso1()  
