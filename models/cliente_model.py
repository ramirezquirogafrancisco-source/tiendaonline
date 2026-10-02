from config import get_db_connection


class ClienteModel:

    @staticmethod
    def obtener_todos():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        connection.close()
        return clientes

    @staticmethod
    def obtener_por_id(id_cliente):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM clientes WHERE ID_Cliente = %s", (id_cliente,)
        )
        cliente = cursor.fetchone()
        cursor.close()
        connection.close()
        return cliente

    @staticmethod
    def crear(nombre, email, telefono):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO clientes (Nombre, Email, Telefono) VALUES (%s, %s, %s)",
            (nombre, email, telefono),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def actualizar(id_cliente, nombre, email, telefono):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE clientes SET Nombre = %s, Email = %s, Telefono = %s "
            "WHERE ID_Cliente = %s",
            (nombre, email, telefono, id_cliente),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def eliminar(id_cliente):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM clientes WHERE ID_Cliente = %s", (id_cliente,)
        )
        connection.commit()
        cursor.close()
        connection.close()