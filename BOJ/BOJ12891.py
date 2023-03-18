import sys

input = sys.stdin.readline

check_data = [0] * 4
now_data = [0] * 4
check = 0

def add(c): # 새로 들어온 문자를 처리
    global check_data, now_data, check
    if c == "A":
        now_data[0] += 1
        if now_data[0] == check_data[0]:
            check += 1

    elif c == "C":
        now_data[1] += 1
        if now_data[1] == check_data[1]:
            check += 1

    elif c == "G":
        now_data[2] += 1
        if now_data[2] == check_data[2]:
            check += 1

    elif c == "T":
        now_data[3] += 1
        if now_data[3] == check_data[3]:
            check += 1


def remove(c): # 제거도는 문자를 처리하는 함수
    global check_data, now_data, check
    if c == "A":
        if now_data[0] == check_data[0]:
            check -= 1
        now_data[0] -= 1

    elif c == "C":
        if now_data[1] == check_data[1]:
            check -= 1
        now_data[1] -= 1

    elif c == "G":
        if now_data[2] == check_data[2]:
            check -= 1
        now_data[2] -= 1

    elif c == "T":
        if now_data[3] == check_data[3]:
            check -= 1
        now_data[3] -= 1


s,p = map(int,input().split())  # 4 2
data = list(input())            # G A A T
check_data = list(map(int,input().split()))  # 2 0 1 1 > A C G T

count = 0

# check_data에서 하나도 필요로 하지 않는 경우는 미리 check에 1을 더해줌
for i in range(4):
    if check_data[i] == 0:
        check += 1

# 부분 문자열의 개수 만큼 now_data에 넣어줌
for i in range(p):
    add(data[i])

if check == 4:
    count += 1

# 한 칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열 처리
for i in range(p,s):
    add(data[i])
    remove(data[i-p])

    if check == 4:
        count += 1

print(count)

