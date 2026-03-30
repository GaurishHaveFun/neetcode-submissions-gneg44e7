class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num1 = 0
        num2 = 0
        res = 0

        for i in range(len(tokens)):
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2) + int(num1)
                stack.append(res)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2) - int(num1)
                stack.append(res)
            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2) * int(num1)
                stack.append(res)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(int(num2) / int(num1))
                stack.append(res)
            else:
                stack.append(tokens[i])
        
        return int(stack.pop())