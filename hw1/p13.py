#bd25ddf0-d6e7-4e18-9fb4-ff7db363ecb2

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
        return []
    if target < root.val:
        return [root.val] + find_path(root.left, target)
    elif target > root.val:
        return [root.val] + find_path(root.right, target)
    else:
        return [root.val]



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
    distance = len(path1) + len(path2) - 2
    return distance

values = list(map(int, input().split()))
root = None
for val in values:
    root = insert(root, val)

nodes = input().split()
node1, node2 = int(nodes[0]), int(nodes[1])

print(shortest_path_distance(root, node1, node2))