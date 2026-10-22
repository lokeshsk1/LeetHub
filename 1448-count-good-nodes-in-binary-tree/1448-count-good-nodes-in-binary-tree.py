# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    res = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, -100000)
        return self.res

    def helper(self, root, maxi):

        if not root:
            return

        if root.val >= maxi:
            print(root.val)
            self.res += 1
        
        self.helper(root.left, max(maxi, root.val))
        self.helper(root.right, max(maxi, root.val))



        
    # 3 1 3 4 1 5
    # 3 3 4 5