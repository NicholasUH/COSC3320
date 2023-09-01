# 43898981-dd2f-48a5-9b17-251f2153c645

'''
Recursion

Given the pre-order traversal and in-order traversal of a binary tree, output the post-order 
traversal of the binary tree.

Input format:
line 1: number of nodes
line 2: the pre-order traversal;
line 3: the post-order in-order traversal.
note: The tree nodes are labeled 1, 2, ..., n
'''

import sys

def function(preorder_list,inorder_list):
    if not preorder_list or not inorder_list:
        return []
    root = preorder_list[0] 
    root_index = inorder_list.index(root) 

    left_subtree = function(preorder_list[1:1+root_index], inorder_list[:root_index])

    right_subtree = function(preorder_list[1+root_index:], inorder_list[root_index+1:])

    return left_subtree + right_subtree + [root]


  

for line in sys.stdin:
    n = int(line) 
    preorder_list = sys.stdin.readline().split()
    inorder_list = sys.stdin.readline().split()  

    postorder_list = function(preorder_list, inorder_list)

    print(" ".join(map(str, postorder_list)))