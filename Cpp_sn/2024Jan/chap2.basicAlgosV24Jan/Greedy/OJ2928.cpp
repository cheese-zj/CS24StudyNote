#include <bits/stdc++.h>
using namespace std;
const int N = 1e6+9;
char s[N];
int main()
{
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n, x; cin >> n >> x;
    cin >> s + 1;
    sort(s+1,s+1+n);
    if (s[1] == s[n]) {
        for (int i = 1 ; i <= n / x + (n % x ? 1 : 0); i++) cout << s[i];
    } else if (s[x] == s[1]) {
        for (int i = x; i <= n; i++) cout << s[i];
    } else {
        cout << s[x];
    }


  return 0;
}