'''
재귀를 사용해서 풀어야하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수
파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데

import sys
sys.setrecursionlimit(10 ** 6)
'''

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input()) # 테스트 케이스 개수

result = True # 이분 그래프인지 아닌지

def dfs(graph, v, visited):
    global result
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            # 바로 직전에 있는 노드와 다른 집합으로 분류
            check[i] = (check[v] + 1) % 2
            dfs(graph, i, visited)
        # 방문했던 노드의 집합과 방문할 노드의 집합과 똑같으면 이분그래프가 아님
        elif check[i] == check[v]:
            result = False

for _ in range(n):
    v, e = map(int,input().split()) # 노드 개수, 에지 개수
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    result = True  # 다시 초기화

    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if result:
            dfs(graph, i, visited)
        else:
            break
    
    if result:
        print("YES")
    else:
        print("NO")




