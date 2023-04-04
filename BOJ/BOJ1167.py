import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int,input().split()))

    start = data[0]

    for i in range(1, len(data)-2, 2):
        edge, cost = data[i], data[i+1]
        graph[start].append((edge, cost))

distance = [0] * (n+1)
visited = [False] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i[0]]:
                queue.append(i[0])
                visited[i[0]] = True
                distance[i[0]] = distance[v] + i[1]

bfs(graph, 1, visited)
max = 1

for j in range(2, n+1):
    if distance[max] < distance[j]:
        max = j

distance = [0] * (n+1)
visited = [False] * (n+1)

bfs(graph, max, visited)

distance.sort(reverse=True)
print(distance[0])