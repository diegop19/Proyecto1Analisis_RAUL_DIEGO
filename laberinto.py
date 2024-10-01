import random
import json
import os



def generar_laberinto(tamano):
    global laberinto
    # Inicializa la matriz del laberinto con paredes (1)
    laberinto = [[1 for _ in range(tamano)] for _ in range(tamano)]

    # Función para verificar si se puede añadir una celda al camino
    def es_valido(x, y):
        if 0 <= x < tamano and 0 <= y < tamano:
            return laberinto[x][y] == 1
        return False

    # Función para generar caminos
    def crear_camino(x, y):
        laberinto[x][y] = 0  # Marcar la celda como parte del camino

        # Mezclar direcciones para aleatorizar
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nx, ny = x + dx * 2, y + dy * 2  # Saltar dos celdas
            if es_valido(nx, ny):
                laberinto[x + dx][y + dy] = 0  # Crear el camino
                crear_camino(nx, ny)  # Recursión para el siguiente paso

    # Comenzar desde una celda aleatoria
    inicio_x = random.randrange(1, tamano - 1, 2)
    inicio_y = random.randrange(1, tamano - 1, 2)
    crear_camino(inicio_x, inicio_y)

    # Asegurar que haya una entrada y salida únicas en los bordes
    # Entrada
    entrada_y = random.choice(range(tamano))
    laberinto[0][entrada_y] = 0  # Entrada en la parte superior

    # Salida
    salida_y = random.choice(range(tamano))
    laberinto[tamano - 1][salida_y] = 0  # Salida en la parte inferior

    # Asegúrate de que hay un camino de la entrada a la salida
    laberinto[0][entrada_y] = 0  # Marcar la entrada
    laberinto[tamano - 1][salida_y] = 0  # Marcar la salida

    return laberinto




