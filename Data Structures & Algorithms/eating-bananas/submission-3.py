from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        floor = 1
        ceil = max(piles)
        res = ceil + 1
        while floor <= ceil:
            hours = 0
            mid = floor + math.ceil((ceil - floor) / 2)
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            if int(hours) == h:
                res = min(res, mid)
                if ceil == floor:
                    break
                ceil -= math.ceil((ceil - floor) / 2) 
            elif hours > h:
                floor = mid + 1
            else:
                res = min(res, int(mid))
                ceil = mid - 1
        return res

