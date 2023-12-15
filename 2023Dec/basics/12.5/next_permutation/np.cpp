#include <bits/stdc++.h>
using namespace std;

int a[10];

int main()
{
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    for (int i = 1; i <= 4; i++) a[i] = i;
    bool tag = true;
    while (tag){
        for (int i = 1; i <= 4; ++ i ) cout << a[i] << ' ';
        cout << '\n';
        tag = next_permutation(a+1, a+1+4);   
    }
    //for (int i = 1; i <= 4; ++ i ) cout << a[i] << ' ';
    return 0;
}