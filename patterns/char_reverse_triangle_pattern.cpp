#include<bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    char k = 'A';

    // loop for row
    // loop for column
        //


    for(int i = 1; i <= n; i++) {
        // k = 'A' + n-1;
        for(int j = i; j >= 1; j--) {
            cout << k << ' ';
            // k--;
        }
        cout << '\n';
    }

    return 0;
}