from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        def Cal(pos) -> int:
            sumA = 0
            for i in range(pos, len(nums), 2):
                sumT = 0
                if i - 1 >= 0:
                    sumT = max(sumT, nums[i] - nums[i - 1] + 1)
                if i + 1 < len(nums):
                    sumT = max(sumT, nums[i] - nums[i + 1] + 1)
                sumA += sumT
            return sumA


        return min(Cal(0), Cal(1))
    
if __name__  == '__main__':
    nums = [1,2,3]
    nums = [9,6,1,6,2]
    rtn = Solution().movesToMakeZigzag(nums)
    print(rtn)