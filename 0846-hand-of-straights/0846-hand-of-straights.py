class Solution:
    def isNStraightHand(self, hand: List[int], g: int) -> bool:

        while hand:

            mn = min(hand)

            for j in range(mn, mn+g):
                try:
                    hand.remove(j)
                    print(j)
                except:
                    return False
        
        return True
            


