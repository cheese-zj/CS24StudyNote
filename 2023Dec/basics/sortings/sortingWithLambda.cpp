#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<int> v = {10, 5, 6, 3, 9, 12};

    sort(v.begin(), v.end(), [](const int &u, const int &v){return u > v;});

    for (int i : v) cout << i << ' ';
}