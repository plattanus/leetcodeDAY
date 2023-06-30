class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        radius *= radius
        def check(A, b, c):
            c += 1
            for i in range(b, c):
                if A + i * i <= radius:
                    return True
            return False
        res = check(x1 * x1, y1, y2) or check(x2 * x2, y1, y2) or check(y1 * y1, x1, x2) or check(y2 * y2, x1, x2)
        if res:
            return res
        if min(x1, x2) < 0 and max(x1, x2) > 0 and min(y1, y2) < 0 and max(y1, y2) > 0:
            res = True
        return res

if __name__  == '__main__':
    radius = 1
    xCenter = 1
    yCenter = 1
    x1 = -3
    y1 = -3
    x2 = 3
    y2 = 3

    rtn = Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    print(rtn)