#include <iostream>
#include <vector>
#include <algorithm>

//using namespace std; 

int main() {
    std::vector<int> vec = {2, 1, 3, 2, 4, 1, 5, 4};
    std::sort(vec.begin(), vec.end());
    auto last = std::unique(vec.begin(), vec.end());
    vec.erase(last, vec.end());

    for (const auto& num : vec){
        std::cout << num << ' ';
    }

    return 0;
}