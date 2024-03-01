#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n; ll k; cin >> n >> k;
        vector<pair<int, int>> monsters(n);

        for (int i = 0; i < n; ++i) {
            cin >> monsters[i].second; // Health
        }
        for (int i = 0; i < n; ++i) {
            cin >> monsters[i].first; // Position
            monsters[i].first = abs(monsters[i].first);
        }
        sort(monsters.begin(), monsters.end());
        ll bullets_used = 0;
        bool res = true;
        for (auto &[distance, health] : monsters) {
            ll needed = (ll) health;
            if (needed > (ll) (k) * distance - bullets_used) {
                res = false;
                break;
            }
            bullets_used += needed;
        }
        cout << (res ? "YES" : "NO") << '\n';
    }
    return 0;
}