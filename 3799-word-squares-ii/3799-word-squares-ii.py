class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        res = []
        n = len(words)
        
        for top in words:
            for left in words:
                for right in words:
                    for bottom in words:
                        if top[0] == left[0] and top[-1] == right[0]:
                            if bottom[0] == left[-1] and bottom[-1] == right[-1]:
                                square = [top, left, right, bottom]
                                if len(set(square)) == 4:
                                    res.append(square)

        return sorted(res)