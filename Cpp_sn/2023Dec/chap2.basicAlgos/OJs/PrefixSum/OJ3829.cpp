#include <bits/stdc++.h>
#define y second
#define x first
#define int long long
using namespace std;
const int N = 1e5 + 9;
int prefix[N], suffix[N];
vector<pair<int,int>> v(N);
signed main(){
    int n; cin >> n;
    for (int i = 1; i <= n; i++ ) {
        cin >> v[i].y >> v[i].x;
    }
    sort(v.begin()+1, v.begin()+1+n);

    int s = 0;
    for (int i = 1; i <= n; i++){
        prefix[i] = prefix[i-1] + s*(v[i].x - v[i-1].x);
        s+=v[i].y;
    }

    s = 0;
    for (int i = n; i >= 1; i--){
        suffix[i] = suffix[i+1] + s*(v[i+1].x - v[i].x);
        s+=v[i].y;
    }

    int m = 1e18;

    for (int i = 1; i <= n; i++){
        m = min(m, prefix[i] + suffix[i]);
    }

    cout << m << '\n';

    return 0;
    
}