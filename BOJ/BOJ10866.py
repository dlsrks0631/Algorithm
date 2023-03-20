# appendleft = 큐 맨앞에 원소 삽입
# append = 큐 맨 뒤에 원소 삽입

import sys

from collections import deque

queue = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        queue.appendleft(cmd[1])

    elif cmd[0] == 'push_back':
        queue.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)

    elif cmd[0] == 'pop_back':
        if queue:
            print(queue[len(queue)-1])
            queue.pop()
        else:
            print(-1)

    elif cmd[0] == 'size':
        print("{0}".format(len(queue)))

    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    else:
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
            
