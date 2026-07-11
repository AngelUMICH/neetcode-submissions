class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        leftP = '({['
        rightP = ')}]'

        for p in s:
            stack.append(p)
            if p in rightP and len(stack) > 1:
                lastP = stack[-2]
                if lastP in leftP and p == rightP[leftP.find(stack[-2])]:
                    stack.pop() # pop right parenthesis
                    stack.pop() # pop left parenthesis
        
        return len(stack) == 0