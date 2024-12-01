class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        vis = set()
        for i in arr:
            if i/2 in vis or i*2 in vis:
                return True
            vis.add(i)
        
        return False