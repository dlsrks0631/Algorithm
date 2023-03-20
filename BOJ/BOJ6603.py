'''
로또

독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.
예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])
집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

< 입력 >
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

1. 문제 해결
-> itertools 조합 사용
-> array의 요소 삭제 사용 -> del
  (ex)
    array = [1,2,3,3,3]
    del(array[0]) -> array의 인덱스를 사용하여 삭제
    print(array) -> [2,3,3,3]
    array.remove(3) -> array의 값을 사용하여 삭제
    print(array) -> [2,3,3]

'''

import itertools
import sys

input = sys.stdin.readline

while True:
    data = list(map(int,input().split()))

    if data[0] == 0:
        break
    del data[0]
    data = list(itertools.combinations(data,6))
    for i in data:
        for j in i:
            print(j, end=' ')
        print()
    print()
