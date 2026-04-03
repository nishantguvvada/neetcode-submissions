# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []
        def recurse_tree(root):
            if not root:
                self.result.append("N")
                return
            
            self.result.append(str(root.val))
            recurse_tree(root.left)
            right = recurse_tree(root.right)

        recurse_tree(root)
        return ','.join(self.result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(','))

        def helper():
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        return helper()