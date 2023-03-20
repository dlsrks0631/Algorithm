'''
부분수열의 합

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램

합이 S가 되는 부분수열의 개수를 출력

< 입력 >
5 0
-7 -3 -2 5 8  ---> 1

< 문제 해결 >
-> 조합 활용
'''

import sys
import itertools

input = sys.stdin.readline

n,s = map(int,input().split())  # 부분 합이 s인 것

data = list(map(int,input().split()))

count = 0

for i in range(1,n+1):
    combinations = itertools.combinations(data,i)

    for j in combinations:
        if sum(j) == s:
            count += 1

print(count)