from utils.db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *

metodo=Metodos
global idencategoria
global idenconfi
idencategoria=""
idenconfi=""
cate = Blueprint("cate", __name__)
@cate.route("/categoria")

def categoria():
    return render_template("crearcategoria.html")
@cate.route("/categoria/Crear_categoria",methods=['POST'])
def crear_categoria():
    try:
        global idencategoria
        idencategoria=request.form['iden']
        nombre=request.form['nombre']
        descripcion=request.form['des']
        carga=request.form['carga']
        categoria1=Categorias(idencategoria,nombre,descripcion,carga)
        db.session.add(categoria1)
        db.session.commit()
        return redirect(url_for('cate.categoria'))



    except:
        print("HUbo un error el ingreso de categoria")
@cate.route("/categoria/Crear_configuracion",methods=['POST'])

def crear_configuracion():
    try:
        global idencategoria
        if idencategoria!=None:
            idenconfi=request.form['iden']
            nombre=request.form['nombre']
            descripcion=request.form['des']
            idrecurso=request.form['idrecu']
            cantidadrecurso=request.form['cantidad']

            confi=Confi(idencategoria, idenconfi,nombre,descripcion)
            db.session.add(confi)
            db.session.commit()
            for recu in Productos.query.all():
                if recu.idpro == idrecurso:
                
                    recurso=Pedido(idencategoria, idenconfi, idrecurso,cantidadrecurso)
                    db.session.add(recurso)
                    db.session.commit()
                    break
                
            return  redirect(url_for('cate.categoria'))



    except:
        print("HUbo un error el ingreso de categoria")  