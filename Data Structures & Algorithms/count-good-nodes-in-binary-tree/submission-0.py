# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recurse_tree(root, max_so_far):

            if not root:
                return 0

            if root.val >= max_so_far:
                good = 1
            else:
                good = 0

            new_max = max(max_so_far, root.val)
            
            return good + recurse_tree(root.left, new_max) + recurse_tree(root.right, new_max)

        return recurse_tree(root, float('-inf'))
