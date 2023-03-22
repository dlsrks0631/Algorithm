# BOJ 11286 절댓값 힙 구현하기


import sys
from queue import PriorityQueue

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

queue = PriorityQueue()

for _ in range(n):
    data = int(input())
    if data == 0:
        if queue.empty():
            print("0\n")
        else:
            temp = queue.get()
            print(str((temp[1])) + '\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        queue.put((abs(data), data))

