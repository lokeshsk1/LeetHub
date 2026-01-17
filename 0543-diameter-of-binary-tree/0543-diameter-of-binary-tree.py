# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.height(root)
        return self.dia

    def height(self, root):

        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        self.dia = max(self.dia, left + right)
        return max(left, right) + 1
