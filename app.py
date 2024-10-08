"Proyecto 01 Laberinto // Curso de Análisis de Algoritmos // Diego y Raúl"
"Página principal"

import json
import os
from flask import Flask, render_template, request, redirect, flash , send_file, jsonify
from laberinto import generar_laberinto
from solucion import solucion_backtracking, solucion_backtracking_optimizado
from construir_matriz_solucion import construir_solucion

app = Flask(__name__)
app.secret_key = 'ra&diegop'
matriz_solucion = None
laberinto = None

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('menu_inicio.html')

@app.route('/generar_solucion', methods=['GET', 'POST'])
def generar_solucion():
    global laberinto 
    global matriz_solucion
    pasos = []

    if request.method == 'POST':
        tipo_solucion = request.form.get('algoritmo')
        inicio = request.form.get("start")

        if inicio != "":
            coordenadas_inicio = eval(inicio)
            x, y = coordenadas_inicio
              
        if tipo_solucion == "fuerza_bruta":
            solucion_fuerza_bruta = solucion_backtracking(laberinto, x, y)
            matriz_solucion = construir_solucion(laberinto, solucion_fuerza_bruta)
        
        if tipo_solucion == "optimizado":
            solucion_optimizado = solucion_backtracking_optimizado(laberinto)
            matriz_solucion = construir_solucion(laberinto, solucion_optimizado)

    return render_template('generar_solucion.html')
    
# Ruta para crear el laberinto
@app.route('/crear_laberinto', methods=['GET', 'POST'])
def crear_laberinto():
    global laberinto 
    if request.method == 'POST':
        tamaño = int(request.form.get('tamaño'))
        
        # Generar la matriz
        matriz_laberinto = generar_laberinto(tamaño)

        laberinto = matriz_laberinto # Cargar laberinto a variable global
        print(laberinto)
        # Pasar la matriz a la plantilla para mostrarla
        return render_template('mostrar_laberinto.html', matriz=matriz_laberinto)
    
    return render_template('crear_laberinto.html')

@app.route('/guardar_cargar', methods=['GET', 'POST'])
def guardar_cargar():
    return render_template('guardar_cargar.html')

@app.route('/guardar_laberinto', methods=['POST'])
def guardar_laberinto():
    global laberinto
    if laberinto is not None:
        nombre_archivo = request.form.get('nombre_archivo')  # Obtener el nombre del archivo desde el formulario
        nombre_archivo += '.json'
        try:
            # Guardar el laberinto en el archivo JSON
            with open(nombre_archivo, 'w') as archivo:
                json.dump(laberinto, archivo, indent=4)
            #int(f"Laberinto guardado exitosamente en {nombre_archivo}.")
            #flash("Laberinto guardado exitosamente.", "success")  # Mensaje de éxito
            return send_file(nombre_archivo, as_attachment=True)  # Ofrece el archivo para descarga
        except Exception as e:
            print(f"Error al guardar el laberinto: {e}")
            flash("Error al guardar el laberinto.", "error")  # Mensaje de error
    else:
        flash("No hay laberinto para guardar.", "error")  # Mensaje de error
    return redirect('/guardar_cargar')  # Redirige a la página de carga/guardar


@app.route('/cargar_laberinto', methods=['POST'])
def cargar_laberinto():
    global laberinto
    # Obtener el archivo subido
    archivo = request.files.get('archivo')
    if archivo and archivo.filename.endswith('.json'):
        # Guardar el archivo en el sistema temporalmente
        nombre_archivo = archivo.filename
        archivo.save(nombre_archivo)  # Guarda el archivo en el directorio actual
        
        # Cargar el laberinto usando la función definida
        laberinto = cargar_laberinto_AUX(nombre_archivo)
        
        if laberinto is not None:
            flash("Laberinto cargado exitosamente.", "success")
        else:
            flash("Error al cargar el laberinto desde el archivo.", "error")
        
        return redirect('/guardar_cargar')  # Redirige a la página de carga/guardar
    else:
        flash("Por favor selecciona un archivo JSON válido.", "error")
        return redirect('/guardar_cargar')  # Redirige a la página de carga/guardar

def cargar_laberinto_AUX(nombre_archivo):
    """
    Carga el laberinto desde un archivo JSON.
    
    :param nombre_archivo: Nombre del archivo JSON desde el cual se cargará el laberinto.
    :return: Matriz que representa el laberinto (lista de listas) o None si ocurre un error.
    """
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                 laberinto = json.load(archivo)
            print(f"Laberinto cargado exitosamente desde {nombre_archivo}.")
            return laberinto
        else:
            print(f"El archivo {nombre_archivo} no existe.")
            return None
    except Exception as e:
        print(f"Error al cargar el laberinto: {e}")
        return None
    
@app.route('/mostrar_laberinto')
def mostrar_laberinto():
    global laberinto
    if laberinto is not None:
        return render_template('mostrar_laberinto.html', matriz=laberinto)
    else:
        flash("No hay laberinto disponible para mostrar.", "error")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)