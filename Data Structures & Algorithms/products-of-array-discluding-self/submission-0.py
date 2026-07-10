class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]
        for i,n in enumerate(nums):
            for j,_ in enumerate(nums):
                if i != j:
                    output[j] = output[j] * n
        
        return output