from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        maxProfit = totalProfit = operations = customersCount = 0
        for c in customers:
            operations += 1
            customersCount += c
            curCustomers = min(customersCount, 4)
            customersCount -= curCustomers
            totalProfit += boardingCost * curCustomers - runningCost
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                ans = operations

        if customersCount == 0:
            return ans

        profitEachTime = boardingCost * 4 - runningCost
        if profitEachTime <= 0:
            return ans

        if customersCount > 0:
            fullTimes = customersCount // 4
            totalProfit += profitEachTime * fullTimes
            operations += fullTimes
            if totalProfit > maxProfit:
                maxProfit = totalProfit
                ans = operations

            remainingCustomers = customersCount % 4
            remainingProfit = boardingCost * remainingCustomers - runningCost
            totalProfit += remainingProfit
            if totalProfit > maxProfit:
                operations += 1
                ans += 1
        return ans

if __name__  == '__main__':
    customers = [8,3]
    boardingCost = 5
    runningCost = 6

    customers = [10,9,6]
    boardingCost = 6
    runningCost = 4
    
    customers = [3,4,0,5,1]
    boardingCost = 1
    runningCost = 92

    rtn = Solution().minOperationsMaxProfit(customers, boardingCost, runningCost)
    print(rtn)