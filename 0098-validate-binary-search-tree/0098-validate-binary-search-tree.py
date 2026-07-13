# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False
        
        pv = -1
        if self.prev:
            pv = self.prev.val

        print(root.val, pv)
        self.prev = root

        if not self.isValidBST(root.right):
            return False


        return True


        
