#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int N = 1e5+9;
int a[N], prefix[N];
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    string s; cin >> s;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        if (s[i] == 'L') a[i+1] = 1;
        else if (s[i] == 'Q') a[i+1] = -1;
    }
    
    for (int i = 1; i <= n; i++){
        prefix[i] = prefix[i-1] + a[i];
    }

    int m = 0;
    for (int i = 1; i <= n-1; i++){
        for (int j = i+1 ; j <= n; j++){
            if (prefix[j] - prefix[i-1] == 0) m = max(m, j-(i-1));
        }
    }

    cout << m << '\n';
    
    return 0;
}