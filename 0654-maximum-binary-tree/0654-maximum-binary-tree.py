# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    
        def helper(nums):

            if len(nums) == 0:
                return None

            max_ind = nums.index(max(nums))
            root = TreeNode(nums[max_ind])
            root.left = helper(nums[:max_ind])
            root.right = helper(nums[max_ind+1:])
            return root

        max_ind = nums.index(max(nums))
        print(max_ind)
        root = TreeNode(nums[max_ind])

        root.left = helper(nums[:max_ind])
        root.right = helper(nums[max_ind+1:])
        return root