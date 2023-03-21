import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

index_stack = []
result = [0] * n
answer = ""

for i in range(n):
    while index_stack and data[index_stack[-1]] < data[i]:
        result[index_stack.pop()] = data[i]
    index_stack.append(i)

while index_stack:
    result[index_stack.pop()] = -1

for j in range(n):
    sys.stdout.write(str(result[j]) + " ")