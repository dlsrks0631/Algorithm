import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end= ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 노드 개수, 간선 개수, 시작노드
n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)