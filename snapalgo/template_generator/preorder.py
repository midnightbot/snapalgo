class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

ans = []
def preorder(root):
    if root is not None:
        ans.append(root.val)
        
        if root.left:
            preorder(root.left)
            
        if root.right:
            preorder(root.right)
            
