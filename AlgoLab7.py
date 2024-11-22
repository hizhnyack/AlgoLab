# Реализовать алгоритм Беллмана - Форда для произвольного графа

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            print(f"Проверка {self.vertex_data[u]}-{self.vertex_data[v]}, расстояние {self.vertex_data[v]}: {distances[v]}")

        return distances

g = Graph(5)

g.add_vertex_data(0, 'ВЧ №89553')
g.add_vertex_data(1, 'Лондон')
g.add_vertex_data(2, 'Вашингтон')
g.add_vertex_data(3, 'Кишинёв')
g.add_vertex_data(4, 'Марсель')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 2, 7)  # D -> C, weight 7
g.add_edge(3, 4, 3)  # D -> E, weight 3
g.add_edge(0, 2, 4)  # A -> C, weight 4
g.add_edge(2, 0, -3) # C -> A, weight -3
g.add_edge(0, 4, 5)  # A -> E, weight 5
g.add_edge(4, 2, 3)  # E -> C, weight 3
g.add_edge(1, 2, -4) # B -> C, weight -4
g.add_edge(4, 1, 2)  # E -> B, weight 2

# Running the Bellman-Ford algorithm from D to all vertices
print("Алгоритм Беллмана-Форда считает из точки ВЧ №89553\n")
distances = g.bellman_ford('ВЧ №89553')
for i, d in enumerate(distances):
    print(f"Время подлёта из ВЧ №89553 в {g.vertex_data[i]} составляет: {d}")