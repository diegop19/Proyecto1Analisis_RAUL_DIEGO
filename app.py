"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu_inicio.html')

if __name__ == '__main__':
    app.run(debug=False)