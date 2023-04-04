import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())

graph = []
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    graph.append(data)

# 동 서 남 북
dx = [1,-1,0,0]
dy = [0,0,-1,1]


queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs(graph):
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx,ny = dx[k] + x, dy[k] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs(graph)
for i in graph:
    for tomato in i:
        if tomato == 0:
            print(-1)
            exit()  
    result = max(result, max(i))

print(result-1)
