#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t;
    cin >> t;
    while(t--) {
        int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> ribbon(n);
        for (int i = 0; i < n; ++i) {
            cin >> ribbon[i];
        }

        int first_chip = -1, last_chip = -1;
        for (int i = 0; i < n; ++i) {
            if (ribbon[i] == 1) {
                if (first_chip == -1) first_chip = i;
                last_chip = i;
            }
        }

        int free_cells = 0;
        for (int i = first_chip; i <= last_chip; ++i) {
            if (ribbon[i] == 0) {
                free_cells++;
            }
        }

 
        cout << free_cells << '\n';
    }
    return 0;
    }
}