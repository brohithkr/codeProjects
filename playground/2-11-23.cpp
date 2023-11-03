#include <iostream>

using namespace std;

void _recurseSort(int arr[], int pos) {
    int i == pos
        while (pos > 0 && arr[pos] > arr[pos - 1]) {
            int temp = arr[pos - 1];
            arr[pos - 1] = arr[pos];
            arr[pos] = temp;
            pos -= 1
        }
    

}

void printTail(int n, int temp) {
    if (temp == 0) {
        cout << n - temp << "\n";
        return;
    }
    cout << n - temp << "\n";
    printTail(n, temp - 1);
}

void printHead(int n) {
    if (n == 0) {
        cout << n << "\n";
        return;
    }
    printHead(n - 1);
    cout << n << "\n";
}

int main() {
    printTail(20, 20);
    printHead(20);
}