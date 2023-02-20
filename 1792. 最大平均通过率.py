import heapq
from typing import List

class Comp:
    def __init__(self, p: int, t: int, ):
        self.p = p
        self.t = t
        self._calV()
    def __lt__(self, other):
        return self.calV > other.calV
    
    def _calV(self):
        self.calV = (self.p + 1)/(self.t + 1) -self.p/self.t

class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        heap = []
        for i in classes:
            heapq.heappush(heap, Comp(i[0],i[1]))

        for i in range(extraStudents):
            htmp = heapq.heappop(heap)
            # print(htmp.p, htmp.t)
            heapq.heappush(heap, Comp(htmp.p + 1, htmp.t + 1))

        sum_av = 0
        while len(heap) > 0:
            htmp = heapq.heappop(heap)
            sum_av += htmp.p/htmp.t
        return sum_av / len(classes)

if __name__  == '__main__':
    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    # classes = [[2,4],[3,9],[4,5],[2,10]]
    # extraStudents = 4
    rtn = Solution().maxAverageRatio(classes, extraStudents)
    print(rtn)