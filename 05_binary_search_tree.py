import random

def insert_bst(root, value):
    if root is None:
        node = {'val': value, 'left': None, 'right': None}
        return node
    elif value < root['val']:
        root['left'] = insert_bst(root['left'], value)
    else:
        root['right'] = insert_bst(root['right'], value)
    return root

def inorder(root):
    if root is None:
        return []
    return inorder(root['left']) + [root['val']] + inorder(root['right'])

random_arr = random.sample(range(1, 51), 15)
print("\nThe Random Array is-- ", random_arr)

root = None

for elem in random_arr:
    root = insert_bst(root, elem)  

print("\nThe Inorder Traversal of BST is--", inorder(root))