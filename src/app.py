from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import mysql.connector

app = Flask(__name__)
app.secret_key = "prueba"

login_manager = LoginManager(app)
login_manager.login_view = "login"


# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="baño"
)

# Creación de la tabla de usuarios al iniciar la aplicación
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")
db.commit()

# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"


# Definición de la clase User para Flask-Login
class User:
    def __init__(self, user_id):
        self.id = user_id
        self.is_active = True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    @staticmethod
    def get(user_id):
        # Obtener los datos del usuario desde la base de datos
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(user_data[0])
        return None


@login_manager.user_loader
def load_user(user_id):
    # Cargar el usuario a partir de su ID almacenado en la sesión
    return User.get(user_id)


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Realizar consulta a la base de datos para validar el usuario
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        if user:
            # Si el usuario existe en la base de datos, iniciar sesión y redirigir al perfil
            user_obj = User(user[0])
            login_user(user_obj)
            return redirect(url_for("inicio"))
        else:
            # Si el usuario no existe o las credenciales son incorrectas, mostrar mensaje de error
            error_message = "Correo electrónico o contraseña incorrectos"
            return render_template("login.html", error_message=error_message)

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Insertar los datos del nuevo usuario en la base de datos
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        db.commit()

        # Mostrar mensaje de éxito
        success_message = "Usuario registrado exitosamente"
        return render_template("register.html", success_message=success_message)
    else:
        # El registro no fue exitoso
        error_message = "No se pudo registrar el usuario"
        return render_template("register.html", error_message=error_message)


@app.route("/inicio")
@login_required
def inicio():
    # Verificar si hay un usuario autenticado en la sesión
    user_id = current_user.id

    # Consultar los datos del usuario desde la base de datos
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    if user:
        # Si el usuario existe, mostrar la página de perfil con los datos del usuario
        return render_template("index.html", user=user)

    # Si no hay un usuario autenticado en la sesión, redirigir al inicio de sesión
    return redirect(url_for("login"))


@app.after_request
def add_cache_control(response):
    # Agregar encabezados de respuesta para evitar el almacenamiento en caché
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route("/logout")
@login_required
def logout():
    # Cerrar sesión y redirigir al inicio de sesión
    logout_user()
    response = make_response(redirect(url_for("login")))
    response.delete_cookie("tidio")  # Suponiendo que "tidio" es el nombre de la cookie a eliminar
    return response


@app.route('/nosotros')
@login_required
def nosotros():
    return render_template("nosotros.html")


@app.route('/Spa')
@login_required
def Spa():
    return render_template("Spa.html")


@app.route('/contacto')
@login_required
def contacto():
    return render_template("contacto.html")


@app.route('/galeria')
@login_required
def galeria():
    return render_template("galeria.html")


if __name__ == "__main__":
    app.run()
