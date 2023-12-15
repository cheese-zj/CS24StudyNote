#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(0), cout.tie(0), cin.tie(0);
  int m; cin >> m;
  queue<string> v, n;
  char q;
  for (int i = 0; i < m ; i ++ ){
    string cmd; cin >> cmd;
    if (cmd == "IN"){
      string name; cin >> name >> q;
      if (q == 'V') v.push(name);
      else if (q == 'N') n.push(name);
    }
    if (cmd == "OUT"){
      cin >> q;
      if (q == 'V') v.pop();
      else if (q == 'N') n.pop();
    }
  }

  while (v.size()) {
    cout << (v.front()) << '\n'; v.pop();
  }
  while (n.size()) {
    cout << (n.front()) << '\n'; n.pop();
  }

}