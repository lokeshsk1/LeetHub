class Solution:
    def kthCharacter(self, k: int) -> str:
        
        w = "a"

        while len(w) < k:

            for c in w:
                w += chr(ord(c)+1)
        
        print(w)
        return w[k-1]