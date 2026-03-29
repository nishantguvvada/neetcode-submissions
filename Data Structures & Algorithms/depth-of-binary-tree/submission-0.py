# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recurse_depth(root):
            if not root:
                return 0
            
            left = recurse_depth(root.left)
            right = recurse_depth(root.right)

            depth = max(left, right) + 1
            return depth
       
        return recurse_depth(root)