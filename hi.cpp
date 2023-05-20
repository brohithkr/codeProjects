#include<iostream>
#include<vector>
using namespace std;


//  * Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
    int getval(ListNode*& l){
        if(l!=NULL){
            int num = l->val;
            l = l->next;
            return num;
        }
        else{
            return 0;
        }
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = getval(l1) + getval(l2);
        int carry = (sum>=10) ? 1:0;
        ListNode* sumhead = new ListNode(sum%10);
        ListNode* sumtemp = sumhead;
        int d1=getval(l1),d2=getval(l2);
        while(!(d1==0 && d2==0)){
            sum = d1+d2+carry;
            carry = (sum>=10) ? 1:0;
            ListNode* s1 = new ListNode(sum%10);
            sumtemp->next = s1;
            sumtemp = sumtemp->next;
            d1 = getval(l1);
            d2 = getval(l2);

        }


        return sumhead;
    }
};

int main(){
    Solution sol;
    vector<int> arr = {1,2,3,1};
    vector<int> arr2 = {1,5,9,1,5,9};
    vector<int> arr3 = {-3,3};
    cout<<sol.addTwoNumbers(arr3,2,4);
}