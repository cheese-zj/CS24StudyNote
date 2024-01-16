#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e6+9;

int a[N], diff[N];

signed main() {
    int n, q; cin >> n >> q;
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++) diff[i] = a[i] - a[i-1];
    while (q--) {
        int l, r, c; cin >> l >> r >> c; 
        diff[l] += c; diff[r+1] -= c;
    }
    for (int i = 1; i <= n; i++) a[i] = a[i-1] + diff[i]; 
    for (int i = 1; i <= n; i++) cout << a[i] << ' ';
    cout << '\n';
    return 0;
}