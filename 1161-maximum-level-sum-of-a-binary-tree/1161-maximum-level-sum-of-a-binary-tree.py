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
        lvl = 1

        while q:

            lvl += 1
            tot = 0
            n = len(q)
            flag = 0

            print(lvl, n)

            for _ in range(n):
                curr = q.popleft()
                if curr.left:
                    flag = 1
                    q.append(curr.left)
                    tot += curr.left.val
                if curr.right:
                    flag = 1
                    q.append(curr.right)
                    tot += curr.right.val
            
            if flag and tot > tot_max:
                tot_max = tot
                res = lvl

            

        
        return res



        
