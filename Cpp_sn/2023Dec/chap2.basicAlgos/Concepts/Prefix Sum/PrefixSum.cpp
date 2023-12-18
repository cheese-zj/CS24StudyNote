#include <bits/stdc++.h>
using namespace std;
int main() {
    int a[7];
    for (int i = 0; i < 7; i++) a[i] = i * 2;

    for (int i = 0; i < 7; i++) cout << a[i] << ' '; 
    cout << '\n';

    int prefix[7];
    prefix[0] = 0;
    for (int i = 1; i <= 7 ; i++){
        prefix[i] = prefix[i-1] + a[i];
    }

    for (int i = 1; i<= 7; i++) cout << prefix[i] <<' ';
}