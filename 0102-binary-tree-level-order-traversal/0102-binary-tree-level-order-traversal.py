# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if not root:
            return []

        q = [root]
        res = []

        while q:
            n = len(q)
            l = []

            for _ in range(n):

                curr = q.pop(0)
                l.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                    
                if curr.right:
                    q.append(curr.right)

                
            
            res.append(l)

        return res
                
                
            


