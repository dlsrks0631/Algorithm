'''
13 8 3 1 -2
5로 나누어 떨어질 때까지 -2
'''

import sys
input = sys.stdin.readline

n = int(input())

result = 0

while n > 0:
    if n%5 == 0:
        result += n // 5
        n -= 5*n//5
        break
    else:
        n -= 2
        result += 1

if n == 0:
    print(result)
else:
    print(-1)

