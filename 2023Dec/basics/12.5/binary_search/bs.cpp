#include <bits/stdc++.h>
//只能对数组进行binary search, 数组中的元素必须是单调的。（单调不减/单调不增)
using namespace std; 

int main(){
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    vector<int> numbers = {1, 3, 5, 7, 9};

    int target = 5;
    
    bool found = binary_search(numbers.begin(), numbers.end(), target);

    if (found){
        cout << "Target Element" << target << " Found\n";
    } else {
        cout << "Target Element" << target << " Not Found\n";
    }
}