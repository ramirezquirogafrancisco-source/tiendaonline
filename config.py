import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',             # Cambia si usas contraseña
        password='',
        database='tiendaonline'  # Tu base de datos
    )
    return connection