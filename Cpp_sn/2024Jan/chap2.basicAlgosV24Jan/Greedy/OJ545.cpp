#include <bits/stdc++.h>
using namespace std;
using ll = long long;
priority_queue<ll, vector<ll>, greater<ll> > pq; 

int main() {
    int n; cin >> n;
    while (n--) {
        ll x; cin >> x ; pq.push(x);
    }
    int ans = 0;
    while (pq.size() > 1){
        ll x = pq.top(); pq.pop();
        ll y = pq.top(); pq.pop();
        pq.push(x+y);
        ans += x+y;
    }
    cout << ans << '\n';
    return 0; 
}
