#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> arr(n,0);

    for (int i = 0; i<n; i++) {
        cin >> arr[i];
    }   

    sort(arr.begin(), arr.end());

    int count = 0;

    for(int k = 0; k<n; k++) {
        long target = arr[k];

        int i = 0;
        int j = n-1;

        while(i<j) {
            if(arr[i] + arr[j] == target) {
                if(i != k && j != k) {
                    count += 1;
                    break;
                }
                else if(i == k) {
                    i += 1;
                }
                else {
                    j -= 1;
                }
            }

            else if (arr[i] + arr[j] < target) {
                i += 1;
            }
            else {
                j -= 1;
            }
        }
    }
    cout << count << endl;
    return 0;

}