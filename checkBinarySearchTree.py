# Trees: Is This a Binary Search Tree?

def checkBST(root):
    # create recursive function to check if left and right nodes are binary search trees
    # Base Case: no children
    if(root.left is None and root.right is None):
        return True
    elif(root.left is None):
        if(root.data < root.right.data):
            return checkBST(root.right)
        else:
            return False
    elif(root.right is None):
        if(root.data > root.left.data):
            return checkBST(root.left)
        else:
            return False
    else:
        if(root.data < root.right.data and root.data > root.left.data):
            return checkBST(root.left) & checkBST(root.right)
        else:
            return False
