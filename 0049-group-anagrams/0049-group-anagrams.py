class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)

        for s in strs:
            ss = "".join(sorted(s))
            hmap[ss].append(s)
            
        return list(hmap.values())