class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

ans = []
def postorder(root):
    if root is not None:
        if root.left:
            postorder(root.left)
            
        if root.right:
            postorder(root.right)
            
        ans.append(root.val)
