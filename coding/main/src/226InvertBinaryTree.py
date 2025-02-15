# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        lft = self.invertTree(root.left)
        rgt = self.invertTree(root.right)

        root.left = rgt
        root.right = lft

        return root


        
