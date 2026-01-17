# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = None
        self.ino = []
        self.inorder(root)
        print(self.ino)
        
        for i in range(1, len(self.ino)):
            if self.ino[i] <= self.ino[i-1]:
                return False
            
        return True

    def inorder(self, root):

        if not root:
            return
        
        self.inorder(root.left)

        self.ino.append(root.val)

        self.inorder(root.right)