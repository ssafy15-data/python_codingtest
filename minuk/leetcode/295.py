import heapq

class MedianFinder:
    count = 0
    min_heap = []
    max_heap = []

    def __init__(self):
        self.count = 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if (self.count % 2):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        self.count += 1
        if (self.min_heap and -(self.max_heap[0]) > self.min_heap[0]):
            min_value, max_value = heapq.heappop(self.min_heap), -(heapq.heappop(self.max_heap))
            heapq.heappush(self.min_heap, max_value)
            heapq.heappush(self.max_heap, -min_value)
        
    def findMedian(self) -> float:
        if (self.count % 2):
            return -(self.max_heap[0])
        else:
            return (-(self.max_heap[0]) + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()