#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--) {
        int n , k ; cin >> n >> k;
        string ans = "";
        for (int i = 0; i < n; i++){
            if (i%2==0) {
                for (int j = 0; j < k; j++) {
                    ans += 'a' + j;
                }
            }
            else {
                for (int j = k-1; j >= 0; j--) {
                    ans += 'a' + j;
                }
            }
        }
        cout << ans <<'\n';        
    }
    return 0;
}