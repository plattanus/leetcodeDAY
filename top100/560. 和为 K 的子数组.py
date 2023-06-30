from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        nowsum = 0
        while left < len(nums):
            while right < len(nums):
                if nowsum >= k:
                    break
                nowsum += nums[right]
                right += 1
            # print(nowsum, left, right)
            if nowsum == k:
                res += 1
            nowsum -= nums[left]
            left += 1
        return res
if __name__  == '__main__':
    nums = [-1, -1, 2, 1]
    k = 1
    nums = [1]
    k = -1
    rtn = Solution().subarraySum(nums, k)
    print(rtn)