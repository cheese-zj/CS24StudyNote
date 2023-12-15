#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n; cin >> n;
    int temp;
    map<int, int> m;
    for (int i = 0; i < n; i++){
        cin >> temp;
        if (m.count(temp) == 0) m.insert(make_pair(temp,1));
        else {
            m[temp]++;
        }
    }
    int res = 0;
    for (auto it : m){
        if (it.first != it.second) res++;
    }
    cout << res;
}