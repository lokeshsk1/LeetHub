class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {'}':'{', ')':'(', ']':'['}

        st = []

        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if not st or st[-1] != pair[i]:
                    return False
                st.pop()
        
        # print(st)
        return st == []
