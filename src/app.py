from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "prueba"

# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba"
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


@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
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
            session["user_id"] = user[0]  # Almacenar el ID del usuario en la sesión
            return redirect(url_for("profile"))
        else:
            # Si el usuario no existe o las credenciales son incorrectas, mostrar mensaje de error
            error_message = "Correo electrónico o contraseña incorrectos"
            return render_template("login.html", error_message=error_message)
    
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Insertar los datos del nuevo usuario en la base de datos
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        db.commit()
        
        # Después de registrar al nuevo usuario, iniciar sesión y redirigir al perfil
        session["user_id"] = cursor.lastrowid  # Almacenar el ID del nuevo usuario en la sesión
        return redirect(url_for("profile"))
    
    return render_template("register.html")


@app.route("/profile")

def profile():
    # Verificar si hay un usuario autenticado en la sesión
    if "user_id" in session:
        user_id = session["user_id"]
        
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



# Estas son las rutas de las tarjetas
@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@app.route('/Spa')
def Spa():
    return render_template("Spa.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")
# Hasta aqui las rutas de las tarjetas



@app.route("/logout")
def logout():
    # Eliminar el usuario de la sesión al cerrar sesión
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run()
