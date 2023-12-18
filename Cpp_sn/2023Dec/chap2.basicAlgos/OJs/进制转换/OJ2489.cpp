#include <iostream>
using namespace std;
using ll = long long;
const int N = 50;
int a[N];
int main() {
    string s = "2021ABCD";
    for (int i = 0; i < s.length(); i++ ){
        if (s[i] <= '9' && '0' <= s[i]){
            a[i+1] = s[i] - '0'; 
        } else {
            a[i+1] = s[i] - 'A' + 10;
        }

    }

    ll x = 0;
    for (int i = 0; i<= s.length(); i++){
        x = x*16 + a[i];
    }

    cout << x << '\n';

    return 0;
}