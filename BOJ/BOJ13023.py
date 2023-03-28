'''
BOJ 13023 ABCDE
시간제한: 2초

문제해결:

'''

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n)]
visited = [False] * n
result = False

for _ in range(m):
    e1,e2 = map(int,input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

def dfs(node, depth):
    global result
    if depth == 5:
        result = True
        return
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i, depth+1) # 수행될 때마다 깊이 증가시킴
    visited[node] = False # 빠져나오면 바꾸고

# 노드마다 dfs 실행
for j in range(n):
    dfs(j, 1)
    if result:
        break

if result:
    print(1)
else:
    print(0)


