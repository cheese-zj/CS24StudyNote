#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--){
        int n, k; cin >> n >> k;
        map<int, int> mp; 
        for (int j = 0; j < n ; j++){
            int c; cin >> c;
            if (!mp.count(c)) mp.insert(make_pair(c,1));
            else mp[c] ++ ;
        }
        
        int ma = 0;
        for (auto p : mp){
            ma = max(ma, p.second);
        }
        for (auto p : mp){
            if (p.second == ma) cout << ceil((double)(n-p.second)/k);
        }
    }
}