from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente_model import ClienteModel

# Definir el Blueprint para las rutas del cliente
cliente_bp = Blueprint('clientes', __name__)


# 1. LISTAR TODOS LOS CLIENTES
@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    lista_clientes = ClienteModel.obtener_todos()
    return render_template('cliente/index.html', clientes=lista_clientes)


# 2. CREAR UN NUEVO CLIENTE
@cliente_bp.route('/clientes/crear', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        ClienteModel.crear(nombre, email, telefono)
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('cliente/crear.html')


# 3. EDITAR / ACTUALIZAR UN CLIENTE
@cliente_bp.route('/clientes/editar/<int:id_cliente>', methods=['GET', 'POST'])
def editar_cliente(id_cliente):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        ClienteModel.actualizar(id_cliente, nombre, email, telefono)
        return redirect(url_for('clientes.listar_clientes'))

    cliente = ClienteModel.obtener_por_id(id_cliente)
    return render_template('cliente/editar.html', cliente=cliente)


# 4. ELIMINAR UN CLIENTE
@cliente_bp.route('/clientes/eliminar/<int:id_cliente>', methods=['POST'])
def eliminar_cliente(id_cliente):
    ClienteModel.eliminar(id_cliente)
    return redirect(url_for('clientes.listar_clientes'))