# 첫째 줄에 피연산자의 개수가 주어짐
# 둘째 줄에는 후위표기식이 주어짐
# 셋째 줄부터는 피연산자에 대응하는 값이 주어짐
# ex) 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해달하는 값
# 계산 결과를 소숫점 둘째 자리까지 출력

# 후위 표기식 
# A + B * C --> BC*A+

# ex)
# 1 --> 변수 갯수
# AA+A+ --> A+A+A
# 1 (A값)

# 출력 = 3

import sys

n = int(sys.stdin.readline().rstrip())

cmd = sys.stdin.readline().rstrip()

stack = []

num_list = [0] * n

for i in range(n):
    num_list[i] = int(sys.stdin.readline().rstrip())

for i in cmd:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i)-ord('A')])

    else :	
        num1 = stack.pop()	
        num2 = stack.pop()				
        	
        if i =='+' :
            stack.append(num2+num1)
        elif i == '-' :
            stack.append(num2-num1)
        elif i == '*' :
            stack.append(num2*num1)
        elif i == '/' :
            stack.append(num2/num1)

print("%.2f" %stack[0])



