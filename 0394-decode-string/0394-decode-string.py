class Solution:
    def decodeString(self, s: str) -> str:
        
        decoded = []
        count = 0
        st = []
        
        for i in s:
            
            if i.isdigit():
                count = count*10 + int(i)
            elif i.isalpha():
                decoded.append(i)
            elif i == '[':
                st.append((decoded, count))
                decoded = []
                count = 0
            elif i == ']':
                prev_decoded , prev_count = st.pop()
                decoded = prev_decoded + (decoded*prev_count)
        
        print(decoded)
        return "".join(decoded)
            