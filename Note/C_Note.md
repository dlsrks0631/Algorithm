## C / C++ Recap

#### 자료형 = Data Type

- 바이트: 컴퓨터에서 데이터를 처리하는 가장 작은 단위
- 1Byte = 8bit
- 1bit: 0과 1을 표현할 수 있음

- 8bit > 256가지 표현가능 > 0 ~ 255


1. 정수형 %d
   char (1바이트) > 문자를 담는데 쓰임
   short (2바이트)
   long (4바이트)
   long long (8바이트)
   int (4바이트)

```
unsigned char c = 0; // 1Byte 양의 정수만 내포하고 있는 자료형
c = 256 // 8bit를 넘어가는 숫자이므로 0을 출력
```

2. 실수형 %f
   float (4바이트)
   double (8바이트) > double 사용시 %lf 사용

3. unsigned / signed

- 부호 생각 여부
- bool: 진리값(참/거짓)을 저장 (= char)

#### 2진법

- 10진법 > 평소 사용하는 숫자
  ex) 12345 = 1*10^4 + 2*10^3 + 3*10^2 + 4*10^1 + 5\*10^0

- 2진법 > 0, 1로만 구성
  ex) 100110(2) = 1*2^5 + 1*2^2 + 1\*2^1 = 38

#### sizeof 연산자

- sizeof(x): x의 크기를 알려줌
- x: 형 (int, float ... )

#### 형변환

- 실수를 정수형 변수에 담을 수 있지만, 정수를 실수형 변수에 담을 수 없음

* 정수 / 정수 = 정수
* 실수 / 정수 = 실수
* 실수 / 실수 = 실수

#### 입력받기

- scanf("%d %d", &a, &b); // &: 포인터(필수)
- space나 enter로 분리되어 있는 두 숫자를 구별해서 하나의 &d로 인식함

#### char && ASCII Code

- character: 문자 (반각문자 ABCabc12346+/\_)
- ASCII Code: 문자 - 숫자

(ex)

```
int main() {
    char a;

    printf("문자 입력: "); // R
    scanf("%c", &a);

    printf("%c의 ASCII 값: %d", a, a); // R의 ASCII값: 82
}
```

#### 연산자

- 산술연산자: 수학적인 연산 ex) + - _ / = += -= _=
- a += 6 >> a = a + 6
- a %= 6 >> a = a % 6
- a ++ >> a = a + 1
- 비교연산자

* =: 대입 ==: 같다

- 논리연산자 &&(and) ||(or) !(not)

#### 전치 && 후치

(ex)
int main() {
int a = 10;
int b;
b = ++a;

    printf("전치 증가 연산\n");
    printf("a: %d\n", a);   // 11
    printf("b: %d\n", b);   // 11

    a = 10;
    b = a++; // b에 a를 저장하고 a에 1을 더해줌

    printf("후치 증가 연산\n");
    printf("a: %d\n", a);   // 11
    printf("b: %d\n", b);   // 10

}

#### Switch문

(ex)

```
int main() {
    int choice;
    scanf("%d", &choice);

    switch (choice){ // switch(변수이름)
    case 1:
        printf("새 게임.\n");
        break; // > 필수

    case 2:
        printf("불러오기.\n");
        break;

    case 3:
        printf("설정.\n");
        break;
    default:    // == else
        printf("잘못 입력하셨습니다.");
    }
}
```

#### 반복문 while / for

- while(조건식)
- for(반복자 초기화;반복자 조건 체크;반복자 변경(ex)증감식)
- 반복자 초기화 -> 조건 체크 -> 코드 실행 -> 반복자 변경 -> 조건 체크
- continue: 다음 코드 실행하지 않고 반복자 변경으로 넘어감
- break:

* 조건이 만족하는 동안 코드 실행
* 무한반복 > while(true) 사용
* do-while > 조건을 만족하는 지 여부와 상관없이 처음 한 번은 무조건 실행
  (ex)

```
int main() {
    int i = 1;
    do {
        printf("%d\n", i);
        i++;
    } while (i <= 10);

    for (int i = 1; i <= 10; i++) { // for(초기화; 조건; 증감)
        printf("%d\n", i);
    }
}
```

#### 문자열

- 문자 열거
- 문자열 끝에는 항상 Null문자 붙음
- 문자열을 입력 받을 때는 scanf에 포인터 붙이지 않음

(ex)
```
char arr[] = "Hello, world!";
printf("%s\n", arr); // %s > 모든 문자를 보여줌

char s[100];
scanf("%s", s); // 앞에 포인터 안붙임
```

- 문자열 관련 함수 > #include <string.h>
  (ex)

```
#include <string.h>

int main() {
    char str[100] = "Hello";

    int len;
    len = strlen(str); // 문자열 길이 출력 > 5

    char str1[] = "Hello world";
    char str2[100];

    // strcpy(복사를 받아야할 문자열, 원본 문자열);
    strcpy(str2, str1);

    strcat(str, "World"); // 뒤에 문자열을 붙여줌

    // str1과 str2 같으면 0
    // str1이 str2보다 앞에 있으면 -1
    // str1이 str2보다 뒤에 있으면 1
    int cmp = strcmp(str1,str2);

}
```

```
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <stdbool.h>


// 2바이트 문자열을 가져오는 함수
unsigned int GetLength(const wchar_t* _pStr) {
    // d_pStr[1] = 100; 
    // const pointer로 생성했기 때문에 접근해서 수정할 수 없음 / 역참조 수정 불가능

    // 문자 개수 체크 용도
    int i = 0;

    while(true) 
    {
        wchar_t c = *(_pStr+i); // == wchar_t c = _pStr[i];

        if('\0' == c) { 
            break; // null 문자 == '\0'
        } 
        ++i;
    }
    return i;
}

// 문자열 합치기
void StrCat(wchar_t* _pDest, unsigned int _iBufferSize, const wchar_t* _pSrc) {
    // 예외처리
    // 이어붙인 최종 문자열 길이가, 목적지 저장 공간을 넘어서려는 경우
    int iDestLen = GetLength(_pDest);
    int iSrcLen = GetLength(_pSrc);

    // Null 문자 공간까지 계산
    if (_iBufferSize < iDestLen + iSrcLen + 1) {
        assert(nullptr);
    }
    // 문자열 합치기
    // 1. Dest(목적지) 문자열의 끝을 확인 (문자열이 이어 붙을 시작 위치)
    iDestLen; // Dest 문자열의 끝 인덱스
    // 2. 반복적으로 Src 문자열을 Dest 끝 위치에 복사하기
    // 3. Src 문자열의 끝을 만나면 반복 종료
    for(int i = 0; i < iSrcLen + 1; ++i) {
        _pDest[iDestLen + i] = _pSrc[i];
    }
}

int StrCmp(const wchar_t* _left, const wchar_t* _right) {
    int leftLen = GetLength(_left);
    int rightLen = GetLength(_right);

    int iLoop = leftLen;
    int iReturn = 0;

    if (leftLen < rightLen) {
        iLoop = leftLen;
        iReturn = -1;
    }
    else if(leftLen > rightLen) {
        iLoop = rightLen;
        iReturn = 1;
    }

    for(int i = 0; i < iLoop; ++i) {
        if(_left[i] < _right[i]) {
            return -1;
        }
        else if (_left[i] > _right[i]) {
            return 1;
        }
    }
    return iReturn;
}


int main() {
    wchar_t szName[10] = L"Raimond";

    // == int iLen = wcslen(szName);
    int iLen = GetLength(szName);  // 7

    printf("%d", &iLen);

    // 문자열 이어 붙이기
    wchar_t szString[100] = L"abc";
    StrCat(szString, 10, L"def");

    int iRet = wcscmp(L"cac", L"ca");
    iRet = StrCmp(L"abc", L"abcdef");


    return 0;
}
```

#### 비트 연산자 / define

- 가독성과 유지보수를 위해 사용
- 비트 곱(&), 합(|), xor(^), 반전(~)
- 비트 단위로 연산을 진행

* & 둘다 1인 경우 1
* | 둘중 하나라도 1 이면 1
* ^ 같으면 0, 다르면 1

(ex)

```
#define HUNGRY   0*001
#define THIRSTY  0*002
#define TIRED    0*004
#define FIRE     0*008

#define HUNGRY2   0*010
#define THIRSTY2  0*020
#define TIRED2    0*040
#define FIRE2     0*080

unsigned char byte = 13;
byte <<= 3; // 2^n 배수
byte >>= 1; // 2^n 나눈 몫

unsigned int iStatus = 0;

// 상태 추가
iStatus |= HUNGRY;
iStatus |= THIRSTY;

// 상태 확인
if (iStatus & THIRSTY) {}

// 특정 자리 비트 제거
iStatus &= ~THIRSTY;
```

#### 변수

> 1. 지역변수
>    함수 안에서 사용되는 변수
>    같은 지역끼리 우선순위가 높음(괄호 안에 선언된 변수)
>    같은 지역에서 같은 이름의 변수 지정 X
> 2. 전역변수
>    main 함수 밖에 선언된 변수
> 3. 정적변수(static)
>    생성된 위치 즉, 생성된 파일에서만 인식 범위를 가짐
>    전역변수는 다른 함수에 접근할 수 있지만 정적변수는 접근하지 못함
>    함수 안에서 사용된 전역변수 초기화는 한 번만 실행되며, 반복적으로 함수 선언 시 초기화 구문은 실행되지 않음
> 4. 외부변수(extern)

#### 메모리 영역

> 1. 스택 영역 > 지역변수가 사용하는 메모리 영역
> 2. 데이터 영역 > (전역/정적/외부)변수가 사용하는 메모리 영역
>    프로그램 시작 시 생성
>    프로그램 종료 시 해체
> 3. 읽기 전용(ROM(코드))
> 4. 힙 영역(동적할당) 
>    동적할당: 프로그램이 실행 도중 원하는 만큼의 메모리를 요청할 수 있

#### 문자 

* char(1바이트), wchar(2바이트)
(ex)
```
char c = 'a';
wchar_t wc = L'a';

char szChar[10] = "abcdef";
char szWChar[10] = L"abcdef;
```

#### 함수 

* 명령어 집합체
* 코드 != 메모리 영역
(ex)

```
int Add(int left, int right) { > left, right 변수도 Add 안에 생성된 변수들로 Add라는 함수 안의 지역변수
    return left + right
}

data = Add(10,20);
```

- 함수에 반환값이 없을 경우 void 사용
  (ex)

```
int g_i = 0;

void Test() {
    ++g_i++
}
```

#### 재귀함수

- 함수 안에서 자기 자신을 호출하는 것
  (ex) Factorial

```
int Factorial__Recursion(int count) {
    if (1 == count) {
        return 1;
    }

    return count * Factorial__Recursion(count -1)
}

int main() {
    printf("%d", Factorial__Recursion(4));

    return 0;
}
```

(ex) 피보나치 수열

```
int Fibonacci__Recursion(int count) {
    if ( count == 1 || count == 2) {
        return 1;
    }
    return  Fibonacci__Recursion(count-1) + Fibonacci__Recursion(count-2);
}

int main() {
    printf("%d", Fibonacci__Recursion(4));

    return 0;
}
```

#### 배열

- 중괄호로 초기화
- 2차원 배열 > [세로][가로]
  (ex)

```
int arr1[10] = {} // 빈괄호로 생성시 전부 0으로 생성
int arr2[3][4] = {
    {1,2,3,4},
    {2,3,4,5},
    {3,4,5,6}
};
```

#### 구조체

- 구조체: 사용자 정의 자료형(데이터 타입)
- typedef:타입을 재정의 해주는것 예시:typedef int INT;in를INT로 바꿔쓴다
- truct:구조체
- struct \_TagMyST: 구조체 이름
- MYST:typedef을 사용해 다시 정한 이름, C++에선 typedef 생략 가능

(ex)

```
typedef struct _TagMyST
{
	int a;//a라는 변수는 없고 int를 지칭하는 단어로 사용
	float f;
}MYST;//만들어낸 자료형 이름

typedef struct _tagBig
{
	MYST k;//구조체 안에 구조체 가능
	int i;
	float c;
}BIG;

typedef int INT;

int main()
{
	int arr[10] = { 1,2,3,4,5,6,7, };//해당 자리에 숫자가 없으면 0으로 초기화
	//구조체
	MYST t = {100,3.14};//구조체도 초기화 가능
	MYST t;//4byte+4byte총합 8byte
	t.a = 10;//.a는int형
	t.f = 10.23423;//.f는 실수형

	int iSize = sizeof(MYST);//sizeof:()안의 자료형의 크기를 알려준다


	int a;
	INT a;

	return 0;
}
```

#### 분할 구현

- 코드 관리의 용이성을 위해 사용
  (ex)

```
// func.h > 함수 선언
int Add(int a, int b);
// func.cpp > 선언된 함수 구현
#include "func.h"

int Add(int a, int b) {
    return a+b;
}
// main > 함수 사용
#include "func.h"
#include "func.cpp"
int main {
   printf("%d", Add(1,2));
}
```

- 헤더파일에 함수를 구현하지 않는 이유: 중복선언을 피하기 위함

#### 포인터 변수
* 주소를 저장하는 변수
* 주소의 단위: BYTE
* 주소를 표현하는 방식은 정수표현방식으로 4바이트
    - 비트 단위로 주소를 받을 수 없음
    - 포인터의 연산은 일반적인 정수의 연산을 따라가지 않음
    - 주소값이 1 증가하는 의미는 다음 int 위치로 접근하기 위해서 sizeof(int) 단위로 증가하게 됨
* 메모리 안에 데이터는 같지만 관점에 따라 해석이 달라질 수 있음
* 자료형(해당 포인터에게 전달된 주소를 해석하는 단위) + *변수명
    - 앞에 나오는 자료형은 전달된 주소를 어떤 관점으로 바라볼지 정하는 것
    - 그렇기에 주소를 저장하는 변수의 크기는 다 같음 !!!
    - 포인터의 크기는 가변길이로 운영체제 플랫폼에 따라 다름 (32bit > 4byte / 64bit > 8byte) 
(ex)
```
int main() {
    int i = 100;
    float f = 3.f;

    // 정수관점으로 보는 포인터 
    // (어떤 관점으로 전달된 주소를 볼지 int,char,float...)* 변수명
    int* pInt = (int*)&f; // &f = f의 주소

    // 주소로 접근 > 변수명 앞에 *
    i = *pInt;
    // pInt는 f의 주소를 정수관점으로 바라보기 때문에 i는 1077936128이라는 큰 숫자가 나옴 
}
```

#### 포인터 && 배열 

* 배열의 특징
    - 메모리가 연속적인 구조 !!
    - 배열의 이름은 배열의 시작 주소이다
* 해당 함수 쪽에서 선언한 지역변수를 수정하고 싶을 때 포인터 사용

(ex)
```
int main() {
    int iArr[10] = {}; // iArr > 배열의 시작 주소

    // int 단위로 접근
    *(iArr + 0) = 10; // iArr[0] = 10;
    *(iArr + 1) = 11; // iArr[1] = 11;
}
```
```
// 포인터 이해
int main() {
    short sArr[10] = {1,2,3,4,5,6,7,8,9,10};
    int *pI = (int*)sArr;
    int iData = *((short*)(pI+2));
    printf("%d\n", iData); // 5

    char cArr[2] = {1,1};
    short* pS = (short*)cArr;
    iData = *pS;
    printf("%d\n", iData); // 257
}
```

#### const && 포인터
* 상수를 선언할 때 쓰임
- 일반적으로 변수처럼 수정할 순 없기에 포인터로 접근해서 수정해야함
* l-value(변수) = r-value(상수)

(ex)
```
int main() {
    int a = 0;
    int* pInt = &a;

    *pInt = 1;
    pInt = nullptr;

    // ===========
    // const 포인터
    // ===========
    int b = 0;
    const int* pConstInt = &a;
    // 오류 *pConstInt = 100; // 원본 데이터를 바꿀 수 없음

    // ===========
    // 포인터 const
    // ===========
    int* const pIntConst = &a;
    *pIntConst = 400;
    // 오류 pIntConst = &b; // 가리키는 원본을 수정할 수 없음

    // 초기화 시 가리킨 대상만 가리킴, 가리키는 원본을 수정 할 수 없음
    const int* const pConstIntConst = nullptr;
}
```

#### void 
* 리턴값이 없는 함수의 자료형, 반환 타입을 적어주지 않아도 됨
* void * - void 포인터
- void *에 주소를 넣어줬을 때 그 주소의 원형을 특정 데이터 타입으로 해석하지 않기 때문에 어떠한 타입의 변수의 주소든 다 저장할 수 있음 
- 역참조 / 주소연산 불가 
(ex)
```
{
    void *pVoid = nullptr;
    int a = 0;
    float f = 0.f;
    double d = 0.;

    pVoid = &a;
    pVoid = &f;
    pVoid = &d;

    // *pVoid;   역참조 불가 - 오류
    // pVoid + 1 주소 연산 불가  - 오류
}
```

#### deque 
* deque(Double-ended queue): 양쪽 끝에서 원소를 삽입/삭제할 수 있는 자료구조
* vector와 유사하지만 원소 삽입/삭제가 빈번한 경우 deque가 효율적
(ex)
```
#include <iostream>
#include <deque>

using namespace std;

int main() {
    deque<int> d1 {1,2,3}; // 초기 값으로 {1,2,3}을 가지는 deque 생성
    deque<int> d2;  // 비어있는 deque 생성

    d2.push_back(1);  // 뒤쪽에 1 추가
    d2.push_front(2); // 앞쪽에 2 추가

    d1.pop_back(); // 뒤쪽 원소 제거
    d1.pop_front(); //앞쪽 원소 제거

    for (auto it = d1.begin(); it != d1.end(); ++it) {
        cout << *it << endl; // 각 원소 출력
    }

    return 0;
}
```

