'''
BOJ 2023 신기한 소수
시간제한: 2초

문제해결
자릿수가 한 개인 소수로부터 탐색을 시작해서 2의 배수인 2,4,6,8을 제외한 가지치기 방식을 사용했다
그 다음 현재수 * 10 + a를 계산하고 소수인지 판단한 후 소수라면 자릿수를 하나 늘리는 방식을 사용
'''
import sys

n = int(input())

# 소수 판별
def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def dfs(num, count):
    if count == n:
        # 소수이면 출력
        if isPrime(num):
            print(num)
        return

    for i in [1,3,5,7,9]:
        if isPrime(num * 10 + i):
            dfs(num * 10 + i, count + 1)

# 소수, 소수 자릿수
dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
