array = [1,3,4,2]

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

quick_sort(array, 0, len(array)-1)


# 파이썬의 장점을 살린 퀵 정렬

def quick_sort_python(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

print(quick_sort_python(array))
