# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

            self.isBal = True
            self.height(root)
            return self.isBal

    def height(self, root):

        if not root:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh-rh) > 1:
            self.isBal = False
        
        return 1 + max(lh, rh)