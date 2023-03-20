# fn = fn-1 + fn-2
# 0,1,1,2,3,5,,,
# 첫째 줄에 N이 주어짐
# N번째 피보나치 수 출력

n = int(input())

array = []
array[0] = 0
array[1] = 1

def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

n = int(input())
print(f(n))


