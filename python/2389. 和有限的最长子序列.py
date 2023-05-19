from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = list(accumulate(sorted(nums)))
        return [bisect_right(f, q) for q in queries]
    
if __name__  == '__main__':
    nums = [4,5,2,1]
    queries = [3,10,21]
    nums = [2,3,4,5]
    queries = [1]
    rtn = Solution().answerQueries(nums, queries)
    print(rtn)