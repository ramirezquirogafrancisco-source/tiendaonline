import os
import sys

# Asegura que Python reconozca la raíz del proyecto para importar 'models' y 'controllers'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.producto_controller import producto_blueprint
from flask import Flask, redirect, url_for

app = Flask(__name__)

# Registrar blueprint del controlador
app.register_blueprint(producto_blueprint)


@app.route("/")
def home():
    # Intenta redirigir a la vista principal de productos
    try:
        return redirect(url_for("producto_blueprint.index"))
    except:
        # En caso de que el Blueprint internamente se llame 'producto'
        return redirect(url_for("producto.index"))


if __name__ == "__main__":
    app.run(debug=True)