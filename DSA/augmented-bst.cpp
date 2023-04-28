#include <iostream>
using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;
    int nofnodes;
    node(int n){
        data = n;
        left = NULL;
        right = NULL;
        nofnodes = 1;
    }
};

class bst{
    public:
    node* root;

    bst(){
        root=NULL;
    }

    void push(int val){
        node* newnode = new node(val);
        node* temp = root;
        if(root==NULL){
            root = newnode;
            return;
        }
        while(1){
            if(val>=temp->data){
                temp->nofnodes+=1;
                if(temp->right==NULL){
                    temp->right = newnode;
                    break;
                }
                temp=temp->right;
            }
            else{
                temp->nofnodes+=1;
                if(temp->left==NULL){
                    temp->left = newnode;
                    break;
                }
                temp = temp->left;
            }
        }
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

    int noflessthan(int num){
        int res=0;
        node* temp=root;
        while(1){
            if(temp->data<num){
                res+=1;
                if(temp->left!=NULL){
                    res+=temp->left->nofnodes;
                }
                if(temp->right==NULL){
                    break;
                }

                temp=temp->right;
            }
            else if(temp->data>num){
                if(temp->left==NULL){
                    break;
                }
                temp=temp->left;
            }
            else{
                res+=temp->left->nofnodes;
                break;
            }
        }
        return res;
    }


};

int main(){
    bst tree;
    tree.push(22);
    tree.push(56);
    tree.push(12);
    tree.push(5);
    tree.push(82);
    tree.push(64);
    tree.display();
    tree.displayStructure();
    // cout<<tree.noflessthan(4);
    


}