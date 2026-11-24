class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st = []
        Map = [-1] * len(nums)

        nums2 = nums + nums
        for i,e in enumerate(nums2):

            while st and e > nums2[st[-1]]:
                curr = st.pop()
                if curr < len(nums):
                    Map[curr] = e
            
            st.append(i)

        print(Map)
        return Map[:len(nums)]
