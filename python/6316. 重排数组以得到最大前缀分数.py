from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        numss = sorted(nums)
        sum = 0
        ans = 0
        for i in range(len(nums)-1, -1 , -1):

            sum += numss[i]
            if sum <= 0:
                break
            ans += 1
        return ans
    
if __name__  == '__main__':
    nums = [2,-1,0,1,-3,3,-3]
    nums = [-2,-3,0]
    rtn = Solution().maxScore(nums)
    print(rtn)