import sys

input = sys.stdin.readline

n,m = map(int,input().split())

numbers = list(map(int,input().split()))
sum_numbers = [0]

temp = 0
print(numbers)
for i in numbers:
    temp = temp + i
    sum_numbers.append(temp)
print(sum_numbers)

for i in range(m):
    a,b = map(int,input().split())
    print(sum_numbers[b]-sum_numbers[a-1])