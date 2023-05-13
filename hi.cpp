#include <iostream>

int main(){
    int arr[1000000];
    arr[0] = 0;
    for(int i=1;i<100000;i++){
        arr[i] = arr[i-1]+i;
        std::cout<<arr[i]<<"\n";
    }
}