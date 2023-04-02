class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

ans = []
def inorder(root):
    if root is not None:
        if root.left:
            inorder(root.left)

        ans.append(root.val)
        
        if root.right:
            inorder(root.right)
            
        
