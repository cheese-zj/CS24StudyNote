#include <bits/stdc++.h>
using namespace std;
int n, m;
int main() {
    cin >> n >> m;
    int aa[n][m];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            aa[i][j] = 0;
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int c; cin >> c;
            if (c == 1){
                aa[i][j] = 9;
                for (int x = -1; x < 2; x++){
                    for (int y = -1; y < 2; y++){
                        if (aa[i+x][j+y]!=9 && i+x>=0 && i+x < n && j+y >= 0 && j+y < m)aa[i+x][j+y]++;
                    }
                }
            }
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cout << aa[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}

