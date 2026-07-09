class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = ''.join(sorted(s1))

        start = 0

        for end in range(len(s1)-1, len(s2)):

            if end - start + 1 > len(s1):
                start += 1
            
            if ''.join(sorted(s2[start:end+1])) == s1:
                return True

        return False