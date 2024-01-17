#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    int a[n];
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a,a+n);
    int res = 1e5+9;
    for (int i = 0; i < n-1; i++){
        res = min(res, a[i+1] - a[i]);
    }
    cout << res << '\n';
    return 0;
}
