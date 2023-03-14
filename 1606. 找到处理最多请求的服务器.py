from heapq import heappop, heappush
from typing import List
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]

if __name__  == '__main__':
    k = 3
    arrival = [1,2,3,4,5]
    load = [5,2,3,3,3]

    k = 3
    arrival = [1,2,3,4]
    load = [1,2,1,2]                                    

    k = 3
    arrival = [1,2,3]
    load = [10,12,11]

    k = 3
    arrival = [1,2,3,4,8,9,10]
    load = [5,2,10,3,1,2,2]

    k = 1
    arrival = [1]
    load = [1]
    
    rtn = Solution().busiestServers(k, arrival, load)
    print(rtn)