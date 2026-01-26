class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        min1 = min2 = float("inf")

        for i in prices:

            if i < min1:
                min1, min2 = i, min1
            elif i < min2:
                min2 = i
        
        res = money - min1 - min2
        if res < 0:
            return money
        return res