class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        st = []

        for i in range(len(prices)):

            while st and prices[st[-1]] >= prices[i]:
                prices[st[-1]] -= prices[i]
                st.pop()
            
            st.append(i)
        
        return prices


