class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        for i in range(len(code)):
            if len(code[i])>0 and all(c.isalnum() or c == '_' for c in code[i]) and businessLine[i] in ("electronics", "grocery", "pharmacy", "restaurant") and isActive[i]:
                res.append([code[i], businessLine[i]])
        
        res.sort(key = lambda x : x[0])
        res.sort(key = lambda x : x[1])
        return [i[0] for i in res]