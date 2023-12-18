#include <bits/stdc++.h>
using namespace std; using ll = long long;
const ll p = 1e9+7;
int main() {
    int n,m; cin >> n >> m;
    int a[n+1];
    a[0] = 0;
    for (int i = 1; i <= n; i++) {
        int x; cin >> x ;
        a[i] = x;
    }
    //for (int i = 0; i <= n; i++ ) cout << a[i] << ' '; cout << '\n';
    while (m--) {
        int l, r, k; cin >> l >> r >> k;
        int prefix[n]; prefix[0] = 0;
        // int x[n+1];
        // for (int i = 0; i <= n; i++) x[i] = pow(a[i], k);
        // for (int i = 0; i <= n; i++ ) cout << x[i] << ' '; cout << '\n';
        for (int i = 1; i <= n; i++){
            prefix[i] = prefix[i-1] + pow(a[i], k);
        }
        // for (int i = 0; i <=n ; i++) cout << prefix[i] << ' '; cout << '\n';
        cout << (prefix[r] - prefix[l-1]) % p << '\n';
    }
}