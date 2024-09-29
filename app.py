"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu_inicio.html')

@app.route('/generar_solucion')
def generar_solucion():
    return render_template('generar_solucion.html')

if __name__ == '__main__':
    app.run(debug=False)