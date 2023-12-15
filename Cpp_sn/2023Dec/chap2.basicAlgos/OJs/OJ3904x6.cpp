#include <bits/stdc++.h>
using namespace std; 
int n;

char match(char c){
    if (c == 'A') return 'T';
    else if (c == 'T') return 'A';
    else if (c == 'C') return 'G';
    else if (c == 'G') return 'C';
    return ' ';
}

int main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    cin >> n;
    int ans = 0;
    char arr[n];
    string a, b; cin >> a >> b;
    for (int i = 0; i< n ; i++){
        if ((match(a[i]) == b[i])){
            arr[i] = 'x';
        } else {
            arr[i] = match(a[i]);
        }
    }


    for (int i = 0; i < n ; i++){
        if (arr[i] != 'x'){
            for (int j = i+1 ; j < n ; j++){
                if (arr[i] == b[j] && arr[j] == b[i]){
                    ans++;
                    arr[i] = arr[j] = 'x';
                    break;
                }
            }
        }
    }

    for (int i = 0; i < n; i++){
        if (arr[i] != 'x') ans++;
    }
    cout << ans << '\n';
    return 0;
}