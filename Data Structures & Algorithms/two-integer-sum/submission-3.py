class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,num in enumerate(nums):
            indices[num] = i

        for j,num in enumerate(nums):
            if target-num in indices and indices[target-num] != j:
                return [j, indices[target-num]]