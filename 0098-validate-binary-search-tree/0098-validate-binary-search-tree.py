# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = None
        return self.inorder(root)

    def inorder(self, root):


        if not root:
            return True
        
        if not self.inorder(root.left):
            return False

        print(root.val, self.prev if self.prev else None)

        if self.prev and self.prev.val >= root.val:
            return False
        
        self.prev = root

        return self.inorder(root.right)