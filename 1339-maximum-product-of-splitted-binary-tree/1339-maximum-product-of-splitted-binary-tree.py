# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        res = 0

        self.mp = dict()
        self.sumOfSubTree(root)

        totSum = self.mp[root]

        for i,j in self.mp.items():
            res = max(res, j * (totSum - j))

        return res % (10**9 + 7)
        
    
    def sumOfSubTree(self, root):

        if not root:
            return 0

        res = root.val + self.sumOfSubTree(root.left) + self.sumOfSubTree(root.right)
        self.mp[root] = res
        
        return res

    