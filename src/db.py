# db.py

import mysql.connector

def create_tables():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="baño"
    )
    cursor = connection.cursor()

    # Define la sentencia SQL para crear la tabla users
    create_users_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    '''


    # Ejecuta las sentencias SQL para crear las tablas
    cursor.execute(create_users_table_query)
    connection.commit()

    cursor.close()
    connection.close()
