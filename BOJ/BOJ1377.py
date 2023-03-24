'''
BOJ 1377 버블 정렬 프로그램 1
시간제한: 2초 
버블 정렬의 swap이 한 번도 일어나지 않은 루프가 언제인지 알아내는 문제로 n의 범위는 50만보다 작거나 같은 자연수이다
버블정렬 알고리즘을 사용시 시간제한에 걸리므로 적어도 O(nlogn)의 시간복잡도를 사용해야함

< 해결 방법 >
버블 정렬의 swap이 한 번도 일어나지 않은 루프가 언제인지 알아내는 문제로 n의 범위는 50만보다 작거나 같은 자연수이다
버블정렬 알고리즘을 사용시 시간제한에 걸리므로 적어도 O(nlogn)의 시간복잡도를 사용해야함
기본으로 제공하는 시간복잡도가 O(nlogn) sort()함수 사용
안쪽 루프는 1에서 n-j까지, 즉 왼쪽에서 오른쪽으로 이동하면서 swap을 수행함. 이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대 거리가 1이라는 뜻으로
데이터의 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 가장 많이 이동한 값을 찾으면 된다

'''

import sys

input = sys.stdin.readline

data = []
n = int(input())
max_index = 0
for i in range(n):
    data.append((int(input()),i))

data.sort()

for i in range(n):
    if max_index < data[i][1] - i:
        max_index = data[i][1] - i

print(max_index+1) # 마지막으로 스왑이 안도는 한 번의 반복문이 있으므로 +1