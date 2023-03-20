# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력

import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

for j in array:
    print(j)