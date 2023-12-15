#include <set>
#include <iostream>
using namespace std;

struct MyCompare {
    bool operator()(const int& a , const int& b) const {
        return a > b;
    }
};

int main(){
    set <int,MyCompare> mySet;
    mySet.insert(25);
    mySet.insert(100);
    mySet.insert(2);

    for (auto elem : mySet) cout << elem << ' ';
    return 0;
}