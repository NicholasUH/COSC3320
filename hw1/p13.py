#1f738344-19a9-4a76-a47b-3d094473980c
'''
Given an array representing values to be added to an empty binary search tree in order, 
and a pair of these values, return the shortest path distance between these values in the 
tree after all values have been inserted.
'''

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def find_path(root, target):
    if not root:
        return 0
    if target < root.val:
        return 1 + find_path(root.left, target)
    elif target > root.val:
        return 1 + find_path(root.right, target)
    else:
        return 0

def find_lca(root, node1, node2):
    if not root:
        return None
    if root.val > node1 and root.val > node2:
        return find_lca(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return find_lca(root.right, node1, node2)
    else:
        return root

def shortest_path_distance(root, node1, node2):
    lca = find_lca(root, node1, node2)
    path1 = find_path(lca, node1)
    path2 = find_path(lca, node2)
    return path1 + path2


def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        root = insert(root, val)

    nodes = input().split()
    node1, node2 = int(nodes[0]), int(nodes[1])

    print(shortest_path_distance(root, node1, node2))



main()