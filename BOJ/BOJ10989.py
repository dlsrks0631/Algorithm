#### 계수정렬 문제 ####
#### 백준 10989 ####
#### 메모리 초과 ###??

import sys

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

count = [0] * (max(array) + 1)

for i in range(n):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
