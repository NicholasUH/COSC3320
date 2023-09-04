#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

struct node{
    int val;
    node *left;
    node *right;

    node(int value, node* _left, node* _right) : val(value), left(_left), right(_right) {}
};

node* insert(node *root, int val){
    if(!root){
        return new node(val, nullptr,nullptr);
    }
    else if(val < root->val){
        root->left = insert(root->left,val);
    }
    else if(val > root->val){
        root->right = insert(root->right,val);
    }
    return root;
}

int findPath(node *root, int value){
    if(!root){
        return 0;
    }
    else if(){

    }
    else if(){

    }
    else{
        return 0;
    }
}

node* findLCA(node *root, int val1, int val2){

    if(!root){
        return nullptr;
    }
    else if(root->val < val1 and root->val < val2){
        return findLCA(root->right,val1,val2);
    }
    else if(root->val > val1 and root->val > val2){
        return findLCA(root->right,val1,val2);  
    }
    else{
        return root;
    }
}

int findDistance(node *root, int val1, int val2){
    node *lca = findLCA(root,val1,val2);
    int path1 = findPath();
    int path2 = findPath();
    return path1 + path2;
}

int main() {
    
    vector<int> nums;
    int node1, node2, intTemp;
    string temp;

    getline(cin,temp);
    stringstream ss(temp);

    while(ss >> intTemp){
        nums.push_back(intTemp);
    }

    cin >> node1 >> node2;

    node *root = nullptr;

    for(int x = 0; x < nums.size();x++){
        root = insert(root,nums[x]);
    }


    return 0;
}
