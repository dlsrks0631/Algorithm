# 최소값 가능성이 없는 데이터는 삭제 !!
# window 크기 밖 데이터 삭제 !!

import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())          # 숫자의 개수, L 입력받기
data = list(map(int,input().split()))   # data 입력받기

d = deque()

for i in range(n):
    while True:
        if d and d[-1][1] > data[i]:
            d.pop()
        else:
            break
    d.append((i, data[i])) 
    if d[0][0] <= i-m:
        d.popleft()
    print(d[0][1], end = ' ')   

