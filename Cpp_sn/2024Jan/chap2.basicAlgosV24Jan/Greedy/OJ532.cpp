#include <bits/stdc++.h>
using namespace std;
const int N = 1e5;
int a[N];

int main( ){
    int t, n; cin >> t >> n;
    for (int i = 0; i < n ; i++) {
        cin >> a[i];
    }
    sort (a, a+n);
    int l = 0, r = n-1, ans = 0;
    while (l <= r) {
        ans++;
        if (l==r) break;
        if (a[l] + a[r] <= t) {
            l++, r--;
        } else {
            r--;
        }
    }
    cout << ans << '\n'; 
    return 0;
}