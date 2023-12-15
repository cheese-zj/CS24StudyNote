#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n,m; cin >> n >> m;
    int aa[n][m];
    for (int i = 0; i < n; i++){
        for (int j = 0; j< m ; j++){
            aa[i][j] = 0;
        }
    }
    int p; cin >> p;
    int ans;
    while (p--){
        int x,y; cin >> x >> y;
        aa[x-1][y-1] = 1;
    }
    int k; cin >> k;
    while (k--){
        for (int i = 0; i < n ; i++){
            for (int j = 0; j < m; j++){
                if (aa[i][j]==1){
                    for (int d : {1,-1}){
                        if (i+d < n && i+d >= 0 && aa[i+d][j]!=1)aa[i+d][j] = -1;
                        if (j+d < m && j+d >= 0 && aa[i][j+d]!=1)aa[i][j+d] = -1;
                    }
                }
            }
        }
        for (int i = 0; i<n; i++){
            for (int j = 0; j<m; j++){
                if (aa[i][j] == -1) aa[i][j] = 1;
            }
        }
    }
    for (int i = 0; i<n; i++){
        for (int j = 0; j<m; j++){
            if (aa[i][j] == 1) ans ++;
            cout << aa[i][j] <<' ';
        }
        cout << '\n';
        
    }
    cout << ans << '\n';
    return 0;
}
