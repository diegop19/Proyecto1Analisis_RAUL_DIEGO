import heapq

"Solución de la ruta del laberinto por medio de backtracking"
def solucion_backtracking(laberinto):
    tamano = len(laberinto)
    
    # Buscar la posición de la entrada (primera fila)
    for y in range(tamano):
        if laberinto[0][y] == 0:
            entrada = (0, y)
            break

    # Buscar la posición de la salida (última fila)
    for y in range(tamano):
        if laberinto[tamano - 1][y] == 2:
            salida = (tamano - 1, y)
            break

    # Direcciones posibles (arriba, derecha, abajo, izquierda)
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Función de backtracking para buscar la salida
    def backtrack(x, y, ruta):
        # Si hemos llegado a la salida
        if (x, y) == salida:
            ruta.append((x, y))
            return True

        # Marcar la celda como visitada (usamos un valor temporal como 3)
        laberinto[x][y] = 3
        ruta.append((x, y))

        # Intentar moverse en cada dirección posible
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < tamano and 0 <= ny < tamano and (laberinto[nx][ny] == 0 or laberinto[nx][ny] == 2):
                if backtrack(nx, ny, ruta):
                    return True

        # Si no hay ruta, retrocedemos
        ruta.pop()
        laberinto[x][y] = 0  # Desmarcar como visitado
        return False

    # Lista para almacenar la ruta encontrada
    ruta = []
    if backtrack(entrada[0], entrada[1], ruta):
        return ruta  # Devolver la ruta encontrada
    else:
        return None  # No se encontró ruta

"Solución de la ruta del laberinto por medio de backtracking pero optimizado"
def solucion_backtracking_optimizado(laberinto):
    tamano = len(laberinto)

    # Buscar la posición de la entrada (primera fila)
    for y in range(tamano):
        if laberinto[0][y] == 0:
            entrada = (0, y)
            break

    # Buscar la posición de la salida (última fila)
    for y in range(tamano):
        if laberinto[tamano - 1][y] == 2:
            salida = (tamano - 1, y)
            break

    # Función para calcular la distancia de Manhattan (heurística)
    def distancia_manhattan(x, y, salida):
        return abs(x - salida[0]) + abs(y - salida[1])

    # Direcciones posibles (arriba, derecha, abajo, izquierda)
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Usamos una cola de prioridad (heap) para priorizar los caminos más prometedores
    def buscar_camino_optimizado():
        # Cola de prioridad con (costo estimado, coordenada x, coordenada y, ruta actual)
        heap = []
        heapq.heappush(heap, (distancia_manhattan(entrada[0], entrada[1], salida), entrada[0], entrada[1], []))
        visitado = set()

        while heap:
            _, x, y, ruta = heapq.heappop(heap)

            if (x, y) in visitado:
                continue

            # Marcar como visitado
            visitado.add((x, y))
            nueva_ruta = ruta + [(x, y)]

            # Si hemos llegado a la salida
            if (x, y) == salida:
                return nueva_ruta

            # Explorar las direcciones posibles
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy

                if 0 <= nx < tamano and 0 <= ny < tamano and (laberinto[nx][ny] == 0 or laberinto[nx][ny] == 2):
                    if (nx, ny) not in visitado:
                        # Añadir el nuevo nodo a la cola de prioridad
                        prioridad = distancia_manhattan(nx, ny, salida)
                        heapq.heappush(heap, (prioridad, nx, ny, nueva_ruta))

        return None  # No se encontró un camino

    # Ejecutar la búsqueda optimizada
    ruta = buscar_camino_optimizado()

    return ruta