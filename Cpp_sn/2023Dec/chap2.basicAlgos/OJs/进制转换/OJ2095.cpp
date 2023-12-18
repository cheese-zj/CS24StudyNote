#include <bits/stdc++.h>
using namespace std; 
using ll = long long;
const int N = 50; 
int a[N];


int main() {
    int x = 2022;
    int i = 1;
    while (x) {
        a[i++] = x%10;
        x /= 10;
    }

    ll ans = 0;

    for (int j = i; j > 0; j--){
        ans = ans*9 + a[j];
    }

    cout << ans << '\n';

    return 0;
}