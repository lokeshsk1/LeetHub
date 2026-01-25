class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        
        v = len([i for i in s if i in 'aeiou'])
        c = len([i for i in s if i.isalpha() and i not in 'aeiou'])

        print(v,c)

        if c > 0:
            return v // c
        return 0