"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('menu_inicio.html')

@app.route('/crear_laberinto')
def crear_laberinto():
    return render_template('crear_laberinto.html')

if __name__ == '__main__':
    app.run(debug=False)