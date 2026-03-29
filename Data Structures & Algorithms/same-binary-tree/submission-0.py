# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recurse_tree(p, q):
            
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left = recurse_tree(p.left, q.left)
            right = recurse_tree(p.right, q.right)

            return left and right

        return recurse_tree(p, q)