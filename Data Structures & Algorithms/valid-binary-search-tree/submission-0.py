# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recurse_tree(root, low, high):

            if not root:
                return True

            if low < root.val < high:
                return recurse_tree(root.left, low, root.val) and recurse_tree(root.right, root.val, high)
            else:
                return False
            
            return False

        return recurse_tree(root, float('-inf'), float('inf'))