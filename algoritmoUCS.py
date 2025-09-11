import heapq

graph = {
    "Duran": {"Milagro": 25,"Guayaquil":5},
    "Milagro": {"Portoviejo": 190, "Duran": 25, "Guayaquil": 52},
    "Guayaquil": {"Duran":5,"Milagro": 52, "Machala": 180, "Riobamba": 200, "Ambato": 265, "Babahoyo": 67},
    "Machala": {"Guayaquil": 180, "Loja": 230},
    "Loja": {"Machala": 230, "Cuenca": 214},
    "Cuenca": {"Loja": 214, "Riobamba": 200},
    "Riobamba": {"Guayaquil": 200, "Ambato": 58, "Cuenca": 200},
    "Ambato": {"Guayaquil": 265, "Riobamba": 58, "Quito": 117},
    "Quito": {"Ambato": 117, "Santo Domingo": 133, "Ibarra": 115},
    "Ibarra": {"Quito": 115, "Tulcán": 125},
    "Tulcán": {"Ibarra": 125, "Esmeraldas": 380},
    "Santo Domingo": {"Quito": 133, "Quevedo": 100, "Manta": 220, "Esmeraldas": 280},
    "Quevedo": {"Babahoyo": 50, "Portoviejo": 120, "Santo Domingo": 100},
    "Babahoyo": {"Quevedo": 50,"Guayaquil":67},
    "Portoviejo": {"Quevedo": 120, "Manta": 40,"Milagro":190},
    "Manta": {"Portoviejo": 40, "Santo Domingo": 220, "Esmeraldas": 300},
    "Esmeraldas": {"Manta": 300, "Santo Domingo": 280, "Tulcán": 380}
}

def uniform_cost_search(start, goal):
    # Cola de prioridad: (costo acumulado, ciudad, ruta)
    frontier = [(0, start, [start])]
    heapq.heapify(frontier)

    # Mejor costo conocido hacia cada ciudad
    best_cost = {start: 0}
    nodes_generated = 0

    while frontier:
        cost, city, path = heapq.heappop(frontier)

        # Si llegamos al objetivo
        if city == goal:
            return path, cost, nodes_generated

        # Expandir vecinos
        for neighbor, distance in graph[city].items():
            nodes_generated += 1
            new_cost = cost + distance

            # Solo insertamos si es la primera vez o si encontramos un costo mejor
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, neighbor, new_path))

    return None, float("inf"), nodes_generated


# Ejecutar búsqueda
ruta, costo_total, nodos = uniform_cost_search("Duran", "Tulcán")

print("Mejor ruta:", " → ".join(ruta))
print("Costo total:", costo_total, "km")
print("Nodos generados:", nodos)
