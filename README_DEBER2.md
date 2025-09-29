# 📌 Algoritmos de Búsqueda en Grafos

Este proyecto implementa y compara distintos algoritmos de búsqueda en un grafo que representa un conjunto de ciudades conectadas por distancias en millas. El objetivo es encontrar la ruta más corta entre dos nodos (ciudades) y analizar cómo se comporta cada algoritmo en cuanto a número de vecinos iterados, ruta encontrada y costo total.

**🧭 Algoritmos implementados**

- UCS (Uniform Cost Search)

Explora nodos expandiendo siempre el de menor costo acumulado.

Itera los vecinos incluso si el nodo actual es el objetivo.

- A* (A estrella)

Combina costo real recorrido + heurística estimada.

Se detiene antes de expandir vecinos si el nodo actual ya es el objetivo.

- UCS Bidireccional (BUCS)

Realiza la búsqueda desde el nodo inicial y el nodo final al mismo tiempo.

Cuando ambas búsquedas se encuentran, se reconstruye el camino.

Suele reducir el número de vecinos iterados respecto a UCS clásico.

**⚙️ Cómo ejecutarlo**

Ejecuta el archivo principal en Python:

python main.py

**📊 Ejemplo de salida**
UCS vecinos iterados: 12
A* vecinos iterados: 9
BUCS vecinos iterados: 7

Ruta UCS: Ellensburg → Spokane → Missoula → Helena → Great Falls → Havre | Costo: 690.0 mi
Ruta A*:  Ellensburg → Spokane → Missoula → Helena → Great Falls → Havre | Costo: 690.0 mi
Ruta BUCS: Ellensburg → Spokane → Missoula → Helena → Great Falls → Havre

**📂 Archivos**

DEBER2.py → Contiene la implementación de UCS, A* y UCS Bidireccional.

**👥 Integrantes**

- María Eulalia Moncayo
- Gabriel Ávalos
- Gabriel Cazares
- Isabella Tulcán.
