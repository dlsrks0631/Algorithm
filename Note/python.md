# Join Method
* 파이썬 문자열(string)과 리스트(list) 자료형에 적용할 수 있는 메서드
* 문자열이나 리스트의 각 요소를 지정한 구분자(seperator)로 연결하여 하나의 문자열로 만들어준다
* 구분자를 지정하지 않으면 기본적으로 빈문자열이 구분자로 사용된다
(ex)
```
my_list = ['apple', 'banana', 'orange']
result = ','.join(my_list)
print(result) # apple,banana,orange

my_str = 'hello'
result = '-'.join(my_str)
print(result)  # h-e-l-l-o
```