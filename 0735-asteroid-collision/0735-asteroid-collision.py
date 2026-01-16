class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        
        st = []

        for i in a:

            while st and st[-1] > 0 and i < 0:

                diff  = st[-1] - (-i)

                if diff > 0:
                    i = 0
                elif diff < 0:
                    st.pop()
                else:
                    st.pop()
                    i = 0

            if i:
                st.append(i)

        return st


        # 10 -5

        # 10 -10

        # 10 15

        # 10 -15


            