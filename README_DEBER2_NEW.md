UNIVERSIDAD SAN FRANCISCO DE QUITO

COLEGIO DE CIENCIAS E INGENIERÍAS

Materia: Inteligencia Artificial

Semestre: 202510 – Primer Semestre 2025/2026

-------------------------------------------------------
PROYECTO: Ruta óptima de Ellensburg, WA a Havre, MT
-------------------------------------------------------

INTEGRANTES:
- María Eulalia Moncayo
- Gabriel Ávalos
- Gabriel Cazares
- Isabella Tulcán.

-------------------------------------------------------
OBJETIVO:
-------------------------------------------------------
Implementar dos algoritmos de búsqueda informada y no informada para encontrar 
la ruta de menor costo (en millas) entre Ellensburg, WA y Havre, MT utilizando 
los datos de distancias y heurísticas proporcionados:

1. **Búsqueda de Costo Uniforme (UCS) Bidireccional**  
   Utiliza dos colas de prioridad (una desde el inicio y otra desde el destino).  
   La búsqueda termina cuando ambas fronteras se cruzan o cuando la suma de 
   los costos mínimos supera el mejor costo encontrado.  
   - Criterio de prioridad: costo acumulado g(n).  
   - Desempate pseudo-aleatorio (semilla fija).  
   - Devuelve: mejor ruta, costo total y número de nodos generados.

2. **Búsqueda A\***  
   Utiliza una cola de prioridad con prioridad f(n) = g(n) + h(n).  
   La heurística h(n) es la distancia en línea recta hasta Havre.  
   - Test de objetivo: se realiza al hacer pop del nodo.  
   - Desempate pseudo-aleatorio reproducible.  
   - Devuelve: ruta óptima, costo total y número de nodos generados.

-------------------------------------------------------
DETALLES DE IMPLEMENTACIÓN:
-------------------------------------------------------
- Lenguaje: Python 3
- Librerías utilizadas:
  * heapq → manejo de colas de prioridad
  * random → desempate pseudo-aleatorio reproducible (random.seed(42))
  * math → operaciones numéricas
  * collections → estructuras auxiliares (deque, defaultdict)
- Grafo: construido con las conexiones y distancias bidireccionales del mapa.
- Heurística: distancias en línea recta (millas) de cada ciudad hacia Havre.
- Cada algoritmo reporta:
  • Ruta óptima
  • Costo total (suma de millas)
  • Nodos generados

-------------------------------------------------------
SALIDA ESPERADA:
-------------------------------------------------------
El programa imprime en consola los resultados de ambos algoritmos:

A* result: {'path': [...], 'cost': ..., 'nodes_generated': ...}
Bidirectional UCS result: {'path': [...], 'cost': ..., 'nodes_generated': ...}

-------------------------------------------------------
CONTRIBUCIÓN DE TODOS LOS INTEGRANTES:
-------------------------------------------------------
- Desarrollo del algoritmo A* y pruebas de validación.
- Desarrollo del UCS bidireccional y manejo de estructuras de datos.
- Integración, documentación, formato del código y README final.

-------------------------------------------------------
OBSERVACIONES:
-------------------------------------------------------
- El desempate pseudo-aleatorio garantiza resultados reproducibles entre ejecuciones.
- La comparación de resultados muestra la eficiencia del A* frente al UCS bidireccional 
  en términos de número de nodos generados.
- Ambos algoritmos cumplen las reglas establecidas en el enunciado.

-------------------------------------------------------
