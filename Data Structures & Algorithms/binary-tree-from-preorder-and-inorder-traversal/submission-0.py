# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None


        root_val = preorder[0]
        mid = 0
        for idx, el in enumerate(inorder):
            if el == root_val:
                mid = idx
        
        left_inorder = inorder[:mid]
        right_inorder = inorder[mid+1:]

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:mid+1], left_inorder)
        root.right = self.buildTree(preorder[mid+1:], right_inorder)

        return root


        