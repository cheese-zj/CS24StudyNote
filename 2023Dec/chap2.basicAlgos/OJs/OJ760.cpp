#include <bits/stdc++.h>
using namespace std; 
const int N = 20;
int a[N];

int dfs(int dep){
    int res = 1;
    for (int i = 1; i <= a[dep-1]/2; i++) {
        a[dep] = i; 
        res += dfs(dep+1); 
    }
    return res;
} 

int main() {
    int n; cin >> n ;
    a[1] = n;
    cout << dfs(2) << '\n';
    return 0;
}