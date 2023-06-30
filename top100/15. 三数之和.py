from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # count = Counter(nums)
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         t = 0 - nums[i] - nums[j]
        #         if nums[i] == nums[j]:
        #             if t != nums[i] and count[t] >= 1:
        #                 res.add(tuple(sorted([nums[i], nums[j], t])))
        #             if t == nums[i] and count[t] >= 3:
        #                 res.add(tuple(sorted([nums[i], nums[j], t])))
        #         else:
        #             if t == nums[i] and count[t] >= 2:
        #                 res.add(tuple(sorted([nums[i], nums[j], t])))
        #             if t ==nums[j] and count[t] >= 2:
        #                 res.add(tuple(sorted([nums[i], nums[j], t])))
        #             if t != nums[i] and t != nums[j] and count[t] >= 1:
        #                 res.add(tuple(sorted([nums[i], nums[j], t])))
        # return [list(elem) for elem in res]
        positives, negatives, zeros = [], [], []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros.append(num)
        res = []
        if len(zeros) >= 3:
            res.append([0, 0, 0])
        positives.sort()
        negatives.sort()
        setpositives = set(positives)
        setnegatives = set(negatives)
        if len(zeros) >= 1:
            for negative in setnegatives:
                if -negative in setpositives:
                    res.append([0, negative, -negative])

        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                if -(negatives[i] + negatives[j]) in setpositives:
                    res.append([negatives[i], negatives[j], -(negatives[i] + negatives[j])])
        
        for i in range(len(positives)):
            for j in range(i+1,len(positives)):
                if -(positives[i] + positives[j]) in setnegatives:
                    res.append([positives[i], positives[j], -(positives[i] + positives[j])])
        return [list(v) for v in set([tuple(v) for v in res])]
    
if __name__  == '__main__':
    nums = [9,-1,0,1,2,-1,-4]
    rtn = Solution().threeSum(nums)
    print(rtn)