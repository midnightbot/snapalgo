class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

#################################### Inorder Traversal #############################

def inorder_traversal(root):
    ans = []
    def find_inorder_traversal(root):
        if root is not None:
            if root.left:
                find_inorder_traversal(root.left)
            ans.append(root.val)
            if root.right:
                find_inorder_traversal(root.right)

    find_inorder_traversal(root)
    return ans

    
#################################### Inorder Traversal #############################

#################################### Postorder Traversal #############################

def postorder_traversal(root):
    ans = []
    def find_postorder_traversal(root):
        if root is not None:
            if root.left:
                find_postorder_traversal(root.left)
            if root.right:
                find_postorder_traversal(root.right)
            ans.append(root.val)
    find_postorder_traversal(root)
    return ans

    
#################################### Postorder Traversal #############################
#################################### Preorder Traversal #############################

def preorder_traversal(root):
    ans = []
    def find_preorder_traversal(root):
        if root is not None:
            ans.append(root.val)
            if root.left:
                find_preorder_traversal(root.left)
            if root.right:
                find_preorder_traversal(root.right)

    find_preorder_traversal(root)
    return ans
#################################### Preorder Traversal #############################