'''
BOJ 11399
시간제한: 1초
파이썬에서 제공한 sort()함수를 사용해도 되지만 n의 최댓값이 1000이고 시간 제한이 1초이므로
시간 복잡도가 O(n^2) 이하인 정렬 알고리즘 중 아무거나 사용해도 되므로 삽입정렬을 사용했다 
'''

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

#### 삽입정렬 ####

for i in range(1,n):
    insert_point = i
    insert_value = p[i]

    for j in range(i-1, -1, -1): # i-1부터 0까지 -1씩 감소하면서
        if p[j] < p[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1): # 삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기
        p[j] = p[j-1]
    p[insert_point] = insert_value # 삽입 위치에 현재 데이터 저장
    
# p.sort()
result = 0

for i in range(n):
    for j in range(i+1):
        result += p[j]

print(result)


