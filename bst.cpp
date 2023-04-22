#include <iostream>
using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;
    node(int n){
        data = n;
        left = NULL;
        right = NULL;
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
                    break;
                }
                temp=temp->right;
            }
            else{
                if(temp->left==NULL){
                    temp->left = newnode;
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
    tree.insert(12);
    tree.insert(2);
    tree.insert(11);
    tree.display();
    tree.displayStructure();


}