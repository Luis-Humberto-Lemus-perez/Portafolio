'''
from flask import Blueprint, render_template, request



#from app import db
from models.productos import Productos

raiz= Blueprint('raiz', __name__)
producto:Productos
'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.productos import Productos
from utils.db import db
from tkinter import filedialog
from werkzeug.utils import secure_filename
from importlib.resources import path
from metodos import *
producto:Productos
metodo=Metodos
lista_recursos=[]
lista_categoria=[]
lista_clientes=[]
lista_consumo=[]


raiz = Blueprint("raiz", __name__)
@raiz.route('/')
def home():
    return render_template('index.html')
@raiz.route("/Configuracion",methods=['POST'])
def configuracion():
    perfil = request.files["confi"]
    filename= secure_filename(perfil.filename)
    perfil.save(path('BaseDatos',filename))
    file = filedialog.askopenfilename(title="abrir configuracion", filetypes=(("xml files","*.xml"),("all files", "*.*")))
    ruta=file
    
    metodo.leer_xmlconfiguracion(lista_recursos,ruta,lista_categoria,lista_clientes)
    consumo = request.files["consumo"]
    filename1= secure_filename(consumo.filename)
    consumo.save(path('BaseDatos',filename1))
    file1 = filedialog.askopenfilename(title="abrir consumos", filetypes=(("xml files","*.xml"),("all files", "*.*")))
    ruta=file1
    metodo.leer_xmlconfiguracion_consumo(lista_consumo,ruta)
    return render_template('index.html', respuesta1="el archivo de configuracion se envio correctamente", respuesta2="El mensaje de consumo se envio correctamente")
@raiz.route("/Guardar",methods=['POST'])
def guardar():
    metodo.basedatosrecurso(lista_recursos)
    metodo.basedatosConsumo(lista_consumo)
    metodo.basedatosCategoria(lista_categoria)
    metodo.basedatosClientes(lista_clientes)
    #for recurso in lista_recursos:
        #producto=Productos(recurso.iden,recurso.nombre,recurso.abrebiatura,recurso.metrica,recurso.tipo,recurso.valor_hora)

    return render_template('index.html',variable=" Se guardo la informacion de manera correcta")
@raiz.route("/deuda",methods=['POST'])
def deu():
    producto=Productos.query.all()
    clientes=Clientes.query.all()
    consumo=Consumos.query.all()
    categoria=Categorias.query.all()
    instancia=Instancias.query.all()
    pedido= Pedido.query.all()
    confi=Confi.query.all()


    metodo.generar_deudabasedatos(producto,clientes,consumo,categoria,instancia,pedido,confi)  
    #metodo.generar_deuda(lista_clientes,lista_recursos,lista_categoria,lista_consumo)
    
    return render_template('index.html',variable1="Datos agregados") 
@raiz.route("/ayuda",methods=['POST'])
def ayuda():
    try:
       
        return render_template("index.html", datos="Nombre:   Luis Humberto Lemus Perez"+"\n"+"Carnet:       201445840"+"\n"+"Introduccion a la programcion y computacion 2"+"\n"+"Seccion:   D"+"\n"+"Proyecto 3"  )
    except:
        print("error")
