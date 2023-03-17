#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    cin.tie(0);
    cin.sync_with_stdio(0);32

    int n, data;
    queue<int> queue;    
    string str;

    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> str;
        if (str == "push") {
            cin >> data;
            queue.push(data);
        }
        else if (str == "pop") {
            if(queue.size() == 0) cout << "-1\n";
            else {
                data = queue.front();
                queue.pop();
                cout << data << "\n";
            }
        }
        else if (str == "size") {
            cout << queue.size() << "\n";
        }
        else if (str == "empty") {
            cout << queue.empty() << "\n";
        }
        else if (str == "front") {
            if (queue.size() == 0) cout << "-1\n";
            else cout << queue.front() << "\n";
        }
        else if (str == "back") {
            if (queue.size() == 0) cout << "-1\n";
            else cout << queue.back() << "\n";
        }
    }

    return 0;
}
