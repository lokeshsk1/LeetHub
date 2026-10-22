# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    res = None

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        if not root:
            return 
        
        self.kthSmallest(root.left, k)

        self.count += 1
        print(root.val, self.count)
        if self.count == k:
            self.res = root.val

        self.kthSmallest(root.right, k)

        return self.res
