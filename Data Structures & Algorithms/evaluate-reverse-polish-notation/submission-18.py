import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opMap = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a / b)}
        for i in tokens:
            if i not in opMap:
                stack.append(int(i))
            else:
                    second = stack.pop()
                    first = stack.pop()
                    calculation = opMap[i]
                    result = calculation(first, second)
                    stack.append(result)
        return int(stack[-1]) 
                    

