class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        

        st = []
        Map = {}

        for i in nums2:

            while st and i > st[-1]:
                curr = st.pop()
                Map[curr] = i
            
            st.append(i)
        
        print(Map)
        res = []
        for i in nums1:
            if i in Map:
                res.append(Map[i])
            else:
                res.append(-1)

        return res
