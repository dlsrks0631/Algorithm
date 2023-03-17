/*
BOJ 1874 스택 수열
첫 줄에 n(1<=n<=100,000)이 주어진다
둘째 줄부터 n개의 줄에는 수열을 이루는 1 이상 n이하의 정수가 하나씩 순서대로 주어짐
같은 정수가 두 번 나오는 일은 없다
*/

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<int> stk;
    string result;

    int count = 1;
    int n;
    cin >> n;

    for(int i = 0; i<n; i++) {
        int x;
        cin >> x;

        while (count <= x) {
            stk.push(count);
            count += 1;
            result += "+";
        }

        if (stk.top() == x) {
            stk.pop();
            result += "-";
        }
        else {
            cout << "NO";
            return 0;
        }
    }
    for (int j = 0; j < result.size(); j++) {
        cout << result[j] << '\n';
    }
}