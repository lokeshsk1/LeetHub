class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        for i,e in enumerate(sentence.split()):
            if e.startswith(searchWord):
                return i+1
        
        return -1

        