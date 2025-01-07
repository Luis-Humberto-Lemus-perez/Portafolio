from flask import (
    render_template,
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
    jsonify,
     session,
)
import functools
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    current_user,
    get_jwt_identity,
)
from werkzeug.security import check_password_hash, generate_password_hash
from myapp.models.user import User

from myapp import db

auth = Blueprint("auth", __name__)


# Registrar un usuario
@auth.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]

        user = User(username, generate_password_hash(password), 'user')

        error = None
        if not username:
            error = "Se requiere nombre de usuario"
        elif not password:
            error = "Se requiere contraseña"

        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "Usuario registrado correctamente"})
        else:
            error = f"El usuario {username} ya esta registrado"
            return jsonify({"error": error}), 401


@auth.route("/login", methods=("GET", "POST"))
def login():
    try:
    
   
        if request.method == "POST":
            username = request.json["username"]
            password = request.json["password"]

            error = None

            user = User.query.filter_by(username=username).first()

            if user == None:
                error = "Nombre de usuario incorrecto"
            elif not check_password_hash(user.password, password):
                error = "Contraseña incorrecta"

            if error is None:
                session.clear()
                session["user_id"] = user.id
                access_token = create_access_token(identity=user.username, additional_claims={"role": user.role})
                response = jsonify(
                    {
                        "message": "Logged In",
                        "username": user.username,
                        "role": user.role,   
                    }
                )
                response.set_cookie("token", access_token, httponly=True)
                return response
            
            return jsonify({"error": error}), 401
    except:
        return jsonify({"error": "Error al iniciar sesión"}), 405
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            print(g.user)
            return jsonify({"error": "Unauthorized"}), 401
        return view(**kwargs)
    return wrapped_view

@auth.route("/logout" )
@login_required
def logout():
    try:
        response = jsonify({"message": "Logged Out"})
        response.set_cookie("token", "", expires=0)
        return response

    except:
        return jsonify({"error": "Error al cerrar sesión"}), 405


