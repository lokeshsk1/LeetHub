class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        st = []
        res = [0]*len(heights)

        for i in range(len(heights)-1, -1, -1):

            while st and heights[st[-1]] < heights[i]:
                res[i] += 1
                st.pop()

            if st:
                res[i] += 1

            st.append(i)
        
        print(res)

        return res

        
        # [10, 11, 12, 13, 14, 15]
