class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        res = []
        n = len(words)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if words[i][0] == words[j][0] and words[i][-1] == words[k][0]:
                            if words[l][0] == words[j][-1] and words[l][-1] == words[k][-1]:
                                square = (words[i], words[j], words[k], words[l])
                                if len(set(square)) == 4:
                                    res.append(square)

        return sorted(res)