# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def recurse_tree(root):

            if not root:
                return

            if p.val < root.val and q.val < root.val:
                return recurse_tree(root.left)
            if p.val > root.val and q.val > root.val:
                return recurse_tree(root.right)
            
            return root

        return recurse_tree(root)