#include <bits/stdc++.h> 
using namespace std;

int f(int x) {
    if (x == 0) return 1;
    if (x % 2 == 0) return f(x/2);
    else return f(x-1)+1;
}

int main() {
    int n; cin >> n;
    cout << f(n) <<'\n';
    return 0;
}