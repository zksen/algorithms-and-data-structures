# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.


from heapq import *

graph = {'0': [(1, '2'), (9, '4'), (1, '3')],
         '1': [(9, '2'), (5, '6'), (4, '3')],
         '2': [(3, '4'), (6, '6'), (9, '1')],
         '3': [],
         '4': [(1, '6')],
         '5': [(5, '6')],
         '6': [(7, '2'), (8, '4'), (1, '5')],
         '7': [(1, '5'), (2, '6')]}

start = '0'
goal = '6'
cost_visited = {start: 0}


def dijkstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    # cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited


visited = dijkstra(start, goal, graph)

cur_node = goal
print(f'\npath from {start} to {goal}: \n {goal} ', end='')
while cur_node != start:
    cur_node = visited[cur_node]
    print(f' <--- {cur_node} ', end='')

print(f'\ncost of path: {cost_visited[goal]}')