class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        smap = defaultdict(int)
        tmap = defaultdict(int)

        for i in range(len(s)):
            
            if smap[s[i]] != tmap[t[i]]:
                print(s[i], t[i])
                return False

            smap[s[i]] = i+1
            tmap[t[i]] = i+1

        

        
        return True

