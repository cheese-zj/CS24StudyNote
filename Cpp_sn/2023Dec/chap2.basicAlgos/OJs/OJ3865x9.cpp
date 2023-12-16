#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n, k ; cin >> n >> k;
    int a = 0;
    while (n--) {
        int x; cin >> x;
        if (x % 2 == 1) a++;
    }
    if (a%2 == 1) cout << "Alice" << '\n';
    else cout << "Bob" <<'\n';
    // cout << a << ' ' << b <<' ';
    return 0;  
}