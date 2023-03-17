/*
N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 이 큐에서 몇 개의 원소를 뽑아내려고 한다

> 3가지 연산만 수행 가능
1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어짐
N은 50보다 작거나 같은 자연수, M은 N보다 작거나 같은 자연수

둘째 줄에는 뽑아내려고 하는 수의 위치가 순서대로 주어짐 (위치는 1보다 크거나 같고, N보다 작거나 같은 자연수)

*/
#include <iostream>
#include <deque>

using namespace std;

int main() {
    int result = 0;
    int n, m;

    cin >> n >> m;

    deque<int> d;
    deque<int> d1;
    deque<int> d2;

    for (int i = 1; i<=n; i++) {
        d.push_back(i);
    }
    
    // m번 연산
    while(m--) {
        d1 = d;
        d2 = d;

        int data;
        int d1_res = 0; // 앞에서 뺄 때
        int d2_res = 0; // 뒤에서 뺄 때

        cin >> data;

        // 앞에서 접근할 때
        while (d1.front() != data) {
            d1.push_back(d1.front());
            d1.pop_front();
            d1_res++;
        }
        d1.pop_front();

        // 뒤에서 접근할 때
        while (d2.front() != data) {
            d2.push_front(d2.back());
            d2.pop_back();
            d2_res++;
        }
        d2.pop_front();
        
        if (d1_res > d2_res) {
            result += d2_res;
            d = d2;
        } 
        else {
            result += d1_res;
            d = d1;
        }
    }
    cout << result;

    return 0;
}