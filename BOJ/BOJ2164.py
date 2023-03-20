import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()

for i in range(1,n+1):
    d.append(i)

while len(d) != 1:
    d.popleft()
    d.append(d[0])
    d.popleft()

print(d[0])

# [1,2,3,4] 3 4 2   4 2 4    2 4  4 4

# []
