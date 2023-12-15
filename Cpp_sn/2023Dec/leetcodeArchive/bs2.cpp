// C++ program to implement recursive Binary Search
#include <bits/stdc++.h>
using namespace std;
 
int binarySearch(int arr[], int x, int low, int high){
    while (low <= high){
        int mid = low + (high - low) / 2;

        if (arr[mid] == x) return mid;

        if (arr[mid] < x) low = mid + 1;

        else high = mid - 1;
    }
    return -1;
}
 
// Driver code
int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int x = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = binarySearch(arr, x, 0, n);
    (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result;
    return 0;
}