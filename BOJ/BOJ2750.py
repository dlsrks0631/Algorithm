# 버블 정렬 - 수 정렬하기

n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

loop = n-1

for i in range(loop):    # 라운드 수(loop 개수)
    for j in range(loop-i):  # 정렬 범위 > 라운드 수만큼 적어짐
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp

for k in range(n):
    print(data[k])