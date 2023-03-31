import sys

data = []

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    start, end = map(int,input().split())
    data.append((start,end))

data.sort(key = lambda x: (x[1], x[0]))
result = 1
end = data[0][1]

for i in range(1,n):
    if data[i][0] >= end:
        result += 1
        end = data[i][1]

print(result)