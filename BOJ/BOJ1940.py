import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = list(map(int,input().split()))

count = 0

# s = set(arr) > set -> index 사용불가
# for i in arr:
#     if m-i in s:
#         count += 1

# print(count//2) // 중복 제거

arr.sort()
i = 0
j = n - 1

while i < j:
    if arr[i] + arr[j] < m:
        i += 1
    elif arr[i] + arr[j] == m:
        count += 1
        i += 1
        j -= 1
    else:
        j -= 1

print(count)


