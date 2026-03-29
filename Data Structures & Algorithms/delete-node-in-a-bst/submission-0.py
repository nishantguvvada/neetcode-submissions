# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        def get_min(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr.val

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                min_val = get_min(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)
        return root
