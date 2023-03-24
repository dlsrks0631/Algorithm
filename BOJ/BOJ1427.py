'''
BOJ 1427 소트인사이드 = 내림차순 정렬하기
시간제한 2초
N <= 10억 -> 최대 자릿수 10

'''

import sys

input = sys.stdin.readline

n = list(input())

#### 선택정렬 ####

for i in range(len(n)):
    max = i
    for j in range(i+1, len(n)):
        if n[max] < n[j]:
            max = j
    if n[i] < n[max]:
        temp = n[i]
        n[i] = n[max]
        n[max] = temp

# n.sort(reverse=True)

result = "".join(n)
print(result)