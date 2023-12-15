#include <bits/stdc++.h>
using namespace std;

int main(){

    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int a[1000];
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++ i) cin >> a[i];
    sort(a+1, a + n + 1);
    for (int i = 1; i <= n; ++ i) cout << a[i] << ' ';

   // for (int i : a) cout << i << ' ';

}


