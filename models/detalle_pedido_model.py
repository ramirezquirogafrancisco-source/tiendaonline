from config import get_db_connection


class DetallePedidoModel:

    @staticmethod
    def obtener_todos():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalle_pedidos")
        detalles = cursor.fetchall()
        cursor.close()
        connection.close()
        return detalles

    @staticmethod
    def obtener_por_id(id_detalle):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM detalle_pedidos WHERE id_detalle = %s",
            (id_detalle,),
        )
        detalle = cursor.fetchone()
        cursor.close()
        connection.close()
        return detalle

    @staticmethod
    def crear(id_pedido, id_producto, precio_unitario):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO detalle_pedidos "
            "(id_pedido, ID_producto, precio_unitario) "
            "VALUES (%s, %s, %s)",
            (id_pedido, id_producto, precio_unitario),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def actualizar(id_detalle, id_pedido, id_producto, precio_unitario):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE detalle_pedidos "
            "SET id_pedido = %s, ID_producto = %s, precio_unitario = %s "
            "WHERE id_detalle = %s",
            (id_pedido, id_producto, precio_unitario, id_detalle),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def eliminar(id_detalle):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM detalle_pedidos WHERE id_detalle = %s",
            (id_detalle,),
        )
        connection.commit()
        cursor.close()
        connection.close()