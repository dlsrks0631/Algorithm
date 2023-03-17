/*
첫째 줄에는 테스트 케이스의 개수 T (1<=T<=20)
각 테스트 케이스의 첫째 줄에 지원자의 숫자 N (1<=N<=100,000)
각 테스트 케이스에 대해서 선발할 수 있는 신입사원의 최대 인원수
*/ 

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        int N;
        cin >> N;

    }
}

/*
1번: 3 2
2번: 1 4
3번: 4 1
4번: 2 3
5번: 5 5
서류심사 기준으로 오름차순 정렬 후 면접시험 기준으로 뽑음
1 4
2 3
3 2
4 1
5 5
*/