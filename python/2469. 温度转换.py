from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

if __name__  == '__main__':
    celsius = 36.50
    celsius = 122.11
    rtn = Solution().convertTemperature(celsius)
    print(rtn)