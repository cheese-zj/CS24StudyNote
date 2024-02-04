#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

void solve() {
    int x, n; cin >> x >> n;
    int s = x;
    for (int i = 1; i*i <= x; i ++){
        if (x%i) continue;
        if (i >= n) {
            s = min(s,i);
        }
        if (x/i >= n) {
            s = min(s, x/i);
        }
    }
    int ans = x/s;
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
