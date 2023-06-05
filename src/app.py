from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "prueba"

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


# Lista para almacenar los mensajes del chat
chat_messages = []

# ESTAS SON LAS RUTAS

# ESTA ES LA RUTA COMPLETA PARA EL LOGIN

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
            return redirect(url_for("inicio"))
        else:
            # Si el usuario no existe o las credenciales son incorrectas, mostrar mensaje de error
            error_message = "Correo electrónico o contraseña incorrectos"
            return render_template("login.html", error_message=error_message)
    
    return render_template("login.html")

# HASTA AQUÍ ES LA RUTA COMPLETA PARA EL LOGIN

# ESTA ES LA RUTA COMPLETA PARA EL REGISTRO DEL USUARIO


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Insertar los datos del nuevo usuario en la base de datos
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        db.commit()
        
        # # Después de registrar al nuevo usuario, redirigir al inicio de sesión
        # return redirect(url_for("login"))
        
        # Mostrar mensaje de éxito
        success_message = "Usuario registrado exitosamente"
        return render_template("register.html", success_message=success_message)
    else:
            # El registro no fue exitoso
            error_message = "No se pudo registrar el usuario"
            return render_template("register.html", error_message=error_message)
    


# HASTA AQUÍ ES LA RUTA COMPLETA PARA EL REGISTRO DEL USUARIO

# ESTAS SON LAS RUTAS COMPLEMENTARIAS DE LA PAGINA BAÑO HUELLAS


# Esta es la ruta para verificar si el usuario existe


@app.route("/inicio")

def inicio():
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


# Hasta aquí es la ruta para verificar si el usuario existe

# Esta es la ruta para el almacenamiento de mensajes en el chat

@app.route('/save_message', methods=['POST'])
def save_message():
    message = request.form.get('message')
    
    # Agregar el mensaje a la lista de mensajes del chat
    chat_messages.append(message)

    # Realizar alguna lógica o procesamiento adicional con el mensaje si es necesario
    
    # Generar una respuesta del bot
    bot_response = generate_bot_response(message)
    
    # Agregar la respuesta del bot a la lista de mensajes del chat
    chat_messages.append(bot_response)

    # Retornar la respuesta como una estructura de datos JSON
    return jsonify({'message': bot_response})

def generate_bot_response(message):
    # Aquí puedes agregar la lógica para generar la respuesta del bot
    # Puedes utilizar el modelo de lenguaje GPT-3.5 u otros métodos

    # Ejemplo: simplemente retornar el mensaje del usuario invertido
    return message[::-1]

# Hasta aquí llega la ruta del chat


# AQUÍ TENGO QUE HACER LAS SECCIONES PARA BLOQUEAR LA FILTRACIÓN DE LOS USUARIOS POR MEDIO DEL URL O LOS BOTONES DE NAVEGACIÓN

# Esta es la ruta para bloquear el usuario


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

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")
# Hasta aqui las rutas de las tarjetas



@app.route("/logout")
def logout():
    # Eliminar el usuario de la sesión al cerrar sesión
    session.pop("user_id", None)
    return redirect(url_for("login"))


# HASTA AQUÍ LLEGAN LAS RUTAS


# INCIAR SERVIDOR

if __name__ == "__main__":
    app.run()
