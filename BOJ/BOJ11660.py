import sys

input = sys.stdin.readline

n,m = map(int,input().split())

data = [[0] * (n+1)]
sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    row = list(map(int,input().split()))
    data.append([0]+row)

for i in range(1,n+1):
    for j in range(1, n+1):
        sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + data[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    result = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]
    print(result)
