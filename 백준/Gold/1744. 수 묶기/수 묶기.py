import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
datas_positive = deque()
datas_negative = deque()
one = 0
zero = 0

for _ in range(n):
    data = int(input())
    if data > 1:
        datas_positive.append(data)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        datas_negative.append(data)

datas_positive = sorted(datas_positive, reverse=True)
datas_negative = sorted(datas_negative)

datas_positive = deque(datas_positive)
datas_negative = deque(datas_negative)

result = 0

# 양수 데이터
while len(datas_positive) > 1:
    a = datas_positive.popleft()
    b = datas_positive.popleft()
    result += a*b

if len(datas_positive) > 0:
    result += datas_positive.popleft()

# 음수 데이터
while len(datas_negative) > 1:
    c = datas_negative.popleft()
    d = datas_negative.popleft()
    result += c*d

# 음수 데이터가 남아있고, 데이터 0이 1개도 없으면
if len(datas_negative) > 0 and zero == 0:
    result += datas_negative.popleft()

# 1 처리
result += one

print(result)