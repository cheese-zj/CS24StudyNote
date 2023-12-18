#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll p = 1e9 + 7;
const int N = 1e5 + 9;
ll a[6][N], prefix[6][N];

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0); 
    int n, m; cin >> n >> m; 
    for (int i = 1; i <= n; ++i) cin >> a[1][i];

    for(int i = 2; i <= 5; ++i)
        for(int j = 1; j<=n; ++j)
            a[i][j] = a[i-1][j] * a[1][j] % p;
    
    for(int i = 1; i <= 5; ++i)
        for(int j = 1; j<=n; ++j)
            prefix[i][j] = (prefix[i][j-1] + a[i][j]) % p;

    while (m--) {
        int l, r, k; cin >> l >> r >> k;
        cout << (prefix[k][r] - prefix[k][l-1] + p) % p << '\n';
    }
    return 0;
}