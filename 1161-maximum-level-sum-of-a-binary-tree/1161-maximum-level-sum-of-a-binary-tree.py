# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        tot_max = root.val
        res = 1
        lvl = 0

        while q:

            lvl += 1
            tot = 0
            n = len(q)

            for _ in range(n):
                curr = q.popleft()
                tot += curr.val
                if curr.left:
                    q.append(curr.left)                    
                if curr.right:
                    q.append(curr.right)
            
            if tot > tot_max:
                tot_max = tot
                res = lvl
        
        return res



        
