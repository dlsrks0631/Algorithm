/*
BOJ5430 AC
AC > 배열에 연산을 하기 위해 만든 언어
R - 뒤집기
D - 버리기 > 배열이 비어있는데 D를 사용한 경우에는 에러

첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
*/

/*
string타입의 문자열을 숫자로 바꾸는 함수
stoi = string to int
stof = string to float
stol = string to long
stod = string to double
*/

#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    int test_case; // 수행횟수

    cin >> test_case;

    // 수행횟수만큼 실행
    for(int i = 0; i<test_case; i++) 
    {
        string data; // 수행 함수
        string arr; // 배열
        int n; // 배열 크기
        deque <int> d;
        
        bool success = true;  // 오류가 없을 경우
        bool not_flip = true; // 뒤집히지 않았을 경우

        cin >> data;
        cin >> n;
        cin >> arr;

        string arr_data;

        for (int j = 0; j<arr.length(); j++) {
            if (arr[j] == '[') {
                continue;
            }
            else if (arr[j] >= '0' && arr[j] <= '9') {
                arr_data += arr[j];
            }
            else if (arr[j] == ',' || arr[j] == ']') {
                if(!arr_data.empty()) {
                    d.push_back(stoi(arr_data));
                    arr_data.clear();
                }
            }
        }

        for (int k = 0; k<data.length(); k++) {
            if(data[k] == 'R') {
                not_flip = !not_flip;
            }
            else {
                if (d.empty()) {
                    success = false;
                    cout << "error\n";
                    break;
                }
                else {
                    if (not_flip) {
                        d.pop_front();
                    }
                    else {
                        d.pop_back();
                    }
                }
            }
        }
        if (success) {
            if (not_flip) {
                cout << "[";
                while(!d.empty()) {
                    cout << d.front();
                    d.pop_front();
                    if(!d.empty()) {
                        cout << ",";
                    }
                }
                cout << "]\n";
            }
            else {
                cout << "[";
                while(!d.empty()) {
                    cout << d.back();
                    d.pop_back();
                    if(!d.empty()) cout << ",";
                }
                cout << "]\n";
            }
        }
    }
    return 0;
}