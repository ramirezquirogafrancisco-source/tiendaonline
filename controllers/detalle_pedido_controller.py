from flask import Blueprint, render_template, request, redirect, url_for

# Importar el modelo principal y los modelos relacionados
from models.detalle_pedido_model import DetallePedidoModel
from models.pedido_model import PedidoModel
from models.producto_model import ProductoModel

# Definir el Blueprint para detalle_pedidos
detalle_pedido_bp = Blueprint('detalle_pedidos', __name__)


# 1. LISTAR TODOS LOS DETALLES DE PEDIDOS
@detalle_pedido_bp.route('/detalle-pedidos', methods=['GET'])
def listar_detalles():
    lista_detalles = DetallePedidoModel.obtener_todos()
    return render_template('detalle_pedido/index.html', detalles=lista_detalles)


# 2. CREAR UN NUEVO DETALLE DE PEDIDO
@detalle_pedido_bp.route('/detalle-pedidos/crear', methods=['GET', 'POST'])
def crear_detalle():
    if request.method == 'POST':
        id_pedido = request.form.get('id_pedido')
        # Captura tanto 'ID_producto' como 'id_producto' por seguridad
        id_producto = request.form.get('ID_producto') or request.form.get('id_producto')
        precio_unitario = request.form.get('precio_unitario')

        DetallePedidoModel.crear(id_pedido, id_producto, precio_unitario)
        return redirect(url_for('detalle_pedidos.listar_detalles'))

    pedidos = PedidoModel.obtener_todos()
    productos = ProductoModel.obtener_todos()
    return render_template('detalle_pedido/crear.html', pedidos=pedidos, productos=productos)


# 3. EDITAR / ACTUALIZAR UN DETALLE DE PEDIDO
@detalle_pedido_bp.route('/detalle-pedidos/editar/<int:id_detalle>', methods=['GET', 'POST'])
def editar_detalle(id_detalle):
    if request.method == 'POST':
        id_pedido = request.form.get('id_pedido')
        id_producto = request.form.get('ID_producto') or request.form.get('id_producto')
        precio_unitario = request.form.get('precio_unitario')

        DetallePedidoModel.actualizar(id_detalle, id_pedido, id_producto, precio_unitario)
        return redirect(url_for('detalle_pedidos.listar_detalles'))

    detalle = DetallePedidoModel.obtener_por_id(id_detalle)
    pedidos = PedidoModel.obtener_todos()
    productos = ProductoModel.obtener_todos()
    return render_template('detalle_pedido/editar.html', detalle=detalle, pedidos=pedidos, productos=productos)


# 4. ELIMINAR UN DETALLE DE PEDIDO
@detalle_pedido_bp.route('/detalle-pedidos/eliminar/<int:id_detalle>', methods=['POST'])
def eliminar_detalle(id_detalle):
    DetallePedidoModel.eliminar(id_detalle)
    return redirect(url_for('detalle_pedidos.listar_detalles'))