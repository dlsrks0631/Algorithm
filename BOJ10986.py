import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr1 = list(map(int,input().split()))  # [ 1,2,3,1,2 ]
arr2 = [] # 합배열
arr3 = [] # 나머지배열
repeat = [0] * m # 중복 확인

result = 0

temp = 0
for i in arr1:
    temp = temp + i
    arr2.append(temp)   # arr2 = [ 1,3,6,7,9 ]

temp = 0
for j in arr2:
    temp = j % m
    arr3.append(temp)   # arr3 = [ 1,0,0,1,0 ]
    if (temp % m == 0):
        result += 1
    repeat[temp] += 1

for k in range(m):
    if repeat[k] >= 2:
        result += (repeat[k] * (repeat[k] - 1)) // 2 # "/"연산을 하면 변수가 float형태가 나오므로 소수점까지 출력하기 때문에 "//" 연산 사용

print(result)


