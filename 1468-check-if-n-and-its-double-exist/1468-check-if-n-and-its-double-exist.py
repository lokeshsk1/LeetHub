class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        Set = set()
        for i in arr:
            if i/2 in Set or i*2 in Set:
                return True
            Set.add(i)
        
        return False