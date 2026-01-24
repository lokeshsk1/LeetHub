class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        

        c = Counter(nums)
        points = [0] * (max(nums)+1)

        for i in nums:
            points[i] += i

        points[1] = max(points[0], points[1])

        for i in range(2, len(points)):
            points[i] = max(points[i-1], points[i-2]+points[i])

        return points[-1]
