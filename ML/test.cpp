/*
Write a C++ program to find the length of a 
longest arithmetic subarray

SAMPLE INPUT/OUTPUT:
Number of elements:5                                                                                                    
Array elements:                                                                                                         
3 4 5 6 7                                                                                                               
longest arithmetic subarray length:4                                                                                    
 
Number of elements:5                                                                                                    
Array elements:                                                                                                         
6 8 10 15 16                                                                                                            
longest arithmetic subarray length:2                                                                                    

*/

#include <iostream>

using namespace std;

int main() {
    cout<<"Number of elements:";
    int n;
    cin>>n;
    cout<<"longest arithmetic subarray length:\n";
    int arr[n];
    int max_till_now = 0;
    int curr_max = 0; 
    int curr_diff = 0;
    int prev_diff = 0;
    for(int i=0;i<n;i++){
        cin>>arr[i];
        if(i>0) {
            prev_diff = curr_diff;
            curr_diff = arr[i]- arr[i-1];
            if(curr_diff == prev_diff) {
                curr_max += 1;
            }
            else {
                if(max_till_now < curr_max) {
                    max_till_now = curr_max;
                    curr_max = 1;
                }
            }
        }
        
    }
    cout<<max_till_now;
    // for(int i=0)
}