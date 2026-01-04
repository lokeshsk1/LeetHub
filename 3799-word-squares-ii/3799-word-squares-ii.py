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
                                resl = set()
                                resl.add(words[i])
                                resl.add(words[j])
                                resl.add(words[k])
                                resl.add(words[l])
                                if len(resl) == 4:
                                    res.append([words[i], words[j], words[k], words[l]])

        res.sort()
        return res