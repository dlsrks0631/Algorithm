# # '(' 나오면 stack에 추가
# # ')' 나올 때 두 가지 방법
# # 1. 전꺼가 '('면 지금까지 넣었던 stack 갯수 추가
# # 2. 그 외(전꺼가 ')'면) 앞으로 나오는 ')' 갯수 추가


import sys

result = 0 # 결과값

stack = [] # 스택

cmd = sys.stdin.readline().rstrip()

for i in range(len(cmd)):
    if cmd[i] == '(':
        stack.append('(')

    else:  # cmd[i] == ')'일때
        if cmd[i-1] == '(': # 전꺼가 '('일 때
            stack.pop()
            result += len(stack)

        else: # 전꺼가 ')'일때  
            stack.pop() # ()))
            result += 1 

print("{0}".format(result)) # 결과값 출력

# bar_razor = list(input())
# answer = 0
# st = []

# for i in range(len(bar_razor)):
#     if bar_razor[i] == '(':
#         st.append('(')

#     else:
#         if bar_razor[i-1] == '(': 
#             st.pop()
#             answer += len(st)

#         else:
#             st.pop() 
#             answer += 1 

# print(answer)


