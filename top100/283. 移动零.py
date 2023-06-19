from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swappos = 0
        i = 0
        while i<len(nums):
            while nums[i] == 0:
                swappos += 1
                i += 1
                if i>=len(nums):
                    break
            if i<len(nums):
                nums[i], nums[i-swappos] = nums[i-swappos], nums[i]
            i+=1
if __name__  == '__main__':
    nums = [1,1,0,1,0,3,12,0,1,1]
    rtn = Solution().moveZeroes(nums)
    print(rtn)