from collections import defaultdict

class Graph:
    def __init__(self, V: int) -> None:     # V - количество вершин
        self.V = V
        self.adj = defaultdict(list)

    def DFSUtil(self, temp: list[int], v: int, visited: list[int]) -> list[int]:
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge(self, v:int, w:int) -> None:
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self) -> list[list[int]]:
        visited = [False] * self.V
        cc = []
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

# Пример использования
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Компоненты связности графа")
    print(cc)

# ввод с клавиатуры

# num_vertices = int(input("Укажите количество вершин: "))
# g = Graph(num_vertices)
#
# for i in range(num_vertices):
#     vertices = list(map(int, input(f"Укажите вершины, соединенные с вершиной {i}: ").split()))
#     for vertex in vertices:
#         g.addEdge(i, vertex)
#
# print(g.connectedComponents())