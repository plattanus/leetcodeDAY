from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # snums = sorted(set(nums))
        # mx = 1
        # t = 1
        # for i in range(1, len(snums)):
        #     if snums[i] == snums[i-1]+1:
        #         t += 1
        #         mx = max(t,mx)
        #     else:
        #         t = 1
        # return mx
        setnums = set(nums)
        mx = 1

        for num in nums:
            if num - 1 not in setnums:
                res = 1
                t = num+1
                while t in setnums:
                    res += 1
                    t += 1
                mx = max(mx,res)
                if mx > len(nums)/2+1:
                    break
        return mx
    
if __name__  == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    rtn = Solution().longestConsecutive(nums)
    print(rtn)