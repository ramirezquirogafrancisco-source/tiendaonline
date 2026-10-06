from flask import Blueprint, render_template, request, redirect, url_for

# Importar el modelo exacto que creó tu compañero[cite: 2]
from models.cliente_model import ClienteModel

# Definir el Blueprint para las rutas del cliente[cite: 2]
cliente_bp = Blueprint('clientes', __name__)


# 1. LISTAR TODOS LOS CLIENTES[cite: 2]
@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    # Obtener clientes desde el Modelo usando el método exacto[cite: 2]
    lista_clientes = ClienteModel.obtener_todos()
    return render_template('clientes/index.html', clientes=lista_clientes)[cite: 2]


# 2. CREAR UN NUEVO CLIENTE[cite: 2]
@cliente_bp.route('/clientes/crear', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        # Obtener los datos del formulario (Vista)[cite: 2]
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        # Guardar mediante el Modelo[cite: 2]
        ClienteModel.crear(nombre, email, telefono)
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('clientes/crear.html')[cite: 2]


# 3. EDITAR / ACTUALIZAR UN CLIENTE[cite: 2]
@cliente_bp.route('/clientes/editar/<int:id_cliente>', methods=['GET', 'POST'])
def editar_cliente(id_cliente):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        # Actualizar usando el método del Modelo[cite: 2]
        ClienteModel.actualizar(id_cliente, nombre, email, telefono)
        return redirect(url_for('clientes.listar_clientes'))

    # Si es GET, obtener el cliente por ID para llenar el formulario
    cliente = ClienteModel.obtener_por_id(id_cliente)[cite: 2]
    return render_template('clientes/editar.html', cliente=cliente)[cite: 2]


# 4. ELIMINAR UN CLIENTE[cite: 2]
@cliente_bp.route('/clientes/eliminar/<int:id_cliente>', methods=['POST'])
def eliminar_cliente(id_cliente):
    ClienteModel.eliminar(id_cliente)[cite: 2]
    return redirect(url_for('clientes.listar_clientes'))