import itertools
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        leftSum = list(itertools.accumulate(nums))
        rightSum = list(itertools.accumulate(nums[::-1]))
        return list(abs(leftSum[i]-rightSum[len(nums)-i-1]) for i in range(len(nums)))

if __name__  == '__main__':
    nums = [10,4,8,3]
    nums = [1]
    rtn = Solution().leftRigthDifference(nums)
    print(rtn)
