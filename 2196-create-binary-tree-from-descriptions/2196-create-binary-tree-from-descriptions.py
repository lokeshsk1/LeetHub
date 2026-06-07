# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        children = set()

        for p,c,isLeft in descriptions:

            if p not in nodes:
                nodes[p] = TreeNode(p)
            pnode = nodes[p]

            if c not in nodes:
                nodes[c] = TreeNode(c)
            cnode = nodes[c]

            if isLeft:
                pnode.left = cnode
            else:
                pnode.right = cnode

            children.add(c)
        
        res = None
        for n in nodes:
            if n not in children:
                res = nodes[n]
                break
        
        return res

                


