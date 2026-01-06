import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.even = True

    def addNum(self, num: int) -> None:
        if self.even:
            heappush(self.min_heap, num)
            heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, -num)
            heappush(self.min_heap, -heappop(self.max_heap))

        self.even = not self.even
       
    def findMedian(self) -> float:
        if self.even:
            left_max = -self.max_heap[0]
            right_min = self.min_heap[0]
            return (left_max + right_min) / 2
        else:
            left_max = -self.max_heap[0]
            return left_max
            


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()