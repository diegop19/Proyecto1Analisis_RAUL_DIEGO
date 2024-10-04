"Algoritmo para modificar la matriz y construir la matriz con la solución dada por la lista de tuplas"

def construir_solucion(matriz, coordenadas):
    for (i, j) in coordenadas:
        matriz[i][j] = 3
    
    return matriz