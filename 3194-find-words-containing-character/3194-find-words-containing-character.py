class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        res = []
        for i,e in enumerate(words):
            if x in e:
                res.append(i)
        return res
