#include <iostream>
using namespace std;

class stack{
    private:
    int* arr;
    int top;
    int size;
    public:
    stack(int n){
        arr = new int[n];
        top = -1;
        size = n;
    }
    void push(int val){
        if(top==size-1){
            cout<<"stack overflow\n";
        }
        top++;
        arr[top] = val;

    }
    int pop(){
        int res = arr[top];
        arr[top] = 0;
        top --;
        return res;
    }
};

class node{
    public:
    int data;
    node* left;
    node* right;
    node* p;

    node(){
        data = 0;
        left = NULL;
        left = NULL;
        p = NULL;
    }
    node(int val){
        data = val;
        left = NULL;
        left = NULL;
        p = NULL;

    }
};

class bst{
    public:
    node* root;

    bst(){
        root=NULL;
    }

    void insert(int val){
        node* newnode = new node(val);
        node* temp = root;
        if(temp==NULL){
            root = newnode;
            return;
        }
        while(1){
            if(val>=temp->data){
                if(temp->right==NULL){
                    temp->right = newnode;
                    temp->right->p = temp;
                    break;
                }
                temp=temp->right;
            }
            else{
                if(temp->left==NULL){
                    temp->left = newnode;
                    temp->left->p = temp;
                    break;
                }
                temp = temp->left;
            }
        }
    }

    void del(int val){
        ;
    }

    void inorderWalk(node* temp){
        if(temp==NULL){
            return;
        }
        inorderWalk(temp->left);
        cout<<temp->data<<" ";
        inorderWalk(temp->right);
    }

    // void inorderWalkiter(){
    //     node* temp = root;
    //     while(1){
    //         temp = temp->left;
    //         if (temp == NULL){
                
    //         }
    //     }
        
    // }


    void display(){
        inorderWalk(root);
        cout<<"\n";
    }

    void _displayStructure(node* temp,int* level){
        if(temp==NULL){
            (*level)-=1;
            return;
        }
        (*level)+=1;
        _displayStructure(temp->right,level);
        for(int i=0;i<(*level);i++){
            cout<<"    ";
        }
        cout<<temp->data<<"\n";
        (*level)+=1;
        _displayStructure(temp->left,level);
        (*level)-=1;
        return;

    }
    void displayStructure(){
        int level = 0;
        _displayStructure(root,&level);
    }


};

int main(){
    bst tree;
    tree.insert(4);
    tree.insert(5);
    tree.insert(3);
    tree.displayStructure();

}