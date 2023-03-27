'''
BOJ 11724 연결 요소의 개수
시간제한: 3초

정점의 개수 N과 간선의 개수 M이 주어짐
둘째 줄부터 M개의 줄에 간선의 양 끝점 U,V가 주어짐
'''

import sys

input = sys.stdin.readline


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(1, n+1):
    if visited[j]:
        continue
    dfs(graph, j, visited)
    result += 1

print(result)




