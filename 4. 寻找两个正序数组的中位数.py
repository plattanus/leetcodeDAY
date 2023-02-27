from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = []
        i = 0
        j = 0
        while True:
            if i<len(nums1) and j<len(nums2):
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            elif i<len(nums1):
                nums.append(nums1[i])
                i += 1
            elif j<len(nums2):
                nums.append(nums2[j])
                j += 1
            else:
                break
        
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2

    
if __name__  == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    nums1 = [1,2]
    nums2 = [3,4]
    rtn = Solution().findMedianSortedArrays(nums1, nums2)
    print(rtn)