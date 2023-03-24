#include <iostream>
#include <vector>
#include <algorithm>

/*
vector > C++ STL(Standard Template Library)에서 제공하는 컨테이너 중 하나
<pair<int, int>>: int형 두 개의 원소를 가지는 pair 타입을 vector의 원소 타입으로 사용한다는 것
*/
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector <pair<int,int>> data(n);
    int max_index = 0;

    for (int i = 0; i < n; i++) {
        cin >> data[i].first;   // 배열의 첫 번째 값
        data[i].second = i;     // 배열의 두 번째 값
    }        
    sort(data.begin(), data.end());

    for (int j = 0; j < n; j++) {
        if (max_index < data[j].second -j) {
            max_index = data[j].second - j;
        }
    }
    cout << max_index + 1;
}