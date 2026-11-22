class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        n = len(temperatures)
        wait = [0] * n
        
        st = []

        for i in range(len(temperatures)):

            while st and temperatures[st[-1]] < temperatures[i]:
                wait[st[-1]] = i - st[-1]
                st.pop()
            else:
                st.append(i)

            # print(st)
        
        return wait
                 