class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while r >= l:
            k = (r+l)//2
            total = 0
            for p in piles:
                total += -(-p//k)
            print(f'k = {k}, total = {total}')
            if total <= h:
                r = k - 1
                res = min(res, k)
            elif total > h:
                l = k + 1
        return res