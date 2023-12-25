#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 + 9;
int arr[N];

signed main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n ; cin >> n;
    for (int i = 1; i <= n; i++ ) {
        cin >> arr[i];
    }
    reverse(arr+1, arr+1+n);
    int b,c,d = 1;
    for (int i = 1; i <= n; i++){
        if (arr[i] > arr[d]) {d = i; break;}
    }

    for (int i = d+1; i <= n; i++) {
        if (arr[i] > arr[d]) {c = i; break;}
    }
    b = c;

    for (int i = c+1; i <= n; i++) {
        if (arr[i] > max(arr[c],arr[d])) {b = i; break;}
    }

    for (int i = b+1; i <= n; i++) {
        if (arr[i] < arr[b]) {cout << "YES\n"; return 0;}
    }
    cout << "NO\n";
    return 0;
}

// #include<bits/stdc++.h>
// using namespace std;
// int n;
// const int M=5e5+5;
// int nums[M];
// int min_r[M];
// int k=-0x3f3f3f3f;
// stack<int> st;

// int main(){
//   memset(min_r,0x3f3f3f3f,sizeof(min_r));
//   cin>>n;
//   for(int i=1;i<=n;i++){
//     cin>>nums[i];
//     min_r[i]=nums[i];
//   }
//   for(int i=n-1;i>=1;i--){    // minimum value on the right side of i
//     min_r[i]=min(min_r[i],min_r[i+1]);
//   }
//   for(int i=1;i<=n;i++){
   
//     while(!st.empty()&&st.top()<nums[i]){
//       k=max(k,st.top());
//       st.pop();
//     }
//     st.push(nums[i]);
//      if(nums[i]<k){
//       if(nums[i]>min_r[i])  {
//         cout<<"YES"<<endl;
//         return 0;
//       }
//     }
    
//   }
//   cout<<"NO"<<endl;
//   return 0;
// }