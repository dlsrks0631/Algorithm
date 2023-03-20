
word = str(input())
list = []

for i in range(len(word)):
    list.append(word[i:])

list.sort()

for i in list:
    print(i)