#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--){
        int n; cin >> n;
        int a[n];
        int ans = 0;
        for (int i = 0; i < n ; i++) {
            cin >> a[i]; if(a[i] == 0) ans ++, a[i]++;
        }
        int temp = 0;
        for (int i : a) {
            temp += i;
        }
        if (temp == 0) ans++;
        cout << ans << '\n';
    }
    return 0;
}