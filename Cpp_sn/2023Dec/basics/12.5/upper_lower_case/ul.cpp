// islower()
// isupper()
// tolower()
// toupper()

#include <bits/stdc++.h>
using namespace std;

int main() {
    char a = 'a';
    a = toupper(a);
    cout << a << '\n';

// may change lower/upper status by +/- 32 to change to lower/upper

    a = a + 32; // changing it to the lowercase status
    cout << a << '\n';

    char b = 'b';
    b = b - 'a' + 'A';
    cout << b << '\n';
}



