class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        res = 0

        for i,f in enumerate(fruits):
            for j,b in enumerate(baskets):
                if f <= b:
                    res += 1
                    baskets[j] = 0
                    break
        
        return len(fruits) - res
        
