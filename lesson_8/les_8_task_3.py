# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def gen_graph(N):
    """Генерация графа"""
    graph = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                graph[j][i] = 0
    return graph


def dfs(graph, start, visited=None):
    """Алгоритм поиска в глубину"""
    if visited is None:
        visited = []
    visited.append(start)
    for next in range(len(graph[start])):
        if graph[start][next] == 1 and not (next in visited):
            dfs(graph, next, visited)
    return visited


print(*gen_graph(5), sep='\n')
print(dfs(gen_graph(5), 2))