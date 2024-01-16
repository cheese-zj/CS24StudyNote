#include <bits/stdc++.h>
//#define int long long
using namespace std;
const int N = 1e6+9;
int o, w, ans;

int main() {
    int n; cin >> n; 
    int z = 2;
    for (int i = 1; i <= n; i ++){
        string s; cin >> s;
        for (char x : s) if (x=='o') (o++); else (w++);
        while (w && o >=z) {
            w--, o--; ans++;
            if (z==2) z = 1;
        }
        cout << ans << '\n';
    }
     
    return 0;
}