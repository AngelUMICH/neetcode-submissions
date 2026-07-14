class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        size = len(heights)
        stack = [] # (index, height)
        maxarea = 0

        for i in range(size):
            lasti = i
            while stack and stack[-1][1] > heights[i]:
                j,h = stack.pop()
                w = i - j
                area = w * h
                maxarea = max(maxarea, area)
                lasti = j
            
            stack.append((lasti, heights[i]))

        while stack:
            i,h = stack.pop()
            w = size - i
            area = w * h
            maxarea = max(maxarea, area)

        return maxarea
