class MedianFinder:

    def __init__(self):
        self.int_list = []

    def addNum(self, num: int) -> None:
        self.int_list.append(num)

    def findMedian(self) -> float:
        # sort가 O(NlogN)이니까 TLE 날 것
        # 다른 방법 생각 안 나네
        self.int_list.sort()
        N = len(self.int_list)
        half = N // 2
        if N % 2 == 1:
            return float(self.int_list[half])
        else:
            return (self.int_list[half - 1] + self.int_list[half]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()