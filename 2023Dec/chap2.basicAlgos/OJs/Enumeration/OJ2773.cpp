#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int x, y; cin >> x >> y;
    map<int, int> m;
    for (int i = 0; i < x; i++){
        for (int j = 0; j < y; j++){
            int z; cin >> z;
            if (m.count(z) == 0) m.insert(make_pair(z,1));
            else m[z] ++;
        }
    }
    for (auto p : m){
        if (p.second > (double)x*y/2) cout << p.first << '\n';
    }
    return 0;
}