from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter((x & y) for x in nums for y in nums)
        
        ans = 0
        for x in nums:
            for mask, freq in cnt.items():
                if (x & mask) == 0:
                    ans += freq
        return ans

if __name__  == '__main__':
    nums = [2,1,3]
    nums = [0,0,0]
    rtn = Solution().countTriplets(nums)
    print(rtn)