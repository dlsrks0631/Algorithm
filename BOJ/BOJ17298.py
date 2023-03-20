# 크기가 N인 수열
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# 그러한 경우가 없는 경우에 오큰수는 -1
# 수열의 크기 백만


# A = [3,5,2,7]
# > 5 7 7 -1

# 자신보다 index가 크고 data가 커야해
# (index,data)

# 다음꺼 확인 시 자신의 data보다 크면 덱에넣고,
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
result = [-1] * n # 결과값

# for i in range(n):
#     for j in range(i+1, n):
#         if data[i] < data[j]:
#             result[i] = data[j]
#             break



for j in result:
    print(j, end=" ")
    



