#include <iostream>
using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;
    int height;
    node(int n){
        data = n;
        left = NULL;
        right = NULL;
        // height = 0;
    }
};

class bst{
    public:
    node* root;

    bst(){
        root=NULL;
    }

    int height_of(node* temp){
        if(temp->left==NULL || temp->right == NULL){
            if(temp->left==NULL){
                return temp->right->height + 1;
            }else if(temp->right==NULL){
                return temp->left->height + 1;
            }else{
                return 0;
            }
        }
        else{
            return max(temp->right->height,temp->left->height) + 1;
        }

    }

    

    void _insert(node* root,int val){
        ;
    }

    void insert(int val){
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

    void display(){
        inorderWalk(root);
        cout<<"\n";
    }



};


