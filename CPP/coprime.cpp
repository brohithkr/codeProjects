#include <iostream>

using namespace std;

bool isPrime(int n) {

    for (int i = 3;i<int(n / 2);i++) {
        if(n%i==0) {
            return false;
        }
    }
    return true;
}

bool isPalindrome(int n) {
    string s = to_string(n);
    for (int i = 0;i<int(s.length() / 2); i++) {
        if (s[i] != s[s.length() - 1 - i]) {
            return false;
        }

    }
    return true;
}

int main() {
    for (int i = 0;i < 1001;i++) {
        if (isPalindrome(i) && isPrime(i)) {
            cout<<i<<"\n";
        }
    }
    return 0;
}