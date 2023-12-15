#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<int> v = {10, 3, 5, 7, 2};
    sort(v.begin(), v.end());

    for (int i = 0; i < v.size(); i++) cout << v[i] << ' '; 
}