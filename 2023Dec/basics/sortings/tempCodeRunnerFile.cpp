#include <bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin >> n;
  int a[n];
  for (int i = 1; i <= n; i++){
    cin >> a[i];
  }
  for (int i = 1; i <= n; i++) cout << a[i] << ' ';
  cout << '\n';
  sort(a+1, a+n+1, [](const int &u, const int &v){return u > v;});
  for (int i = 1; i <= n; i++) cout << a[i] << ' ';
}