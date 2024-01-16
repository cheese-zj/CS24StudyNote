#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e6+9;
int a[N][N], diff[N][N];

signed main() {
    int n, m, q; cin >> n >> m >> q;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) cin >> a[i][j];
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) diff[i][j] = a[i][j] - a[i][j-1];
    while (q--) {
        int x1, x2, y1, y2, c; cin>>x1>>x2>>y1>>y2>>c;
        for (int i = x1; i <= x2; i++) {
            diff[i][y1] += c; diff[i][y2+1] -= c;
        }
    }
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) a[i][j] = a[i][j-1] + diff[i][j];

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++) cout << a[i][j] << ' '; cout << '\n';}

    return 0;
}