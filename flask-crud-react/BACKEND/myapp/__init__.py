from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
jwt = JWTManager()
jwt.init_app(app)

#Importar vistas 
@app.route('/')
def index():
    return 'Hola mundo'
from myapp.routes.auth import auth
app.register_blueprint(auth)
#db.create_all()