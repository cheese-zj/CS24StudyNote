// reverse(a, a+n) **address**

#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v = {1,2,3,4,5};
    for (int i : v) cout << i << ' ';
    cout << '\n';
    reverse(v.begin(),v.end());
    for (int i : v) cout << i << ' ';
}