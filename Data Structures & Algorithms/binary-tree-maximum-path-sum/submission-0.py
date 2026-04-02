# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def recurse_tree(root):

            if not root:
                return 0

            left = max(recurse_tree(root.left), 0)
            right = max(recurse_tree(root.right), 0)
            self.max_sum = max(self.max_sum, left + right + root.val)
            return root.val + max(left, right)
        recurse_tree(root)
        return self.max_sum