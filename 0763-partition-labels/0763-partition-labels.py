class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = dict()

        for i in range(len(s)):
            last[s[i]] = i
        
        start = 0
        res = []

        while start < len(s):
            
            fin = last[s[start]]

            j = start
            while j < fin:
                fin = max(fin, last[s[j]])
                j += 1
                
            print(start, fin, fin-start+1)
            res.append(fin-start+1)

            start = fin + 1

        return res

            
