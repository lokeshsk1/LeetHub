# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
            
        q = [root]
        res = [root.val]

        while q:

            n = len(q)

            for _ in range(n):
                curr = q.pop(0)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            print(res, n)
            if q:
                res.append(q[-1].val)
        
        return res

            