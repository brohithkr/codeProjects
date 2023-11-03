#include <bits/stdc++.h>
using namespace std;
#define newl cout<<"\n"
#define fori(a,b) for(int i=a;i<b;i++)
#define forj(a,b) for(int j=a;j<b;j++)
typedef long long int ll;

bool isOdd(ll n) {
    return (n % 2 == 1);
}

int numPossible(int pos, int lb, int ub, int k) {
    if (k > (ub - pos)) {
        return (ub - pos) + 1;
    }
    else if (k > (pos - lb)) {
        return pos - lb + 1;
    }

    else {
        return k;
    }
}


int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        ll arr[n];
        fori(0, n) {
            cin >> arr[i];
            cout<<arr[i];
        }
        int lb = 0, ub = n - 1;
        int tot = 0;
        int i = 0;
        while (i < n) {
            // cout<<isOdd(arr[i])<<".";
            if (arr[i]%2==0) {
                tot += numPossible(i, lb, ub, k);
                lb = i + k;
                i += k + 1;
                cout<<arr[i]<<" "<<tot<<"..";
                continue;
            }
            i+=1;
        }
        cout<<tot<<"\n";
    }
    return 0;
}