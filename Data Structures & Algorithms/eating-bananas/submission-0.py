class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            kVal = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/kVal)

            if hours <= h:
                res = min(res, kVal)
                right = kVal - 1
            else:
                left = kVal + 1

        return res
        