from flask import Blueprint, render_template, request, redirect, url_for
from models.producto_model import ProductoModel

producto_blueprint = Blueprint('producto', __name__)

@producto_blueprint.route('/productos')
def index():
    productos = ProductoModel.obtener_todos()
    if productos:
        print("CLAVES DE PRODUCTO EN MYSQL:", productos[0].keys() if isinstance(productos[0], dict) else productos[0])
    return render_template('producto/index.html', productos=productos)

@producto_blueprint.route('/productos/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        ProductoModel.crear(nombre, precio, stock)
        return redirect(url_for('producto.index'))
    return render_template('producto/crear.html')

@producto_blueprint.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        
        ProductoModel.actualizar(id, nombre, precio, stock)
        return redirect(url_for('producto.index'))

    producto = ProductoModel.obtener_por_id(id)
    if not producto:
        return redirect(url_for('producto.index'))

    # Pasamos tanto producto como id explícitamente
    return render_template('producto/editar.html', producto=producto, id=id)

@producto_blueprint.route('/productos/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    ProductoModel.eliminar(id)
    return redirect(url_for('producto.index'))