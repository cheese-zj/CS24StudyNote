#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n; 
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i ++) cin >> a[i];
    cout << *max_element(a, a+n) << '\n';
    cout << *min_element(a, a+n) << '\n';

    long long sum = 0;

    for (int i = 0; i < n; i++) sum += a[i];

    cout << fixed << setprecision(2) << 1.0 * sum / n << '\n';
}