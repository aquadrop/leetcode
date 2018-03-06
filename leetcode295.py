
from queue import PriorityQueue

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_pq = PriorityQueue()
        self.right_pq = PriorityQueue()
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.left_pq.qsize() == 0:
            self.left_pq.put_nowait(-num)

        if num < self.left_pq.get():
            self.left_pq.put_nowait(num)
        else:
            self.right_pq.put_nowait(num)
        self.count += 1

    def findMedian(self):
        """
        :rtype: float
        """



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()