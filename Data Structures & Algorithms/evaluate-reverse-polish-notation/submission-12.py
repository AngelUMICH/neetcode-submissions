class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arith = "+-*/"
        val1 = 0
        val2 = 0
        val = 0

        for t in tokens:
            if t in arith:
                print(stack,t)
                val2 = stack.pop()
                val1 = stack.pop()
                if t == '+':
                    val = val1 + val2
                elif t == '-':
                    val = val1 - val2
                elif t == '*':
                    val = val1 * val2
                elif t == '/':
                    val = val1 / val2
                stack.append(int(val))
            if t not in arith:
                stack.append(int(t))
        return stack[-1]
