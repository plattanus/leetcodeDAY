from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})

if __name__  == '__main__':
    nums = [1,5,0,3,5]
    nums = [0]
    rtn = Solution().minimumOperations(nums)
    print(rtn)