class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        

        word_set = set(wordList)
        q = [beginWord]
        depth = 0

        if endWord not in word_set:
            return 0
        
        while q:
            n = len(q)
            depth += 1
            for _ in range(n):

                curr = q.pop(0)
                print(curr)

                for i in range(len(curr)):
                    for j in range(0, 26):
                        newWord = curr[:i] + chr(j + ord('a')) + curr[i+1:]
                        # print(newWord)

                        if newWord == endWord:
                            return depth+1
                        
                        if newWord in word_set:
                            q.append(newWord)
                            word_set.remove(newWord)
                
        return 0


