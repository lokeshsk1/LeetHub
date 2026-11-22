class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        st = []

        for i in asteroids:

            while i < 0 and st and st[-1] > 0:
                diff = i + st[-1]

                print(diff)

                if diff == 0:
                    st.pop()
                    break
                elif diff > 0:
                    break
                else:
                    st.pop()
            else:
                st.append(i)
        
        return st