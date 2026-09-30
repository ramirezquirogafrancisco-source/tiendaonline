from config import get_db_connection


class ProductoModel:

    @staticmethod
    def obtener_todos():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        connection.close()
        return productos

    @staticmethod
    def obtener_por_id(id_producto):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM productos WHERE ID_producto = %s", (id_producto,)
        )
        producto = cursor.fetchone()
        cursor.close()
        connection.close()
        return producto

    @staticmethod
    def crear(nombre, precio, stock):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
            (nombre, precio, stock),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def actualizar(id_producto, nombre, precio, stock):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE"
            " ID_producto = %s",
            (nombre, precio, stock, id_producto),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def eliminar(id_producto):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM productos WHERE ID_producto = %s", (id_producto,)
        )
        connection.commit()
        cursor.close()
        connection.close()