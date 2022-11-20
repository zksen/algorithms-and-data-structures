# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

N = 10
handshake_graph = [[0 for _ in range(N)] for _ in range(N)]
count = 0

for i in range(N):
    for j in range(N):
        handshake_graph[i][j] = 0
        handshake_graph[j][i] = 1
        if i == j:
            handshake_graph[i][j] = 0

for i in range(N):
    for j in range(N):
        if handshake_graph[i][j] == 1:
            count += 1

# print(*handshake_graph, sep='\n')
print(f'Количество рукопажатий у такого количества друзей:{N}, будет:{count}')
