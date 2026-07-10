class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <1:
            return False
        valueset = []
        valueset.append(nums[0])
        for i in nums[1:]:
            if i in valueset:
                return True
            else:
                valueset.append(i)
        return False
