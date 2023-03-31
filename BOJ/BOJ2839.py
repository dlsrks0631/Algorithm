'''
18 

5kg, 3kg


'''

import sys

input = sys.stdin.readline

n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        n -= 5
        result += 1
    else:
        n -= 3
        result += 1
    
if n == 0:
    print(result)
else:
    print(-1)