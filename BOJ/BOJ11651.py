import sys

n = int(sys.stdin.readline())

array = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    array.append([y,x])

array.sort()

for a,b in array:
    print(b,a)