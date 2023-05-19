from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        snums = sorted(nums)
        snums = snums[::-1]
        # print(snums)
        res = 0
        vis = [0 for _ in range(len(nums))]
        i = len(nums)//2
        for j in range(len(nums)):
            while i<(len(nums)):
                if 2 * snums[i] <= snums[j]:
                    if vis[i] == 0 and vis[j] == 0:
                        vis[i] = vis[j] = 1
                        print(snums[i], snums[j])
                        res += 2
                        break
                i += 1
            vis[j] = 1
        return res
    
if __name__  == '__main__':
    nums = [3,5,2,4]
    nums = [9,2,5,4]
    nums = [7,6,8]
    rtn = Solution().maxNumOfMarkedIndices(nums)
    print(rtn)