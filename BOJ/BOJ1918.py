a = input()
stack = [] #스택
res=[] #출력

for x in a:
    if x.isalpha():
        res.append(x)
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while len(stack) != 0 and (stack[-1]=='*' or stack[-1]=='/'):
                res.append(stack.pop())
            stack.append(x)
        elif x == '+' or x == '-':
            while len(stack) != 0 and stack[-1] != '(':
                res.append(stack.pop())
            stack.append(x)
        elif x == ')':
            while len(stack) != 0 and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()

#스택안에 남아있는 값들 pop            
for _ in range(len(stack)):
    res.append(stack.pop())

for i in res:
    print(i,end='')