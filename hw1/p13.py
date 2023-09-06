#1f738344-19a9-4a76-a47b-3d094473980c
'''
Given an array representing values to be added to an empty binary search tree in order, 
and a pair of these values, return the shortest path distance between these values in the 
tree after all values have been insert_nodeed.
'''

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, val):
    # insert nodes to create a BST, lower values go left, greater values go right
    if not root:
        return node(val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root

def find_path(root, target):
    # calculate distance from lowest common ancestor to targer node by finding depth
    if not root:
        return 0
    if target < root.val:
        return 1 + find_path(root.left, target)
    elif target > root.val:
        return 1 + find_path(root.right, target)
    else:
        return 0

def find_lowest_common_ancestor(root, node1, node2):
    
    # Find the lowest common ancestor by travering until the current node is either
    # one of the nodes being looked for OR the curr node is less than one node AND 
    # greater than the other
    
    if not root:
        return None
    if root.val > node1 and root.val > node2:
        return find_lowest_common_ancestor(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return find_lowest_common_ancestor(root.right, node1, node2)
    else:
        return root

def find_distance(root, node1, node2):
    # find lowest common ancestor, use the LCA to find the distance between it and the
    # other two nodes, then add the distances up to find the wanted distance
    lca = find_lowest_common_ancestor(root, node1, node2)
    path1 = find_path(lca, node1)
    path2 = find_path(lca, node2)
    return path1 + path2

def main():
    # Input Parsing
    values = list(map(int, input().split()))
    nodes = input().split()
    node1, node2 = int(nodes[0]), int(nodes[1])

    # BST Creation
    root = None
    for val in values:
        root = insert_node(root, val)

    print(find_distance(root, node1, node2))

main()