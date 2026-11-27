class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        st = []
        third = float('-inf')

        for i,e in enumerate(nums[::-1]):

            if e < third:
                return True
            
            while st and e > st[-1]:
                third = max(third, st[-1])
                st.pop()

            st.append(e)


            # print(st, third)

        return False


        # 1, 4, 2