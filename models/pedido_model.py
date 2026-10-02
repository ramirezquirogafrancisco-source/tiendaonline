from config import get_db_connection


class PedidoModel:

    @staticmethod
    def obtener_todos():
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()
        cursor.close()
        connection.close()
        return pedidos

    @staticmethod
    def obtener_por_id(id_pedido):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM pedidos WHERE id_pedido = %s", (id_pedido,)
        )
        pedido = cursor.fetchone()
        cursor.close()
        connection.close()
        return pedido

    @staticmethod
    def crear(id_cliente):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO pedidos (ID_cliente) VALUES (%s)",
            (id_cliente,),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def actualizar(id_pedido, id_cliente):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE pedidos SET ID_cliente = %s WHERE id_pedido = %s",
            (id_cliente, id_pedido),
        )
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def eliminar(id_pedido):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM pedidos WHERE id_pedido = %s", (id_pedido,)
        )
        connection.commit()
        cursor.close()
        connection.close()