#include <bits/stdc++.h>
using namespace std;

int f(int x) {
    int res = 0;
    while (x) {
        res += x%10;
        x /= 10;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t; 
    while (t--) {
        int n; cin >> n;
        int ans = 0; int c = 1;
        while (c < n){
            c += f(c);
            ans ++; 
        }
        if (c == n) cout << ans << '\n'; 
        else cout << -1 << '\n';
    }

    return 0;
}