#include <bits/stdc++.h>
using namespace std; 
using ll = long long; 
const int N = 100;
int a[N];
int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        string s; cin >> s;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] <= '9' && s[i] >= '0') a[i+1] = s[i] - '0';
            else a[i+1] = s[i] - 'A' + 10;
        }

        ll x = 0;
        for (int i = 0; i <= s.length(); i++){
            x = x*n + a[i];
        } 
        
        vector<char> v;
        while (x) {
            if (x%m <= 9 && x%m >= 0) v.push_back(x%m + '0');
            else v.push_back(x % m - 10 + 'A');
            x /= m;
        }

        reverse(v.begin(), v.end());
        for (char c : v) cout << c; cout << '\n';
        
    }     
}