#include <iostream>
#include <string>

using namespace std;

int main(){

    ios::sync_with_stdio(0), cin.tie(0),cout.tie(0);

    string str;
    cout << "May I have your name?";
    cin >> str;
    cout << "Hi! " << str << "!" << endl;
    return(0);
}