# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
        
        def recurse_tree(root, subRoot):

            if not root:
                return False

            if helper(root, subRoot):
                return True

            return recurse_tree(root.left, subRoot) or recurse_tree(root.right, subRoot)

        return recurse_tree(root, subRoot) 