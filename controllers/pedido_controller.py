from flask import Blueprint, render_template, request, redirect, url_for

# Importar el modelo de pedidos y el de clientes para poblar los selectores
from models.pedido_model import PedidoModel

# Definir el Blueprint para pedidos[cite: 2]
pedido_bp = Blueprint('pedidos', __name__)


# 1. LISTAR TODOS LOS PEDIDOS[cite: 2]
@pedido_bp.route('/pedidos', methods=['GET'])
def listar_pedidos():
    # Obtener todos los pedidos desde el Modelo[cite: 2]
    lista_pedidos = PedidoModel.obtener_todos()
    return render_template('pedidos/index.html', pedidos=lista_pedidos)[cite: 2]


# 2. CREAR UN NUEVO PEDIDO[cite: 2]
@pedido_bp.route('/pedidos/crear', methods=['GET', 'POST'])
def crear_pedido():
    if request.method == 'POST':
        # Capturar el id_cliente seleccionado en el formulario
        id_cliente = request.form.get('id_cliente')

        # Crear el pedido (MySQL generará la fecha automáticamente con CURRENT_TIMESTAMP)
        PedidoModel.crear(id_cliente)[cite: 2]
        return redirect(url_for('pedidos.listar_pedidos'))

    # Si es GET, traemos los clientes para mostrarlos en el <select> del formulario[cite: 2]
    clientes = ClienteModel.obtener_todos()[cite: 2]
    return render_template('pedidos/crear.html', clientes=clientes)[cite: 2]


# 3. EDITAR / ACTUALIZAR UN PEDIDO[cite: 2]
@pedido_bp.route('/pedidos/editar/<int:id_pedido>', methods=['GET', 'POST'])
def editar_pedido(id_pedido):
    if request.method == 'POST':
        id_cliente = request.form.get('id_cliente')

        # Actualizar usando el método del modelo exacto[cite: 2]
        PedidoModel.actualizar(id_pedido, id_cliente)[cite: 2]
        return redirect(url_for('pedidos.listar_pedidos'))

    # Si es GET, obtenemos el pedido por ID y la lista de todos los clientes
    pedido = PedidoModel.obtener_por_id(id_pedido)[cite: 2]
    clientes = ClienteModel.obtener_todos()[cite: 2]
    return render_template('pedidos/editar.html', pedido=pedido, clientes=clientes)[cite: 2]


# 4. ELIMINAR UN PEDIDO[cite: 2]
@pedido_bp.route('/pedidos/eliminar/<int:id_pedido>', methods=['POST'])
def eliminar_pedido(id_pedido):
    PedidoModel.eliminar(id_pedido)[cite: 2]
    return redirect(url_for('pedidos.listar_pedidos'))