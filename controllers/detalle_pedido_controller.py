from flask import Blueprint, render_template, request, redirect, url_for

# Importar el modelo principal y los modelos relacionados para los formularios
from models.detalle_pedido_model import DetallePedidoModel

# Definir el Blueprint para detalle_pedidos[cite: 2]
detalle_pedido_bp = Blueprint('detalle_pedidos', __name__)


# 1. LISTAR TODOS LOS DETALLES DE PEDIDOS[cite: 2]
@detalle_pedido_bp.route('/detalle-pedidos', methods=['GET'])
def listar_detalles():
    # Obtener la lista completa desde el modelo[cite: 2]
    lista_detalles = DetallePedidoModel.obtener_todos()
    return render_template('detalle_pedidos/index.html', detalles=lista_detalles)[cite: 2]


# 2. CREAR UN NUEVO DETALLE DE PEDIDO[cite: 2]
@detalle_pedido_bp.route('/detalle-pedidos/crear', methods=['GET', 'POST'])
def crear_detalle():
    if request.method == 'POST':
        id_pedido = request.form.get('id_pedido')
        id_producto = request.form.get('id_producto')
        precio_unitario = request.form.get('precio_unitario')

        # Guardar mediante el modelo con los métodos exactos de tu compañero[cite: 2]
        DetallePedidoModel.crear(id_pedido, id_producto, precio_unitario)[cite: 2]
        return redirect(url_for('detalle_pedidos.listar_detalles'))

    # Para el método GET, traemos pedidos y productos para los desplegables (<select>)[cite: 2]
    pedidos = PedidoModel.obtener_todos()[cite: 2]
    productos = ProductoModel.obtener_todos()[cite: 2]
    return render_template('detalle_pedidos/crear.html', pedidos=pedidos, productos=productos)[cite: 2]


# 3. EDITAR / ACTUALIZAR UN DETALLE DE PEDIDO[cite: 2]
@detalle_pedido_bp.route('/detalle-pedidos/editar/<int:id_detalle>', methods=['GET', 'POST'])
def editar_detalle(id_detalle):
    if request.method == 'POST':
        id_pedido = request.form.get('id_pedido')
        id_producto = request.form.get('id_producto')
        precio_unitario = request.form.get('precio_unitario')

        # Actualizar los datos usando el modelo[cite: 2]
        DetallePedidoModel.actualizar(id_detalle, id_pedido, id_producto, precio_unitario)[cite: 2]
        return redirect(url_for('detalle_pedidos.listar_detalles'))

    # Cargar los datos actuales del detalle y las listas de selección[cite: 2]
    detalle = DetallePedidoModel.obtener_por_id(id_detalle)[cite: 2]
    pedidos = PedidoModel.obtener_todos()[cite: 2]
    productos = ProductoModel.obtener_todos()[cite: 2]
    return render_template('detalle_pedidos/editar.html', detalle=detalle, pedidos=pedidos, productos=productos)[cite: 2]


# 4. ELIMINAR UN DETALLE DE PEDIDO[cite: 2]
@detalle_pedido_bp.route('/detalle-pedidos/eliminar/<int:id_detalle>', methods=['POST'])
def eliminar_detalle(id_detalle):
    DetallePedidoModel.eliminar(id_detalle)[cite: 2]
    return redirect(url_for('detalle_pedidos.listar_detalles'))