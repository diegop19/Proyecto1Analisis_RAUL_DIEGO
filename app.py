"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

from flask import Flask, render_template, request
from laberinto import generar_laberinto

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('menu_inicio.html')

@app.route('/generar_solucion')
def generar_solucion():
    return render_template('generar_solucion.html')

@app.route('/crear_laberinto')

# Ruta para crear el laberinto
@app.route('/crear_laberinto', methods=['GET', 'POST'])

def crear_laberinto():
    if request.method == 'POST':
        tamaño = int(request.form.get('tamaño'))
        
        # Generar la matriz
        matriz_laberinto = generar_laberinto(tamaño)
        
        # Pasar la matriz a la plantilla para mostrarla
        return render_template('mostrar_matriz.html', matriz=matriz_laberinto)
    
    return render_template('crear_laberinto.html')

if __name__ == '__main__':
    app.run(debug=False)