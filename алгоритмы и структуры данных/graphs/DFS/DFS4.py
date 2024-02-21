from __future__ import annotations
from collections import defaultdict


class Graph:

    def __init__(self, vertex: int) -> None:
        self.V = vertex  # вершина
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, vertex: int, destination: int) -> None:
        self.graph[vertex].append(destination)

    # dfs
    def dfs(self, destination: int, visited_vertex: list[bool]) -> None:
        visited_vertex[destination] = True
        print(destination, end='')
        for i in self.graph[destination]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, destination, visited_vertex: list[bool], stack: list) -> None:
        visited_vertex[destination] = True
        for i in self.graph[destination]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(destination)

    # transpose the matrix
    def transpose(self) -> Graph:
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self) -> None:
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)
        scc_count = 0
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")
                scc_count += 1
        print(f"Количество компонент сильной связности: {scc_count}")


# ввод графа с клавиатуры
num_vertices = int(input("Укажите количество вершин: "))
g = Graph(num_vertices)

for i in range(num_vertices):
    vertices = list(map(int, input(f"Укажите вершины, соединенные с вершиной {i}: ").split()))
    for vertex in vertices:
        g.add_edge(i, vertex)

print("Компоненты сильной связности:")
g.print_scc()
