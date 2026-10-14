from flask import Blueprint, render_template, request, redirect, url_for

# Importar los modelos necesarios
from models.pedido_model import PedidoModel
from models.cliente_model import ClienteModel

# Definir el Blueprint para las rutas de pedidos
pedido_bp = Blueprint('pedidos', __name__)


# 1. LISTAR TODOS LOS PEDIDOS
@pedido_bp.route('/pedidos', methods=['GET'])
def listar_pedidos():
    lista_pedidos = PedidoModel.obtener_todos()
    return render_template('pedido/index.html', pedidos=lista_pedidos)


# 2. CREAR UN NUEVO PEDIDO
@pedido_bp.route('/pedidos/crear', methods=['GET', 'POST'])
def crear_pedido():
    if request.method == 'POST':
        id_cliente = request.form.get('id_cliente')
        PedidoModel.crear(id_cliente)
        return redirect(url_for('pedidos.listar_pedidos'))

    clientes = ClienteModel.obtener_todos()
    return render_template('pedido/crear.html', clientes=clientes)


# 3. EDITAR / ACTUALIZAR UN PEDIDO
@pedido_bp.route('/pedidos/editar/<int:id_pedido>', methods=['GET', 'POST'])
def editar_pedido(id_pedido):
    if request.method == 'POST':
        id_cliente = request.form.get('id_cliente')
        PedidoModel.actualizar(id_pedido, id_cliente)
        return redirect(url_for('pedidos.listar_pedidos'))

    pedido = PedidoModel.obtener_por_id(id_pedido)
    clientes = ClienteModel.obtener_todos()
    return render_template('pedido/editar.html', pedido=pedido, clientes=clientes)


# 4. ELIMINAR UN PEDIDO
@pedido_bp.route('/pedidos/eliminar/<int:id_pedido>', methods=['POST'])
def eliminar_pedido(id_pedido):
    PedidoModel.eliminar(id_pedido)
    return redirect(url_for('pedidos.listar_pedidos'))