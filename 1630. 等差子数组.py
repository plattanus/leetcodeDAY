from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = list()
        for left, right in zip(l, r):
            minv = min(nums[left:right+1])
            maxv = max(nums[left:right+1])
            
            if minv == maxv:
                ans.append(True)
                continue
            if (maxv - minv) % (right - left) != 0:
                ans.append(False)
                continue
            
            d = (maxv - minv) // (right - left)
            flag = True
            seen = set()
            for j in range(left, right + 1):
                if (nums[j] - minv) % d != 0:
                    flag = False
                    break
                t = (nums[j] - minv) // d
                if t in seen:
                    flag = False
                    break
                seen.add(t)
            ans.append(flag)
        
        return ans


if __name__  == '__main__':
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]

    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]

    rtn = Solution().checkArithmeticSubarrays(nums, l, r)
    print(rtn)