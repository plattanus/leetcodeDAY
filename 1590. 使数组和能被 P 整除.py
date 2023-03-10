from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k = sum(nums) % p
        if k == 0:
            return 0
        last = {0: -1}
        cur = 0
        ans = len(nums)
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            target = (cur - k + p) % p
            if target in last:
                ans = min(ans, i - last[target])
            last[cur] = i
        return -1 if ans == len(nums) else ans

if __name__  == '__main__':
    nums = [3,1,4,2]
    p = 6
    nums = [6,3,5,2]
    p = 9
    nums = [1,2,3]
    p = 3
    rtn = Solution().minSubarray(nums, p)
    print(rtn)
