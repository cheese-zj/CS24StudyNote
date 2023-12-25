#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e7+9;
int a[N], prefix[N];

signed main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        for (int i = 1; i <= n; i++) cin >> a[i];
        sort(a+1, a+1+n);
        for (int i = 1; i <= n; i++) prefix[i] = prefix[i-1] + a[i];

        int ans = 0;
        for (int i = 0; i <= k; i++){
            int diff = prefix[n-(k-i)] - prefix[2*i];
            ans = max(ans, diff);
        }
        cout << ans <<'\n';
    
    }
    return 0;
}