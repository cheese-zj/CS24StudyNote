#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b,c;
    int n; cin >> n >> a >> b >> c;
    int ans = n;
    for (int i = 1; i <= n; i++){
        if (i%a == 0 || i%b == 0 || i%c == 0) ans --;
    }
    cout << ans << '\n';
    return 0;
}

// OJ152