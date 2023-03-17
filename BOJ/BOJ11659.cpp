#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    
    vector<int> sum_numbers(n+1);
    int temp = 0;
    for (int i = 0; i < n; i++) {
        temp += numbers[i];
        sum_numbers[i+1] = temp;
    }
    
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        cout << sum_numbers[b] - sum_numbers[a-1] << "\n";
    }
    
    return 0;
}