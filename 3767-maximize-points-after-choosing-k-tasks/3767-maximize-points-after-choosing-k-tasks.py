class Solution:
    def maxPoints(self, t1: List[int], t2: List[int], k: int) -> int:
        # We want to pick exactly k tasks where taking t1 gives better gain
        # Gain difference if we choose t1 instead of t2
        # Positive diff => better to choose t1
        import heapq

        n = len(t1)
        min_heap = []  # keep top k positive diffs (smallest diff pops first)

        # Push all diffs into min-heap, but keep size <= k
        for i in range(n):
            diff = t1[i] - t2[i]
            heapq.heappush(min_heap, (diff, i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        selected = {idx for _, idx in min_heap}

        # Compute maximum score
        res = 0
        for i in range(n):
            if i in selected:
                res += t1[i]  # forced to pick t1
            else:
                res += max(t1[i], t2[i])  # free to pick best

        return res
