from typing import Counter, List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter()
        for x in nums:
            if x % 2 == 0:
                count[x] += 1
        res, ct = -1, 0
        for k, v in count.items():
            if res == -1 or v > ct or (v == ct and res > k):
                res = k
                ct = v
        return res
    
if __name__  == '__main__':
    nums = [0,1,2,2,4,4,1]
    nums = [4,4,4,9,2,4]
    nums = [29,47,21,41,13,37,25,7]
    rtn = Solution().mostFrequentEven(nums)
    print(rtn)