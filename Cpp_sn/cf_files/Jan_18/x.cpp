#include <bits/stdc++.h>
using namespace std;

vector<string> v(3);

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n; //cout << n << '\n';
        for (int i = 0; i <= 2; ++i){
            cin>>v[i];
        }
        int pr = 1;
        for (int i = 0; i < n; ++i){
            char a = v[0][i], b = v[1][i], c = v[2][i];
            if ((a==b && a!=c) || (a!=b && b!=c && a!=c)) ;
            else {
                pr = 0;
            }
        }
        if (pr) cout << "YES\n"; else cout << "NO\n";
    }
    return 0;
}