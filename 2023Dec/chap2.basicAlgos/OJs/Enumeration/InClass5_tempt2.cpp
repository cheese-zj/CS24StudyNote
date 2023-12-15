#include <bits/stdc++.h>
using namespace std;
const int N = 1e5;
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--){
        int mins = 1e5;
        int a[N];
        int n, k; cin >> n >> k;
        for (int i = 0; i < n ; i++) cin >> a[i];
        for (int c = 0; c < 60 ; c++){
            int ans = 0;
            for (int i = 0; i<n; ){
                if (a[i] == c) i++;
                else {
                    i += k;
                    ans ++;
                }
            }
            mins = min(mins, ans);
        }
        cout << mins << '\n';
    }
    return 0;
}