#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 1, 3, 4, 9};

    sort(v.begin(), v.end());

    for(int i = 0; i < v.size(); ++ i)cout << v[i] << ' ';

    return 0;
}

