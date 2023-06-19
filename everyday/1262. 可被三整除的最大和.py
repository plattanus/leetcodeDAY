from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        def mincheck(d1,d2):
            ld1 = len(d1)
            ld2 = len(d2)
            if ld1%3==1 and ld2%3==0:
                return min(d1[0],d2[0]+d2[1])
            if ld1%3==1 and ld2%3==2:
                if ld1 != 1:
                    return min(d1[0]+d1[1],d2[0])
                return d2[0]
            if ld1%3==2 and ld2%3==0:
                return min(d1[0]+d1[1],d2[0])
            if ld1%3==2 and ld2%3==1:
                if ld2 != 1:
                    return min(d1[0],d2[0]+d2[1])
                return d1[0]
            if ld1%3==0 and ld2%3==2:
                return min(d1[0],d2[0]+d2[1])
            if ld1%3==0 and ld2%3==1:
                return min(d1[0]+d1[1],d2[0])
        res = 0
        d1 = []
        d2 = []
        for num in nums:
            if num%3 == 0:
                res += num
            elif num%3 == 1:
                d1.append(num)
            else:
                d2.append(num)
        if len(d1) == len(d2) or len(d1)%3 == len(d2)%3:
            return res + sum(d1) + sum(d2)
        d1 = sorted(d1)
        d2 = sorted(d2)
        # print(d1,d2)
        if len(d1) == 0:
            if len(d2)%3 == 1:
                return res + sum(d2) - d2[0]
            return res + sum(d2) - d2[0] - d2[1]
        if len(d2) == 0:
            if len(d1)%3 == 1:
                return res + sum(d1) - d1[0]
            return res + sum(d1) - d1[0] - d1[1]
        return res + sum(d1) + sum(d2) - mincheck(d1,d2)

if __name__  == '__main__':
    nums = [2,3,36,8,32,38,3,30,13,40]
    rtn = Solution().maxSumDivThree(nums)
    print(rtn)