 # 정수를 저장하는 스택을 구현 (선입 후출)
 # push X : 정수 X를 스택에 넣는다
 # pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
#        스택에 아무것도 없을 시 -1 출력
# size : 스택에 들어있는 정수의 개수 출력
# empty : 스택이 비어있으면 1, 아니면 0 출력
# top : 스택의 가장 위에 있는 정수를 출력. 스택에 있는 정수 없으면 -1

# 첫째 줄에는 주어지는 명령의 수 N

import sys

N = int(sys.stdin.readLine())

stack = []

for i in range(N):
    command = sys.stdin.readLine().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print("{0}".format(len(stack)))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
