class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(key = lambda x : x[0], reverse = 1)

        st = []

        for p,s in pair:

            d = target - p
            t = d / s

            if not st or t > st[-1]:
                st.append(t)

        # print(st)
        
        return len(st)
