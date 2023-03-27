'''
BOJ 1517 버블정렬

시간제한: 1초

N의 범위가 50만까지 이므로 시간복잡도가 O(n^2)인 버블정렬 알고리즘은 사용하지 못한다
두 그룹을 병합하는 과정에서 버블 정렬의 swap이 포함되어 있기 때문에 병합정렬을 사용했다
'''

import sys

input = sys.stdin.readline
result = 0

n = int(input())
array = list(map(int,input().split()))

array.insert(0,0)
tmp = [0] * (n+1)

# 병합 정렬
def merge_sort(s,e):
    global result
    if e - s < 1: return
    m = int(s + (e-s) / 2)
    merge_sort(s,m)
    merge_sort(m+1, e)

    for i in range(s, e+1):
        tmp[i] = array[i]
    
    index1 = s
    index2 = m + 1

    k = s # 시작 위치 삽입
    # 두 그룹을 합치기
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            array[k] = tmp[index2]
            result += (index2-k)    # swap 개수 증가
            k += 1
            index2 += 1
        else:
            array[k] = tmp[index1]
            k += 1
            index1 += 1
    
    # 두 번째 set이 다 출력되서 첫 번째 set이 끝까지 못갔을 때
    while index1 <= m:
        array[k] = tmp[index1]
        k += 1
        index1 += 1
    
    # 첫 번째 set이 다 출력되서 두 번째 set이 끝까지 못갔을 때
    while index2 <= m:
        array[k] = tmp[index2]
        k += 1
        index2 += 1

merge_sort(1, n)
print(result)