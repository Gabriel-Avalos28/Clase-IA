import heapq, math

# ----- Grafo (Graph) -----
graph = {
    'Ellensburg': {'Spokane': 175, 'Pendleton': 168},
    'Spokane': {'Ellensburg': 175, 'Bonners Ferry': 112, 'Missoula': 199},
    'Pendleton': {'Ellensburg': 168},
    'Bonners Ferry': {'Spokane': 112, 'West Glacier': 176},
    'Missoula': {'Spokane': 199, 'Helena': 111},
    'Butte': {'Helena': 65},
    'Helena': {'Butte': 65, 'Great Falls': 91, 'West Glacier': 243, 'Missoula': 111},
    'West Glacier': {'Bonners Ferry': 176, 'Helena': 243, 'Great Falls': 211, 'Havre': 231},
    'Great Falls': {'Helena': 91, 'West Glacier': 211, 'Havre': 115},
    'Havre': {'Great Falls': 115, 'West Glacier': 231}
}

def ucs_neighbors_iterated(start, goal):
    pq = [(0.0, start, [start])]
    best = {start: 0.0}
    neighbors_iterated = 0
    while pq:
        g, u, path = heapq.heappop(pq)
        if g > best.get(u, math.inf):
            continue
        # CONTAMOS SIEMPRE los vecinos (incluye start/goal) — incluso si u es el goal
        # The neighbor count logic is placed before the goal check in UCS
        for v, w in graph[u].items():
            neighbors_iterated += 1
            ng = g + w
            if ng < best.get(v, math.inf):
                best[v] = ng
                heapq.heappush(pq, (ng, v, path + [v]))
        if u == goal:
            return neighbors_iterated, path, g
    return neighbors_iterated, None, math.inf

def astar_neighbors_iterated(start, goal):
    pq = [(heuristic[start], 0.0, start, [start])]
    best = {start: 0.0}
    neighbors_iterated = 0
    while pq:
        f, g, u, path = heapq.heappop(pq)
        if g > best.get(u, math.inf):
            continue
        # A* PARA ANTES de iterar vecinos si es el goal (A* stops before iterating neighbors if it's the goal)
        if u == goal:
            return neighbors_iterated, path, g
        for v, w in graph[u].items():
            neighbors_iterated += 1  # incluye start/goal si aparecen
            ng = g + w
            if ng < best.get(v, math.inf):
                best[v] = ng
                heapq.heappush(pq, (ng + heuristic[v], ng, v, path + [v]))
    return neighbors_iterated, None, math.inf


def bidirectional_ucs(start, goal):
    # Cola de prioridad para ambos lados
    fwd_pq = [(0.0, start, [start])]
    bwd_pq = [(0.0, goal, [goal])]

    # Mejor costo conocido en cada lado
    fwd_best = {start: 0.0}
    bwd_best = {goal: 0.0}

    # Para reconstrucción
    fwd_paths = {start: [start]}
    bwd_paths = {goal: [goal]}

    # Nodos expandidos
    neighbors_iterated = 0

    # Costo y punto de encuentro
    best_cost = math.inf
    meet_node = None

    while fwd_pq and bwd_pq:
        # Escoger el lado con menor costo parcial
        if fwd_pq[0][0] <= bwd_pq[0][0]:
            g, u, path = heapq.heappop(fwd_pq)
            if g > fwd_best.get(u, math.inf):
                continue
            # Revisar si u ya fue alcanzado desde atrás
            if u in bwd_best:
                total_cost = g + bwd_best[u]
                if total_cost < best_cost:
                    best_cost = total_cost
                    meet_node = u
            # Expandir vecinos
            for v, w in graph[u].items():
                neighbors_iterated += 1
                ng = g + w
                if ng < fwd_best.get(v, math.inf):
                    fwd_best[v] = ng
                    fwd_paths[v] = path + [v]
                    heapq.heappush(fwd_pq, (ng, v, path + [v]))
        else:
            g, u, path = heapq.heappop(bwd_pq)
            if g > bwd_best.get(u, math.inf):
                continue
            # Revisar si u ya fue alcanzado desde adelante
            if u in fwd_best:
                total_cost = g + fwd_best[u]
                if total_cost < best_cost:
                    best_cost = total_cost
                    meet_node = u
            # Expandir vecinos
            for v, w in graph[u].items():
                neighbors_iterated += 1
                ng = g + w
                if ng < bwd_best.get(v, math.inf):
                    bwd_best[v] = ng
                    bwd_paths[v] = path + [v]
                    heapq.heappush(bwd_pq, (ng, v, path + [v]))

    if meet_node is None:
        return neighbors_iterated, None, math.inf

    # Reconstruir camino completo
    path_fwd = fwd_paths[meet_node]
    path_bwd = list(reversed(bwd_paths[meet_node]))
    full_path = path_fwd[:-1] + path_bwd

    return neighbors_iterated, full_path, best_cost


# --------- PRUEBA ----------
if _name_ == "_main_":

    s, t = "Ellensburg", "Havre"
    n_ucs, ruta_u, costo_u = ucs_neighbors_iterated(s, t)
    n_astar, ruta_a, costo_a = astar_neighbors_iterated(s, t)
    n_bucs, ruta_bucs, costo_bucs = bidirectional_ucs(s, t)

    print("UCS vecinos iterados:", n_ucs)  
    print("A* vecinos iterados:", n_astar)
    print("BUCS vecinos iterados:", n_bucs)  
    print("Ruta UCS:", " → ".join(ruta_u), " | Costo:", costo_u, "mi")  
    print("Ruta A*:", " → ".join(ruta_a), " | Costo:", costo_a, "mi")   
    print("Ruta BUCS:", " → ".join(ruta_bucs))
