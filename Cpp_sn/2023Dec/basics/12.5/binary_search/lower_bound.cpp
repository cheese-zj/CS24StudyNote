#include <bits/stdc++.h>
using namespace std;
int main(){
    int data[200];
    for (int i = 0; i < 200; i++ ) data[i] = 4 * i + 6;
    int target; cin >> target;

    cout << (lower_bound(data, data + 200, target) - data) << '\n';

    return 0;
}