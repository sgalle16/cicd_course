"""
Application entry point for a simple calculator web app.
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir, potencia, modulo

app = Flask(__name__)


@app.route("/health")
def health():
    """
    Health check endpoint to verify if the application is running.
    """
    return "OK", 200


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles GET requests to display the calculator form
    and POST requests to perform calculations based on form input.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            elif operacion == "potencia":
                resultado = potencia(num1, num2)
            elif operacion == "modulo":
                resultado = modulo(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError as e:
            resultado = f"Error: {str(e)}"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    # Quita debug=True para producción
    app.run(debug=False, port=5000, host="0.0.0.0")
