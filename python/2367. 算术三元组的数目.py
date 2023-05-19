from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for num in nums:
            if num + diff in nums and num + diff + diff in nums:
                ans += 1
        return ans
    

if __name__  == '__main__':
    nums = [0,1,4,6,7,10]
    diff = 3
    nums = [4,5,6,7,8,9]
    diff = 2
    rtn = Solution().arithmeticTriplets(nums, diff)
    print(rtn)