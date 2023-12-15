#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
    int b = 1;
    auto a = b;
    cout << a << endl;
    vector<string> msg = {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    int len = msg.size();
    cout << "长度" << len << endl;
    for (int i=0; i<5; i++){
        // ms.push_back("a");
        cout << i << endl;
    }

    for (string s : msg){
        cout << s << '\n';
    }

    return 0;
}