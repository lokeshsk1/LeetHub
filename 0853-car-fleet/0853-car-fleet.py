class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        

        pair = [[position[i],speed[i]] for i in range(len(position))]

        pair.sort(reverse = 1)

        st = []

        for p,s in pair:
            d = target - p
            t = d / s

            if not st or st[-1] < t:
                st.append(t)

        # print(pair)

        return len(st)