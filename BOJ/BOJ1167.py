import sys

input = sys.stdin.readline

n = int(input())
datas = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int,input().split()))

    start = data[0]

    for i in range(1, len(data)-2, 2):
        edge, cost = data[i], data[i+1]
        datas[start].append((edge, cost))

def bfs(graph, start, visited):
    