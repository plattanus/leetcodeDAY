


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [10002 for i in range(10002)]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[len(nums)-1]

if __name__  == '__main__':
    nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]
    rtn = Solution().jump(nums)
    print(rtn)
