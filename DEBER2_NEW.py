import heapq, random, math
from collections import defaultdict, deque

random.seed(42)  # Para desempate pseudo-aleatorio reproducible

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0
    def push(self, priority, item):
        # desempate pseudoaleatorio: usamos random junto a counter
        heapq.heappush(self.heap, (priority, random.random(), self.counter, item))
        self.counter += 1
    def pop(self):
        return heapq.heappop(self.heap)[-1]
    def is_empty(self):
        return not self.heap

def reconstruct_path(came_from, start, goal):
    path = [goal]
    cur = goal
    while cur != start:
        cur = came_from[cur]
        path.append(cur)
    path.reverse()
    return path

# ------------------ GRAFO (ejemplo) ------------------
# Replace these edges with the exact edges and distances from your map.
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

# ------------------ HEURÍSTICA (S-LINEA A HAVRE) ------------------
heuristic = {
    'Ellensburg': 516.03,
    'Pendleton': 472.53,
    'Spokane': 362.93,
    'Missoula': 232.19,
    'Bonners_Ferry': 303.57,
    'Helena': 174.65,
    'Butte': 221.04,
    'West_Glacier': 197.21,
    'Great_Falls': 104.1,
    'Havre': 0.0
}

# ---------- A* ----------
def a_star(start, goal, graph, heuristic):
    frontier = PriorityQueue()
    frontier.push(heuristic[start], (start, 0.0))  # (node, g)
    came_from = {}
    cost_so_far = {start: 0.0}
    nodes_generated = 0
    visited = set()
    while not frontier.is_empty():
        node, g = frontier.pop()
        if node == goal:
            path = reconstruct_path(came_from, start, goal)
            return {'path': path, 'cost': g, 'nodes_generated': nodes_generated}
        if node in visited:
            continue
        visited.add(node)
        for neigh, w in graph.get(node, {}).items():
            nodes_generated += 1
            new_g = g + w
            if neigh not in cost_so_far or new_g < cost_so_far[neigh]:
                cost_so_far[neigh] = new_g
                came_from[neigh] = node
                frontier.push(new_g + heuristic.get(neigh, 0.0), (neigh, new_g))
    return None

# ---------- Bidirectional UCS ----------
def bidirectional_ucs(start, goal, graph):
    if start == goal:
        return {'path':[start], 'cost':0.0, 'nodes_generated':0}
    front_f = PriorityQueue()
    front_b = PriorityQueue()
    front_f.push(0.0, (start, 0.0))
    front_b.push(0.0, (goal, 0.0))
    parents_f = {start: None}
    parents_b = {goal: None}
    cost_f = {start: 0.0}
    cost_b = {goal: 0.0}
    expanded_f = set()
    expanded_b = set()
    nodes_generated = 0
    best_meet = None
    best_cost = math.inf

    def peek_min_g(pq):
        return pq.heap[0][0] if pq.heap else math.inf

    while not front_f.is_empty() and not front_b.is_empty():
        if peek_min_g(front_f) <= peek_min_g(front_b):
            node, g = front_f.pop()
            if node in expanded_f: 
                continue
            expanded_f.add(node)
            if node in expanded_b:
                total = g + cost_b[node]
                if total < best_cost:
                    best_cost = total
                    best_meet = node
            for neigh, w in graph.get(node, {}).items():
                nodes_generated += 1
                new_g = g + w
                if neigh not in cost_f or new_g < cost_f[neigh]:
                    cost_f[neigh] = new_g
                    parents_f[neigh] = node
                    front_f.push(new_g, (neigh, new_g))
                    if neigh in cost_b:
                        total = new_g + cost_b[neigh]
                        if total < best_cost:
                            best_cost = total
                            best_meet = neigh
        else:
            node, g = front_b.pop()
            if node in expanded_b:
                continue
            expanded_b.add(node)
            if node in expanded_f:
                total = g + cost_f[node]
                if total < best_cost:
                    best_cost = total
                    best_meet = node
            for neigh, w in graph.get(node, {}).items():
                nodes_generated += 1
                new_g = g + w
                if neigh not in cost_b or new_g < cost_b[neigh]:
                    cost_b[neigh] = new_g
                    parents_b[neigh] = node
                    front_b.push(new_g, (neigh, new_g))
                    if neigh in cost_f:
                        total = new_g + cost_f[neigh]
                        if total < best_cost:
                            best_cost = total
                            best_meet = neigh

        if peek_min_g(front_f) + peek_min_g(front_b) >= best_cost:
            break

    if best_meet is None:
        return None
    path_f = []
    cur = best_meet
    while cur is not None:
        path_f.append(cur)
        cur = parents_f.get(cur, None)
    path_f.reverse()
    path_b = []
    cur = parents_b.get(best_meet, None)
    while cur is not None:
        path_b.append(cur)
        cur = parents_b.get(cur, None)
    full_path = path_f + path_b
    return {'path': full_path, 'cost': best_cost, 'nodes_generated': nodes_generated}

# ---------- Run ----------
start = 'Ellensburg'
goal = 'Havre'

res_a = a_star(start, goal, graph, heuristic)
res_bi = bidirectional_ucs(start, goal, graph)

print("A* result:", res_a)
print("Bidirectional UCS result:", res_bi)
