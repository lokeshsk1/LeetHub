class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        

        st = []

        for i in asteroids:

            if i < 0:
                while st and st[-1] > 0:
                    diff = st[-1] + i
                    if diff > 0:
                        break
                    elif diff == 0:
                        st.pop()
                        break
                    else:
                        st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        
        return st
            