#include <bits/stdc++.h>
//#define int long long
using namespace std;
const int N = 1e6+9;
multiset<string> ms;

void f(string s) {
    int o = 0; int w = 0;
    for (char x : s) if (x=='o') (o++); else (w++);
    cout << min(o-1, w) << '\n';
}

int main() {
    int n; cin >> n; 
    for (int i = 1; i <= n; i ++){
        string s; cin >> s;
        ms.insert(s);
    }
    return 0;
}