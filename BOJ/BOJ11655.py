# ex) Baekjoon Online Judge --> Onrxwbba Bayvar Whqtr
# ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다
# 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다
# ex) One is 1 --> Bar vf 1
# 영어 알파벳을 13글자씩 밀어서 만듬

# 97(a) ~ 122(z)
# 122 + 13= 135 --> 97+13 = 110
# 121 + 13 = 134 ---> 97+12 = 109


word = input()

for i in word:
    if ord(i) >= 110 and i.islower() and i.isdigit() == False:
        print(chr(ord(i)+13-26), end = '')

    elif 97 <= ord(i) <= 109 and i.islower() and i.isdigit() == False:
        print(chr(ord(i)+13),end='')

    elif 65 <= ord(i) <= 77 and i.isupper() and i.isdigit() == False:
        print(chr(ord(i)+13),end='')

    elif 78 <= ord(i) <= 90 and i.isupper() and i.isdigit() == False:
        print(chr(ord(i)+13-26), end = '')

    else:
        print(i,end='')