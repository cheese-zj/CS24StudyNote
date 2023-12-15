#include <bits/stdc++.h>
using namespace std;
const int N = 120;
int aa[N][N];
int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n,m; cin >> n >> m;
    int p; cin >> p;
    int ans = 0;
    while (p--){
        int x,y; cin >> x >> y;
        aa[x][y] = 1;
    }
    int k; cin >> k;
    while (k--){
        for (int i = 1; i <= n ; i++){
            for (int j = 1; j <=m; j++){
                if (aa[i][j]==1){
                    if (aa[i-1][j] != 1) aa[i-1][j] = 2;
                    if (aa[i+1][j] != 1) aa[i+1][j] = 2;
                    if (aa[i][j-1] != 1) aa[i][j-1] = 2;
                    if (aa[i][j+1] != 1) aa[i][j+1] = 2;
                }
            }
        }
        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=m; j++){
                if (aa[i][j] == 2) aa[i][j]--;
            }
        }
    }
    for (int i = 1; i<=n; i++){
        for (int j = 1; j<=m; j++){
            if (aa[i][j] == 1) ans ++;
        }
    }
    cout << ans << '\n';
    return 0;
}
