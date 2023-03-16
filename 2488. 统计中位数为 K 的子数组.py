from typing import Counter, List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        kIndex = nums.index(k)
        ans = 0
        counts = Counter()
        counts[0] = 1
        sum = 0
        for i, num in enumerate(nums):
            if num - k > 0:
                sum += 1
            elif num -k < 0:
                sum -= 1
            if i < kIndex:
                counts[sum] += 1
            else:
                prev0 = counts[sum]
                prev1 = counts[sum - 1]
                ans += prev0 + prev1
        return ans

    
if __name__  == '__main__':


    nums = [3,2,1,4,5]
    k = 4
    nums = [2,3,1]
    k = 3
    rtn = Solution().countSubarrays(nums, k)
    print(rtn)