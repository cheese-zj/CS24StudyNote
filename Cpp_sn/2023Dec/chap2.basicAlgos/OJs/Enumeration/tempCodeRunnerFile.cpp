#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--){
        int n, k; cin >> n >> k;
        int a[n];
        map<int, int> mp; 
        for (int i = 0; i < n ; i++){
            int c; cin >> c;
            a[i] = c;
            if (!mp.count(c)) mp.insert(make_pair(c,1));
            else mp[c] ++ ;
        }
        int mf = 0;
        for (auto p : mp){
            mf = max(mf, p.second);
        }
        int ma;
        for (auto p : mp){
            if (p.second == mf){
                ma = p.first;
                break;
            }
        }
        int ans = 0;
        int hold = 0;
        for (auto elem : a){
            if (elem == ma) {
                ans += ceil((float)hold/k);
                hold = 0;
            }
            else{
                hold ++;
            }
        }
        cout << ans << '\n';
    }
}