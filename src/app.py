from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import mysql.connector
from datetime import datetime, timedelta
import bcrypt
from itsdangerous import URLSafeTimedSerializer
import random
import string
import uuid
from flask import flash


app = Flask(__name__)
app.secret_key = "prueba"

# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="baño"
)


##### CREACIÓN DE LAS TABLAS AL INICIAR APP.PY ##########


# Creación de la tabla de usuarios al iniciar la aplicación
cursor = db.cursor()
cursor.execute("""
               
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        registration_date DATETIME NOT NULL
    )
""")
db.commit()

# Creación de la tabla de mascotas al iniciar la aplicación

cursor.execute("""
               
    CREATE TABLE IF NOT EXISTS pets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        pet_name VARCHAR(255) NOT NULL,
        especie VARCHAR(255) NOT NULL,
        raza VARCHAR(255) NOT NULL,
        edad INT NOT NULL,
        registration_date DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
db.commit()


# Creación de la tabla de contacto al iniciar la aplicación
cursor.execute("""
               
        CREATE TABLE IF NOT EXISTS contacto (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            mensaje TEXT NOT NULL,
            registration_date DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
db.commit()

# Creación de la tabla de ventas al iniciar la aplicación
cursor.execute("""

        CREATE TABLE IF NOT EXISTS ventas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            descripcion_paquete VARCHAR(255) NOT NULL,
            valor DECIMAL(10, 2) NOT NULL,
            registration_date DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")


db.commit()

    ##### HASTA AQUÍ LA CREACIÓN DE LAS TABLAS AL INICIAR APP.PY ##########

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
        return redirect(url_for("login"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Realizar consulta a la base de datos para obtener el hash de la contraseña del usuario
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            # Verificar el hash de la contraseña almacenada con la contraseña proporcionada
            if bcrypt.checkpw(password.encode("utf-8"), user[2].encode("utf-8")):
                # Contraseña válida, iniciar sesión y redirigir al perfil
                user_obj = User(user[0])
                login_user(user_obj)
                return redirect(url_for("inicio"))

        # Si el usuario no existe o las credenciales son incorrectas, mostrar mensaje de error
        error_message = "Correo electrónico o contraseña incorrectos"
        return render_template("login.html", error_message=error_message)

    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("login"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Verificar si el usuario ya está registrado en la base de datos
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            # El usuario ya está registrado, mostrar mensaje de alerta
            flash("El usuario ya está registrado", "warning")
            return render_template("register.html")

        # Generar el hash y salting de la contraseña
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Obtener la fecha y hora actual
        current_date = datetime.now()

        # Insertar los datos del nuevo usuario y el hash de la contraseña en la base de datos
        cursor.execute("INSERT INTO users (email, password, registration_date) VALUES (%s, %s, %s)", (email, password_hash, current_date))
        db.commit()

        # Mostrar mensaje de éxito
        flash("Usuario registrado exitosamente", "success")
        return render_template("register.html")

    return render_template("register.html")


# Esto aquí es para que el usuario no haga trampa en el login e inicio
@app.after_request
def add_cache_control(response):
    # Agregar encabezados de respuesta para evitar el almacenamiento en caché
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

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



# Este es el resto de las rutas y sus funciones ...

@app.route("/logout")
@login_required
def logout():
    # Cerrar sesión y redirigir al inicio de sesión
    logout_user()
    response = make_response(redirect(url_for("login")))
    response.delete_cookie("")  # Cookie a eliminar
    return response

@app.route('/nosotros')
@login_required
def nosotros():
    return render_template("nosotros.html")

@app.route('/Spa')
@login_required
def Spa():
    return render_template("Spa.html")

@app.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mensaje = request.form.get('mensaje')

        # Obtener el ID del usuario actualmente autenticado
        user_id = current_user.id


        # Obtener la fecha y hora actual
        current_date = datetime.now()

        
        # Insertar los datos en la tabla 'contacto' junto con el ID del usuario
        cursor = db.cursor()
        query = 'INSERT INTO contacto (user_id, nombre, mensaje, registration_date) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (user_id, nombre, mensaje, current_date))
        db.commit()

        # Mostrar mensaje de éxito
        flash('Mensaje enviado exitosamente', 'success')
        return redirect(url_for('contacto'))

    return render_template('contacto.html')


@app.route('/galeria')
@login_required
def galeria():
    return render_template("galeria.html")


from datetime import datetime, timedelta

# Registrar mascotaaaaaaa

@app.route("/register_pet", methods=["GET", "POST"])
@login_required
def register_pet():
    if request.method == "POST":
        pet_name = request.form.get("nombre")
        especie = request.form.get("especie")
        raza = request.form.get("raza")
        edad = request.form.get("edad")

        # Obtener el ID del usuario actualmente autenticado
        user_id = current_user.id

        # Obtener la fecha y hora actual
        current_date = datetime.now()

        # Verificar si ya existe una mascota registrada con el mismo nombre en la última hora
        cursor = db.cursor()
        query = "SELECT registration_date FROM pets WHERE user_id = %s AND pet_name = %s ORDER BY registration_date DESC LIMIT 1"
        cursor.execute(query, (user_id, pet_name))
        existing_pet = cursor.fetchone()

        if existing_pet:
            # Calcular la diferencia de tiempo entre el último registro y la hora actual
            time_difference = current_date - existing_pet[0]
            time_difference_minutes = int(time_difference.total_seconds() / 60)

            if time_difference_minutes < 60:
                # Calcular el tiempo restante en minutos
                remaining_time_minutes = 60 - time_difference_minutes

                # Mostrar un mensaje de alerta con el tiempo restante en minutos
                flash(f"No puedes registrar a {pet_name} nuevamente hasta dentro de {remaining_time_minutes} minutos.", "warning")
                return redirect(url_for("register_pet"))

        # Insertar los datos de la mascota en la base de datos
        query = "INSERT INTO pets (user_id, pet_name, especie, raza, edad, registration_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (user_id, pet_name, especie, raza, edad, current_date))
        db.commit()

        # Mostrar mensaje de éxito
        flash("Mascota registrada exitosamente", "success")
        return redirect(url_for("register_pet"))

    return render_template("register_pet.html")



#Esta es la ruta de lo que se muestra despues del pago


@app.route('/pagoexitoso')
@login_required
def pagoexitoso():
    # Obtener el ID del usuario actualmente autenticado
    user_id = current_user.id
    
    # Obtener la fecha y hora actual
    current_date = datetime.now()
    
    # Definir la descripción del paquete y su valor
    descripcion_paquete = "Paquete básico"
    valor = 27000
    
    # Insertar el registro en la base de datos
    cursor = db.cursor()
    query = "INSERT INTO ventas (user_id, descripcion_paquete, valor, registration_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, descripcion_paquete, valor, current_date))
    db.commit()
    
    return render_template("pagoexitoso.html")

@app.route('/pagoexitoso2')
@login_required
def pagoexitoso2():
    # Obtener el ID del usuario actualmente autenticado
    user_id = current_user.id
    
    # Obtener la fecha y hora actual
    current_date = datetime.now()
    
    # Definir la descripción del paquete y su valor
    descripcion_paquete = "Paquete Premium"
    valor = 50000
    
    # Insertar el registro en la base de datos
    cursor = db.cursor()
    query = "INSERT INTO ventas (user_id, descripcion_paquete, valor, registration_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, descripcion_paquete, valor, current_date))
    db.commit()
    
    return render_template("pagoexitoso2.html")

@app.route('/timeline')
@login_required
def timeline():
    return render_template("timeline.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)