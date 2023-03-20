# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다

# 수빈이는 걷거나 순간이동 할 수 있음
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 동생을 찾을 수 있는 가장 빠른 시간
# 5 17 --> 4
# 5 10 11 12 13 14 15 16 17
# 5-10-9-18-17
0

from collections import deque
import sys

n,k = map(int,sys.stdin.readline().split())

def bfs():
    queue = deque([n])

    while queue:
        visited[n] = 0
        v = queue.popleft()

        if v == k:
            return visited[v] 
        
        for i in (v-1,v+1,v*2):
            if 0 <= i <= 100000 and visited[i] == False:
                visited[i] = visited[v] + 1
                queue.append(i)

visited = [False]*100001

print(bfs())



# def bfs(num):
#     queue = deque([num])

#     while queue:
#         visited[num] = 0
#         num = queue.popleft()

#         if num == k:
#             return visited[num]

#         for i in (num-1,num+1,2*num):
#             if 0 <= i <= 100000 and visited[i] == False:
#                 visited[i] = visited[num] + 1
#                 queue.append(i)