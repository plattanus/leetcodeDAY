from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for i in range(1, len(nums)):
            t = nums[i] + nums[i-1]
            if t in s:
                return True
            s.add(t)
        return False

if __name__  == '__main__':
    nums = [4,2,4]
    nums = [1,2,3,4,5]
    nums = [0,0,0]
    rtn = Solution().findSubarrays(nums)
    print(rtn)