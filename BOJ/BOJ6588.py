# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다
# n = a+b
# n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다
# 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는
# Goldbach's conjecture is wrong 출력
# 8 --> 8 = 3 + 5

import sys

def isPrime(num):
    if num > 1:
        for i in range(2, int(num**1/2) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False

while True:
    n = int(sys.stdin.readline().rstrip())

    a = []
    b = []

    for i in range(2, n):
        for j in range(2, n):
            if isPrime(i) and isPrime(j) and i+j == n and i < j:
                a.append(i)
                b.append(j)

                a.sort(reverse=True)
                b.sort()

                print("{0} = {1} + {2}".format(n, a[0], b[0]))

    if not n:
        break
