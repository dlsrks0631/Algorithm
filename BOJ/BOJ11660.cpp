#include <iostream>
#include <algorithm>

#define MAX 1024

using namespace std;

int arr[MAX+1][MAX+1];
int sum[MAX+1][MAX+1];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;
    cin>>n>>m;

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cin >> arr[i][j];
            sum[i][j] = sum[i-1][j]+sum[i][j-1] - sum[i-1][j-1]+arr[i][j];
        }
    }

    int x1,y1,x2,y2;
    int ans;

    for(int i=0;i<m;i++)
    {
        cin>>x1>>y1;
        cin>>x2>>y2;
        ans = sum[x2][y2] - sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1];
        cout<<ans<<'\n';
    }
    return 0;
}