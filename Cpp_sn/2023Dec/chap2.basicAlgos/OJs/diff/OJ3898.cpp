#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 * 2 + 9;
int a[N], diff[N];
signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);


    int n, w; cin >> n >> w;

    for (int i = 0; i <= N; i++)a[i] = w;
    for (int i = 0; i <= N; i++)diff[i] = a[i] - a[i-1];

    while (n--) {
        int l, r, c; cin >> l >> r >> c;
        diff[l] += c; diff[r] -= c;
    }

    for (int i = 0; i <= N; i++) a[i] = a[i-1] + diff[i];
    for (int i = 0; i <= N; i++) if (a[i] < 0) cout << "NO\n";

     cout << "YES\n";

    return 0;

}