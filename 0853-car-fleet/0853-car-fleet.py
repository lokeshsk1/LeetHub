class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position, speed)]

        pair = sorted(pair, key = lambda x : x[0], reverse = True)
        st = []

        print(pair)

        for p, s in pair:
            d = target - p
            t = d / s

            print(t)
            
            if not st or (st and t > st[-1]):
                st.append(t)
            
        return len(st)

        # 0,2 4,1 2,3

        # 4,1 2,3 0,2

        # 6/1, 8/3, 10/2

        # 6, 2. , 5


