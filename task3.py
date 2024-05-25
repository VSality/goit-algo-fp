import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))

def dijkstra(graph, start):
    min_heap = [(0, start)]
    
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    
    parents = {vertex: None for vertex in graph.vertices}
    
    while min_heap:
        # Вибір вузла з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(min_heap)
        
        # Всі суміжні вершини
        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances, parents

def print_path(parents, vertex):
    path = []
    while vertex is not None:
        path.append(vertex)
        vertex = parents[vertex]
    path.reverse()
    return path


graph = Graph()
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]

for u, v, weight in edges:
    graph.add_edge(u, v, weight)

start_vertex = 'A'
distances, parents = dijkstra(graph, start_vertex)

print(f"Distances from start vertex '{start_vertex}':")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")

print("\nPaths from start vertex:")
for vertex in graph.vertices:
    if vertex != start_vertex:
        path = print_path(parents, vertex)
        print(f"Path to {vertex}: {' -> '.join(path)}")
