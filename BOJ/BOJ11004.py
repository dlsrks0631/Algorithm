'''
BOJ 11004 k번째 수 구하기
시간제한 2초
N <= 500만

퀵 정렬 사용
'''
import sys

input = sys.stdin.readline
print = sys.stdout.write

def quick_sort(array, start, end):
    # 원소가 한 개인 경우 종료
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:  # while 루프에서 인덱스 left와 right가 범위를 벗어날 수 있으므로 left <= end 조건을 먼저 명시해야함
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # left와 right가 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        elif right > left:
            array[left], array[pivot] = array[pivot], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

n,k = map(int,input().split())
array = list(map(int,input().split()))

quick_sort(array,0,len(array)-1)

print(str(array[k-1]))