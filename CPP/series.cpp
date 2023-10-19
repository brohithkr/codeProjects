#include <iostream>

using namespace std;

int fact(int n) {
    int res = 1;
    int i=1;
    while(i<=n) {
        res *= i;
        i+=1;
    }
    return res;
}


void print_series(int n) {
    int i=1;
    while (i<=n)
    {
        int res = i;
        int j=1;
        while (j<=i)
        {
            res *= j;
            j+=1;
        }
        cout<<res<<" ";
        i+=1;
    }
}

int main() {
    int n=3;
    int i=1;
    long long sum = 0;
    while (i<=n)
    {
        int res = 1;
        int j=1;
        while (j<=i)
        {
            res *= j;
            j+=1;
        }
        // cout<<res<<" ";
        sum += res;
        i+=1;
    }
    cout<<sum<<endl;
}

