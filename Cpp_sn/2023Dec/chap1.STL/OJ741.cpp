#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n; cin >> n;
    priority_queue<int, vector<int>, greater<ll>> pq;
    for (int i = 0; i < n ; i++ ){
        int x; cin >> x;
        pq.push(x); 
    }
    ll ans = 0;
    while (pq.size() >= 2){
        ll x = pq.top(); pq.pop();
        ll y = pq.top(); pq.pop();
        ans += x + y;
        pq.push(x+y);
    }

    cout << ans << '\n';
    return 0;

}