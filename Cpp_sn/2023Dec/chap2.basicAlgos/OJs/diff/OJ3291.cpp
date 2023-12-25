#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e7 + 9;
int a[N], diff[N]; 
signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int n, m ; while(cin >> n >> m) {
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        for (int i = 1; i <= n; i ++) {
            diff[i] = a[i] - a[i-1];
        }
        while (m--) {
            int x, y, z; cin >> x >> y >> z; 
            diff[x] += z; diff[y+1] -= z;
        }

        for (int i = 1; i <= n; i++) a[i] = a[i-1] + diff[i];

        for (int i = 1; i <= n; i++){
            cout << a[i] << ' ';
        }
        cout << '\n';
    }

    return 0;
}