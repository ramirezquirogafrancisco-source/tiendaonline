import os
import sys
from flask import Flask, redirect, url_for

# Asegura que Python reconozca la raíz del proyecto para importar 'models' y 'controllers'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 1. IMPORTAR CONTROLADORES (BLUEPRINTS)
from controllers.producto_controller import producto_blueprint
from controllers.cliente_controller import cliente_bp
from controllers.pedido_controller import pedido_bp
from controllers.detalle_pedido_controller import detalle_pedido_bp

app = Flask(__name__)

# 2. REGISTRAR LOS BLUEPRINTS
app.register_blueprint(producto_blueprint)
app.register_blueprint(cliente_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(detalle_pedido_bp)

# 3. RUTA INICIAL / PRINCIPAL
@app.route("/")
def home():
    # Redirige a la vista principal de productos al ingresar a http://127.0.0.1:5000/
    try:
        return redirect(url_for("productos.listar_productos"))
    except:
        return redirect(url_for("producto_blueprint.index"))


if __name__ == "__main__":
    app.run(debug=True)