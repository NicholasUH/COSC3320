// 4ef5c19c-97c2-4541-bc59-f862fc9920d8
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
    if(val < root->val){
        root->left = insert(root->left,val);
    }
    else{
        root->right = insert(root->right,val);
    }
    return root;
}

int findPath(node *root, int value){
    if(!root){
        return 0;
    }
    else if(value < root->val){
        return 1 + findPath(root->left,value);
    }
    else if(value > root->val){
        return 1 + findPath(root->right,value);
    }
    else{
        return 0;
    }
}

node* findLCA(node *root, int val1, int val2){

    if(!root){
        return NULL;
    }
    if(root->val > val1 && root->val > val2){
        return findLCA(root->left,val1,val2);
    }
    else if(root->val < val1 && root->val < val2){
        return findLCA(root->right,val1,val2);  
    }
    else{
        return root;
    }
}

int findDistance(node *root, int val1, int val2) {
    node *lca = findLCA(root, val1, val2);
    int path1 = findPath(lca, val1);
    int path2 = findPath(lca, val2); 
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
    
    cout << findDistance(root,node1,node2) << endl;

    return 0;
}
