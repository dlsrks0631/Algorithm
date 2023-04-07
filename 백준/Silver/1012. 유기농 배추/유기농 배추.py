from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):           
    queue = deque([(x,y)])
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 :
                queue.append((nx,ny))
                graph[nx][ny] = 0

test_case = int(input()) 

for i in range(test_case):
    m,n,k = map(int,input().split())
    graph = [[0] * n for _ in range(m)]
    result = 0

    for j in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                result += 1

    print(result)