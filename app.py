"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('menu_inicio.html')

<<<<<<< HEAD
@app.route('/generar_solucion')
def generar_solucion():
    return render_template('generar_solucion.html')
=======
@app.route('/crear_laberinto')
def crear_laberinto():
    return render_template('crear_laberinto.html')
>>>>>>> 7b17f28dc01b6196a175cf928356c859357a415c

if __name__ == '__main__':
    app.run(debug=False)