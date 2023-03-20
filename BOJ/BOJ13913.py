'''
숨바꼭질4

join

'''

from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
check = [0] * 100001


def move(now):
    data = []
    temp = now

    for _ in range(visited[now] + 1):
        data.append(temp)
        temp = check[temp]
        #리스트를 문자열로 바꿔서 뒤에서부터 합침
    print(' '.join(map(str, data[::-1])))


def bfs():
    queue = deque([n])

    while queue:
        now = queue.popleft()

        if now == k:
            print(visited[now])

            # 어떻게 움직였는지 출력
            move(now)
            return  # 빠져나옴

        for next_node in (now - 1, now + 1, now * 2):
            if 0 <= next_node <= 100000 and visited[next_node] == 0:
                visited[next_node] = visited[now] + 1
                queue.append(next_node)
                check[next_node] = now

bfs()
