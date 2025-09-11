# Ruta Óptima de Durán a Tulcán con Búsqueda Uniforme 

Participantes: María Eulalia Moncayo, Gabriel Ávalos, Gabriel Cazares, Isabella Tulcán.

## 🌍 Búsqueda de Costo Uniforme (UCS)


Este programa implementa el algoritmo de Búsqueda de Costo Uniforme para encontrar 
la ruta de menor costo (en kilómetros) entre dos ciudades en un grafo.

⚙️ Cómo funciona:
- Usa un grafo representado con un diccionario (cada ciudad apunta a sus vecinas y distancias).
- Emplea una cola de prioridad (heapq) para expandir primero el nodo de menor costo acumulado.
- Devuelve:
    • La mejor ruta encontrada
    • El costo total (km)
    • El número de nodos generados durante la búsqueda

📌 Uso:
ruta, costo_total, nodos = uniform_cost_search("Duran", "Tulcán")

print("Mejor ruta:", " → ".join(ruta))
print("Costo total:", costo_total, "km")
print("Nodos generados:", nodos)

🚀 Requisitos:
- Python 3.x
- No requiere librerías externas
"""
