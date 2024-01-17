#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e6+3;
int a[N], diff[N];

void solve() {
    int n, q; cin >> n >> q;
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int i = 1; i <= n; ++i) diff[i] = a[i] - a[i-1];
    while (q--) {
        int l , r , z; cin >> l >> r >> z; 
        diff[l] += z; diff[r+1] -= z ;
    }
    for (int i = 1; i <= n; ++i) a[i] = a[i-1] + diff[i];
    for (int i = 1; i <= n; ++i) cout << max(0ll, a[i]) << ' ';
    cout << '\n';
}

signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    solve();
    return 0;
}
