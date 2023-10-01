# 70665735-ae48-4466-bb72-69f20d215e48

def reconstruct_binary_tree(preorder_list,inorder_list):
    if not preorder_list or not inorder_list:
        return []
    
    # find root value using preorder
    root = preorder_list[0] 

    # find root index in inorder to determine left and right subtree
    # everything left is left subtree, likewise for the right subtree
    root_index = inorder_list.index(root)

    #create the proper subtrees
    left_subtree = reconstruct_binary_tree(preorder_list[1:root_index+1], inorder_list[:root_index])
    right_subtree = reconstruct_binary_tree(preorder_list[root_index+1:], inorder_list[root_index + 1:])

    # return in post-order fashion
    return left_subtree + right_subtree + [root]

def main():
    # input parsing
    num_of_nodes = int(input()) 
    preorder_list = input().split()
    inorder_list = input().split()  

    postorder_list = reconstruct_binary_tree(preorder_list, inorder_list)
    print(" ".join(map(str, postorder_list)))

main()