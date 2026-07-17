class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) <= len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        total = len(A) + len(B)
        half = total // 2
        even = total % 2 == 0
        
        l,r = 0, len(B) - 1
        while True:
            i = (r+l) // 2
            j = half - i - 2

            leftA = A[j] if j >= 0 else float('-infinity')
            rightA = A[j+1] if (j+1) < len(A) else float('infinity')
            leftB = B[i] if i >= 0 else float('-infinity')
            rightB = B[i+1] if (i+1) < len(B) else float('infinity')
            print(f'i={i}, j={j} | l={0}, r={r}')
            print(f'A: {A[:j+1]} | {rightA}')
            print(f'B: {B[:i+1]} | {rightB}')
            print(leftA, leftB, rightA, rightB)
            if leftA <= rightB and leftB <= rightA:
                if even:
                    return (max(leftA,leftB)+min(rightA,rightB))/2
                else:
                    return min(rightA,rightB)

            if leftB > rightA:
                r = i - 1
            else:
                l = i + 1
        