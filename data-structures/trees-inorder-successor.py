# Inorder Successor of Binary Search Tree: https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P
# Date: April 16, 2018
# Author: Rishi Daryanani, following C++ code of mycodeschool: https://gist.github.com/mycodeschool/6515e1ec66482faf9d79

class Node:
    # Constructor to create a Binary Tree node
    def __init__(self, value ,left=None ,right=None):
        self.data = value
        self.left = left
        self.right = right


# Insert node in BST
def insert(root: Node, data: int):
    if root is None:
        root = Node(data)
    elif data <= root.data:
        # insert to left
        root.left = insert(root.left, data)
    else:
        # insert to right
        root.right = insert(root.right, data)
    return root

def inorder_print(root: Node):
    if root is None: return
    inorder_print(root.left)
    print(root.data)
    inorder_print(root.right)

# --- successor functions ---

def find_node(root: Node, data: int) -> Node:
    if root is None: return None
    if root.data == data:
        return root
    elif data < root.data: return find_node(root.left,data)
    else: return find_node(root.right,data)

def find_min(root):
    # min is the left most node
    if root is None: return None
    while root.left:
        root = root.left
    print('found min!', root.data)
    return root

def get_successor(root: Node, data: int):

    current_node = find_node(root, data)
    if current_node is None: return None # data not found

    if (current_node.right):
        # Case 1 - there is a right subtree, so get the min of that
        # Time complexity: O(h)
        return find_min(current_node.right)

    else:
        # Case 2 - no right subtree, so we need to get the closest ancestor where this
        # current_node is in the left subtree of that ancestor
        # Time complexity: O(h)
        successor = None
        ancestor = root
        while (ancestor != current_node): # traverse until we reach the current node
            if current_node.data < ancestor.data:
                successor = ancestor # so far this is the deepest node for which current node is in left
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor

if __name__ == "__main__":
    # Driver program


    '''
    Ex 1: (edit above to get this tree if needed, as in https://gist.github.com/mycodeschool/6515e1ec66482faf9d79
       5
      / \
     3   10
    / \    \ 
   1   4   11
   
   Ex 2: demo below
   
       6
      / \
     3   10
    / \    \ 
   1   4   11
        \
         5
         
    To find the predecessor (as opposed to the successor), we simply have 2 cases as above:
        Case 1. There is a left subtree (e.g. take "6" above), so the predecessor is the max of that
        Case 2. No left subtree, so we get the closest ancestor where the current node is on the right
        [Note: I haven't implemented it in this code]
    '''
    root = Node(6)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 1)
    root = insert(root, 11)
    root = insert(root, 5)

    inorder_print(root)
    successor = get_successor(root, 5); # should return 6 which happens to be the root in this case
    print('Successor:', (successor.data if successor else 'No successor'))