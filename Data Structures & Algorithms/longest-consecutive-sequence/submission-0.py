class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find numbers that start sequences
        seen = set(nums)
        starters = []
        for n in nums:
            if n-1 not in seen:
                starters.append(n)

        largest = 0

        for s in starters:
            n = s + 1
            while(n in seen):
                n += 1
            if (n-s > largest):
                largest = n-s
        
        return largest
