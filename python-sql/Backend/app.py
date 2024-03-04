from flask import Flask
from routes.raiz import raiz
from routes.routecliente import client
from routes.rfactura import fact
from routes.rconsumo import consu
from routes.rreportes import re
from routes.consultaDatos import consultaDatos
from routes.catego import cate
from routes.recurso import recurso
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

#from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
#print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root@localhost/productosdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#SQLAlchemy(app)

app.register_blueprint(raiz)
app.register_blueprint(consultaDatos)
app.register_blueprint(recurso)
app.register_blueprint(cate)
app.register_blueprint(client)
app.register_blueprint(consu)
app.register_blueprint(fact)
app.register_blueprint(re)


