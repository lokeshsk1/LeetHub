class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        res = float('inf')
        hmap = defaultdict(list)

        for i in range(len(nums)):
            hmap[nums[i]].append(i)
        
        for i,j in hmap.items():
            if len(j) >= 3:
                for k in range(len(j)-2):
                    res = min(res, 2*(max(j[k:k+3]) - min(j[k:k+3])))

        return -1 if res==float(inf) else res

