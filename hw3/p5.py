# 6a6237c7-a22e-4d8b-a335-1fda5dab5bdf

def function(preorder_list,inorder_list):
    if not preorder_list or not inorder_list:
        return []
    root = preorder_list[0] 
    root_index = inorder_list.index(root) 

    left_subtree = function(preorder_list[1:1+root_index], inorder_list[:root_index])

    right_subtree = function(preorder_list[1+root_index:], inorder_list[root_index+1:])

    return left_subtree + right_subtree + [root]


def main():
    n = int(input()) 
    preorder_list = input().split()
    inorder_list = input().split()  

    postorder_list = function(preorder_list, inorder_list)

    print(" ".join(map(str, postorder_list)))

main()