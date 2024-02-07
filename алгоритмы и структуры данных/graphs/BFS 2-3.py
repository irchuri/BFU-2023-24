from collections import deque


with open('matrix.txt') as f:
    matrix = [list(map(int, row.split(','))) for row in f.readlines()]


def matrix_to_adjacency_component(matrix: list[list]) -> dict:
    components = dict()
    for i, node in enumerate(matrix):
        adjacent = list()
        for j, connected in enumerate(node):
            if connected:
                adjacent.append(j)
        components[i] = adjacent
    return components


components = matrix_to_adjacency_component(matrix)


print(f'Количество компонент связности: {len(components)}')
print('Компоненты связности:')
for componenta in components:
    print(f'{componenta+1}:   {components[componenta]}')

# def breadth_first_search(graph:dict, root) -> set:
#     visited = set()
#     queue = deque([root])
#
#     while queue:
#         vertex = queue.popleft()
#         visited.add(vertex)
#         for i in graph[vertex]:
#             if i not in visited:
#                 queue.append(i)
#     return(visited)


