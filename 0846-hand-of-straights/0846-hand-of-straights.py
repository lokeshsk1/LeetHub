class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:

        c = Counter(hand)

        for i in sorted(c):
            if c[i] > 0:
                curr = c[i]
                for j in range(g):
                    c[i+j] -= curr
                    if c[i+j] < 0:
                        return False
        
        return True
            


