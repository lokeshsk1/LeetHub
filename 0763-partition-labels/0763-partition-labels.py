class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = dict()

        for i in range(len(s)):
            last[s[i]] = i
        
        start = 0
        res = []

        while start < len(s):
            
            end = last[s[start]]

            j = start
            while j < end:
                end = max(end, last[s[j]])
                j += 1
                
            res.append(end-start+1)

            start = end + 1

        return res

            
